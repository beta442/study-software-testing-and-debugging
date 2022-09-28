import sys
import typing
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

import requests
import validators
import queue


def _url_is_reachable(url: str, timeout=10):
	try:
		req = requests.head(url, allow_redirects=True, timeout=timeout)
		return url, req.ok, req.status_code
	except Exception:
		return url, False, 500


class WebPageRedirectUrlsChecker:
	def __init__(self, url: str, chrome_driver_path="", log=False, log_file=sys.stdout):
		if not validators.url(url):
			raise ValueError("WebPageRedirectUrlsChecker: invalid url provided")

		options = webdriver.chrome.options.Options()
		options.add_argument('--log-level=3')
		options.add_argument('--headless')
		options.add_argument('--ignore-certificate-errors-spki-list')
		options.add_argument('--ignore-ssl-errors')
		options.add_experimental_option('excludeSwitches', ['enable-logging'])
		self._google_driver = webdriver.Chrome(options=options) if chrome_driver_path == "" else webdriver.Chrome(
			chrome_driver_path, options=options)

		self._url = url
		self._hostname = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))
		self._ok_urls: set[tuple[str, int]] = set()
		self._bad_urls: set[tuple[str, int]] = set()
		self._log_file: typing.IO = log_file
		self._are_logging: bool = log

	def __del__(self):
		self._google_driver.quit()

	def _is_logging(self) -> bool:
		return self._are_logging

	def scan(self) -> None:
		page_queue = queue.Queue()
		scanned_pages: set[str] = set()

		scanned_pages.add(self._url)
		page_queue.put(self._url)

		while not page_queue.empty():
			page = page_queue.get()

			links_to_validate = set()
			try:
				if (page[-1:] == '#' and
						page[:-1] in scanned_pages):
					continue
				self._google_driver.get(page)
				link_list = self._google_driver.find_elements(by=By.TAG_NAME, value='a')

				for link in link_list:
					link_url = link.get_attribute('href')

					parsed_uri = urlparse(link_url)
					host_name = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

					if (link_url and
							link_url not in scanned_pages and
							link_url not in links_to_validate and
							host_name == self._hostname):
						links_to_validate.add(link_url)

						if self._is_logging():
							print(f"On page '{page}'. Found link '{link_url}'.", file=self._log_file)

			except Exception:
				raise ConnectionError('Can''t scan page:' + page)

			with ThreadPoolExecutor(max_workers=20) as executor:
				req_futures = [executor.submit(_url_is_reachable, _link) for _link in links_to_validate]

				for req_future in as_completed(req_futures):
					(url, is_valid_link, status) = req_future.result()

					if self._is_logging():
						print(f"Url '{url}' is " + ('reachable' if is_valid_link else 'unreachable') +
						      f'. Code is {status}',
						      file=self._log_file)

					if is_valid_link:
						if url not in scanned_pages:
							page_queue.put(url)
							self._ok_urls.add((url, status))
					else:
						self._bad_urls.add((url, status))

					scanned_pages.add(url)

	def get_ok_urls(self) -> set[tuple[str, int]]:
		return self._ok_urls

	def get_bad_urls(self) -> set[tuple[str, int]]:
		return self._bad_urls
