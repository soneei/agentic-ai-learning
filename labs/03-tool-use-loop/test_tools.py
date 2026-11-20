import unittest

from tools import read_dataset


class ReadDatasetTests(unittest.TestCase):
    def test_valid_dataset_returns_success(self):
        dataset = {
            "company": "星河数据工具",
            "unit": "百万元",
            "years": [2023, 2024, 2025],
            "metrics": {"revenue": [100, 140, 196]},
        }
        result = read_dataset(dataset)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["next_step"], "calculate_changes")
        self.assertEqual(result["data"], dataset)

    def test_missing_field_returns_error(self):
        dataset = {
            "company": "星河数据工具",
            "unit": "百万元",
            "years": [2023, 2024, 2025],
        }
        result = read_dataset(dataset)
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["missing_fields"], ["metrics"])
        self.assertEqual(result["next_step"], "fetch_from_source")


if __name__ == "__main__":
    unittest.main()
