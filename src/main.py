try:
    from .processors.registry import ProcessorFactory
except ImportError:
    from processors.registry import ProcessorFactory


def processFile(fileType, fileContent):
    strategy = ProcessorFactory.create_strategy(fileType)
    return strategy.get_count(fileContent)


def main():
    file_type = "csv"

    with open(f"data.{file_type}", "r", encoding="utf-8") as file:
        file_content = file.read()

    count = processFile(file_type, file_content)
    print(count)


if __name__ == "__main__":
    main()
