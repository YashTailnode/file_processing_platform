from .csv_processor import CsvProcessor
from .json_processor import JsonProcessor
from .xml_processor import XmlProcessor


class ProcessorFactory:
    _strategies = {
        "csv": CsvProcessor,
        "json": JsonProcessor,
        "xml": XmlProcessor,
    }

    @classmethod
    def create_strategy(cls, file_type):
        strategy = cls._strategies.get(file_type.lower())

        if strategy is None:
            raise ValueError(f"Unsupported file type: {file_type}")

        return strategy()
