import xml.etree.ElementTree as ET

from .base import FileProcessorStrategy


class XmlProcessor(FileProcessorStrategy):
    file_type = "xml"

    def get_count(self, file_content):
        try:
            root = ET.fromstring(file_content)
        except ET.ParseError as error:
            raise ValueError("Invalid XML") from error

        return len(list(root))
