import json

from .base import FileProcessorStrategy


class JsonProcessor(FileProcessorStrategy):
    file_type = "json"

    def get_count(self, file_content):
        try:
            parsed_content = json.loads(file_content)
        except json.JSONDecodeError as error:
            raise ValueError("Invalid JSON") from error

        if isinstance(parsed_content, list):
            return len(parsed_content)

        return 1
