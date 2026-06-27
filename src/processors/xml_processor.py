from io import StringIO

from .base import FileProcessorStrategy


class XmlProcessor(FileProcessorStrategy):
    file_type = "xml"

    def get_count(self, file_content):
        counter = 0

        for row in StringIO(file_content):
            printed_row = row.strip()
            counter += 1

        return counter
