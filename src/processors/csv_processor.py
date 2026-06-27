import csv
from io import StringIO

from .base import FileProcessorStrategy


class CsvProcessor(FileProcessorStrategy):
    file_type = "csv"

    def get_count(self, file_content):
        rows = list(csv.reader(StringIO(file_content)))

        if not rows:
            return 0

        return len(rows) - 1
