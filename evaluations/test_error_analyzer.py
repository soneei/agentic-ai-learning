import unittest

from error_analyzer import analyze, outcome_label
from orchestrator import run_loop


def good_data():
    return {
        "company": "星河数据工具",
        "unit": "百万元",
        "years": [2023, 2024, 2025],
        "metrics": {"revenue": [100, 140, 196]},
    }


class ErrorAnalyzerTests(unittest.TestCase):
    def test_outcome_label(self):
        run = run_loop(good_data())
        self.assertEqual(outcome_label(run), "completed")
        run2 = run_loop({"company": "星河数据工具"})
        self.assertEqual(outcome_label(run2), "stopped:upstream_error")

    def test_all_good_cases_have_no_failures(self):
        cases = [
            {"name": "good1", "data": good_data(), "should_succeed": True},
            {"name": "good2", "data": good_data(), "should_succeed": True},
        ]
        result = analyze(cases)
        self.assertEqual(result["failure_count"], 0)
        self.assertIsNone(result["top_priority"])

    def test_failures_are_attributed_to_correct_step(self):
        cases = [
            {"name": "good", "data": good_data(), "should_succeed": True},
            {"name": "bad1", "data": {"company": "X"}, "should_succeed": True},
            {"name": "bad2", "data": {"unit": "百万元"}, "should_succeed": True},
        ]
        result = analyze(cases)
        self.assertEqual(result["failure_count"], 2)
        # 两个失败都归因到 read_dataset
        self.assertEqual(result["freq_by_step"], {"read_dataset": 2})
        self.assertEqual(result["top_priority"]["step"], "read_dataset")
        self.assertEqual(result["top_priority"]["count"], 2)

    def test_expected_failure_is_not_counted(self):
        # should_succeed=False 的样本即使停下了，也不算错误
        cases = [
            {"name": "expected-stop", "data": {"company": "X"}, "should_succeed": False},
        ]
        result = analyze(cases)
        self.assertEqual(result["failure_count"], 0)

    def test_top_priority_picks_most_frequent_step(self):
        cases = [
            {"name": "bad1", "data": {"company": "X"}, "should_succeed": True},
            {"name": "bad2", "data": {"company": "X"}, "should_succeed": True},
            {"name": "good", "data": good_data(), "should_succeed": True},
        ]
        result = analyze(cases)
        self.assertEqual(result["top_priority"]["step"], "read_dataset")
        self.assertIn("补数据源", result["top_priority"]["fix_hint"])


if __name__ == "__main__":
    unittest.main()
