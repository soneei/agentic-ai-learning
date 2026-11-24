import unittest

from tools import read_dataset, calculate_changes, check_data_quality


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


class CalculateChangesTests(unittest.TestCase):
    def test_growth_rate_calculation(self):
        read_result = read_dataset({
            "company": "星河数据工具",
            "unit": "百万元",
            "years": [2023, 2024, 2025],
            "metrics": {"revenue": [100, 140, 196]},
        })
        result = calculate_changes(read_result)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["next_step"], "check_data_quality")
        revenue_changes = result["data"]["changes"]["revenue"]
        self.assertEqual(revenue_changes[0]["growth_rate"], 0.4)
        self.assertEqual(revenue_changes[1]["growth_rate"], 0.4)

    def test_error_propagates_without_calculation(self):
        read_result = read_dataset({"company": "星河数据工具"})
        result = calculate_changes(read_result)
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["next_step"], "fetch_from_source")


class CheckDataQualityTests(unittest.TestCase):
    def _changes_of(self, metrics):
        read_result = read_dataset({
            "company": "星河数据工具",
            "unit": "百万元",
            "years": [2023, 2024, 2025],
            "metrics": metrics,
        })
        return calculate_changes(read_result)

    def test_normal_data_passes_to_summary(self):
        calc = self._changes_of({"revenue": [100, 140, 196]})
        result = check_data_quality(calc)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["flags"], [])
        self.assertEqual(result["next_step"], "generate_summary")

    def test_abnormal_growth_rate_flags_and_routes_to_verify(self):
        calc = self._changes_of({"revenue": [100, 300, 50]})
        result = check_data_quality(calc)
        self.assertEqual(result["status"], "warning")
        self.assertEqual(len(result["flags"]), 2)
        self.assertEqual(result["next_step"], "verify_source_and_calculation")

    def test_zero_base_rate_is_flagged(self):
        calc = self._changes_of({"revenue": [0, 50, 60]})
        result = check_data_quality(calc)
        issues = [f["issue"] for f in result["flags"]]
        self.assertIn("zero_base_growth_rate_undefined", issues)

    def test_upstream_error_propagates(self):
        read_result = read_dataset({"company": "星河数据工具"})
        calc = calculate_changes(read_result)
        result = check_data_quality(calc)
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["next_step"], "fetch_from_source")


if __name__ == "__main__":
    unittest.main()
