try:
    from .processors.registry import ProcessorFactory
except ImportError:
    from processors.registry import ProcessorFactory


def process_file(file_type, file_content):
    if not file_content or not file_content.strip():
        raise ValueError("File content cannot be empty")

    strategy = ProcessorFactory.create_strategy(file_type)
    record_count = strategy.get_count(file_content)
    return {"record_count": record_count}


def processFile(fileType, fileContent):
    return process_file(fileType, fileContent)


def main():
    file_type = "csv"

    with open(f"data.{file_type}", "r", encoding="utf-8") as file:
        file_content = file.read()

    result = process_file(file_type, file_content)
    print(result)


if __name__ == "__main__":
    main()
