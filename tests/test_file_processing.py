import unittest

from src.main import process_file


class TestFileProcessing(unittest.TestCase):
    def test_csv_parsing_counts_rows_excluding_header(self):
        file_content = "id,name\n1,John\n2,Mary"

        result = process_file("csv", file_content)

        self.assertEqual(result, {"record_count": 2})

    def test_json_parsing_counts_records(self):
        file_content = '[{"id": 1}, {"id": 2}]'

        result = process_file("json", file_content)

        self.assertEqual(result, {"record_count": 2})

    def test_xml_parsing_counts_records(self):
        file_content = """
        <records>
            <record>
                <id>1</id>
            </record>
            <record>
                <id>2</id>
            </record>
        </records>
        """

        result = process_file("xml", file_content)

        self.assertEqual(result, {"record_count": 2})

    def test_unsupported_file_type_raises_error(self):
        with self.assertRaisesRegex(ValueError, "Unsupported file type: yaml"):
            process_file("yaml", "id: 1")

    def test_empty_content_raises_error(self):
        with self.assertRaisesRegex(ValueError, "File content cannot be empty"):
            process_file("csv", "")

    def test_malformed_json_raises_error(self):
        with self.assertRaisesRegex(ValueError, "Invalid JSON"):
            process_file("json", '{"id": 1')

    def test_malformed_xml_raises_error(self):
        with self.assertRaisesRegex(ValueError, "Invalid XML"):
            process_file("xml", "<records><record></records>")


if __name__ == "__main__":
    unittest.main()
