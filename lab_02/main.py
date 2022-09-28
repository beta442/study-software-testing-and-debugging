import argparse
import datetime
import sys

import WebPageRedirectUrlsChecker
from FileHandlersGenerator import *

_DATE_TIME_FORMAT = '%Y-%m-%d-%H-%M-%S'
_INVALID_LINKS_FILE_NAME = 'invalid-links'
_OUTPUT_FILES_ENCODING = 'utf-8'
_OUTPUT_FILE_FORMAT = '.txt'
_VALID_LINKS_FILE_NAME = 'valid-links'


def init_args_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(usage="Provide website's url and wait",
	                                 description="Script finds live and dead links on specified site")

	parser.add_argument("URL", help="URL of site that will be check")
	parser.add_argument("-v", "--verbose", help="Show additional info", action="store_true", dest="v")

	return parser


def print_links(links_with_status: set[tuple[str, int]], file: typing.IO):
	for item in links_with_status:
		link = item[0]
		status = item[1]
		file.write(f'{link} {status}\n')

	file.write(f'\nLinks amount: {len(links_with_status)}\n');


def main() -> None:
	parser = init_args_parser()
	args = parser.parse_args()

	urls_checker = WebPageRedirectUrlsChecker.WebPageRedirectUrlsChecker(args.URL, log=args.v)
	urls_checker.scan()

	ok_links = urls_checker.get_ok_urls()
	bad_links = urls_checker.get_bad_urls()

	start_time = datetime.datetime.now()
	datetime_string = start_time.strftime(_DATE_TIME_FORMAT)
	script_path = os.path.dirname(os.path.abspath(__file__))

	(valid_links_file, invalid_links_file) = get_output_files_handlers(
		[FileHandlerNameParams(script_path, _VALID_LINKS_FILE_NAME, datetime_string, '.txt'),
		 FileHandlerNameParams(script_path, _INVALID_LINKS_FILE_NAME, datetime_string, '.txt')])

	print_links(ok_links, valid_links_file)
	valid_links_file.write(f"{datetime_string}\n")

	print_links(bad_links, invalid_links_file)
	invalid_links_file.write(f"{datetime_string}\n")

	valid_links_file.close()
	invalid_links_file.close()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nUser interrupt", file=sys.stderr)
	except Exception:
		print("Unhandled exception occured")
		sys.exit(1)
