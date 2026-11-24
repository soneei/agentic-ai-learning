import unittest

from failure_report import build_cases, generate_report
from error_analyzer import analyze


class FailureReportTests(unittest.TestCase):
    def test_all_injected_failures_are_caught(self):
        cases = build_cases()
        clean = [{k: v for k, v in c.items() if k != "fault"} for c in cases]
        result = analyze(clean)
        # 7 个样本里故意注入 5 个错（3 缺字段 + 2 异常数据）
        self.assertEqual(result["failure_count"], 5)
        self.assertEqual(result["total_cases"], 7)

    def test_attribution_distribution(self):
        cases = build_cases()
        clean = [{k: v for k, v in c.items() if k != "fault"} for c in cases]
        result = analyze(clean)
        self.assertEqual(result["freq_by_step"], {
            "read_dataset": 3,
            "check_data_quality": 2,
        })

    def test_top_priority_is_read_dataset(self):
        cases = build_cases()
        clean = [{k: v for k, v in c.items() if k != "fault"} for c in cases]
        result = analyze(clean)
        self.assertEqual(result["top_priority"]["step"], "read_dataset")

    def test_good_cases_not_flagged(self):
        cases = build_cases()
        clean = [{k: v for k, v in c.items() if k != "fault"} for c in cases]
        result = analyze(clean)
        bad_names = {f["name"] for f in result["failures"]}
        self.assertNotIn("正常样本 A", bad_names)
        self.assertNotIn("正常样本 B", bad_names)

    def test_report_is_nonempty(self):
        text = generate_report()
        self.assertIn("优先修", text)
        self.assertIn("read_dataset", text)


if __name__ == "__main__":
    unittest.main()
