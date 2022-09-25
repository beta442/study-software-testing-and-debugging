import os
import typing

from attr import dataclass
from random import randint


@dataclass
class FileHandlerNameParams:
	path: str
	name: str
	datetime: str
	file_format: str


def get_output_files_handlers(file_name_params: list[FileHandlerNameParams], generate_id=False, encoding='utf-8') -> \
		list[typing.IO]:
	handlers: list[typing.IO] = list()
	for param in file_name_params:
		file_id: str = ''.join(['%s' % randint(0, 9) for digit in range(0, 6)]) if generate_id else ""
		file_path = os.path.join(param.path, param.name + '-' + param.datetime + ('-' if generate_id else '') +
		                         param.file_format)
		file = open(file_path, 'w', encoding=encoding)
		handlers.append(file)

	return handlers
