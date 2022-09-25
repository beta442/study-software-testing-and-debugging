import argparse
import datetime
import requests
import sys

import WebPageRedirectUrlsChecker
from FileHandlersGenerator import *

_DATE_TIME_FORMAT = '%Y-%m-%d-%H-%M-%S'
_INVALID_LINKS_FILE_NAME = 'invalid-links'
_OUTPUT_FILES_ENCODING = 'utf-8'
_OUTPUT_FILE_FORMAT = '.txt'
_VALID_LINKS_FILE_NAME = 'valid-links'


def init_args_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(usage="Provide website's url and specify output detsinations",
	                                 description="Script finds live and dead links on specified site")

	parser.add_argument("URL", help="URL of site that will be check")
	parser.add_argument("-v", "--verbose", help="Show additional info", action="store_true", dest="v")

	return parser


def main() -> None:
	parser = init_args_parser()
	args = parser.parse_args()

	start_time = datetime.datetime.now()
	datetime_string = start_time.strftime(_DATE_TIME_FORMAT)
	script_path = os.path.dirname(os.path.abspath(__file__))

	(valid_links_file, invalid_links_file) = get_output_files_handlers(
		[FileHandlerNameParams(script_path, _VALID_LINKS_FILE_NAME, datetime_string, '.txt'),
		 FileHandlerNameParams(script_path, _INVALID_LINKS_FILE_NAME, datetime_string, '.txt')])

	urls_checker = WebPageRedirectUrlsChecker.WebPageRedirectUrlsChecker(args.URL, log=args.v)
	urls_checker.scan()

	ok_links = urls_checker.get_ok_urls()
	bad_links = urls_checker.get_bad_urls()

	for item in ok_links:
		valid_links_file.write(f'{item[0]} {item[1]}\n')

	for item in bad_links:
		invalid_links_file.write(f'{item[0]} {item[1]}\n')

	valid_links_file.close()
	invalid_links_file.close()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nUser interrupt", file=sys.stderr)
# except Exception:
# 	print("Unhandled exception occured")
# 	sys.exit(1)
