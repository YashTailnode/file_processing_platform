import json

from .base import FileProcessorStrategy


class JsonProcessor(FileProcessorStrategy):
    file_type = "json"

    def get_count(self, file_content):
        counter = 0

        for row in file_content.splitlines():
            parsed_row = json.loads(row)
            length = len(parsed_row)
            counter += length

        return counter
