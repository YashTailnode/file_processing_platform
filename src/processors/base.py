from abc import ABC, abstractmethod


class FileProcessorStrategy(ABC):
    file_type = ""

    @abstractmethod
    def get_count(self, file_content):
        pass
