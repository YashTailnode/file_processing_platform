# File Processing Platform

This project processes file content for supported formats and returns the number of records found.

Supported file types:

- CSV
- JSON
- XML

## Setup

Python 3 is required. This project currently uses only Python standard library modules, so no external packages are needed.

```bash
python3 --version
```

## Run the Application

From the project root:

```bash
python3 src/main.py
```

The core function is:

```python
process_file(file_type, file_content)
```

Example:

```python
from src.main import process_file

result = process_file("csv", "id,name\n1,John\n2,Mary")
print(result)
```

Output:

```python
{"record_count": 2}
```

## Run Tests

Tests should be placed in the `tests/` directory.

Using `unittest`:

```bash
python3 -m unittest discover tests
```

## Application Flow

```text
File Type + File Content
          |
          v
process_file(file_type, file_content)
          |
          v
Validate empty content
          |
          v
ProcessorFactory.create_strategy(file_type)
          |
          v
CSV / JSON / XML processor strategy
          |
          v
Parse file content and count records
          |
          v
Return {"record_count": count}
```

## Design Patterns

This project uses Factory + Strategy.

The `ProcessorFactory` selects the correct processor for the requested file type. Each processor implements the `FileProcessorStrategy` abstraction and owns the parsing/counting logic for one file format.

To add a new file type, such as YAML:

1. Create a new processor class that extends `FileProcessorStrategy`.
2. Implement `get_count(file_content)`.
3. Register the class in `ProcessorFactory`.

This keeps the main processing flow unchanged while allowing new formats to be added with minimal changes.

## Error Handling

The application raises meaningful `ValueError` messages for invalid input:

- `Unsupported file type: <file_type>`
- `File content cannot be empty`
- `Invalid JSON`
- `Invalid XML`
