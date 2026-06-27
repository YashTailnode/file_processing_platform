try:
    from ..processors.csv_processor import CsvProcessor
    from ..processors.json_processor import JsonProcessor
    from ..processors.xml_processor import XmlProcessor
except ImportError:
    from processors.csv_processor import CsvProcessor
    from processors.json_processor import JsonProcessor
    from processors.xml_processor import XmlProcessor


class StrategyFactory:
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
