from io import StringIO

from .base import FileProcessorStrategy


class CsvProcessor(FileProcessorStrategy):
    file_type = "csv"

    def get_count(self, file_content):
        counter = 0

        for row in StringIO(file_content):
            counter += 1

        return counter
