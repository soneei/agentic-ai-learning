import unittest

from baseline import run_baseline, format_summary, RESEARCH_DATASET


class BaselineTests(unittest.TestCase):
    def test_baseline_runs_to_completion(self):
        result = run_baseline()
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["reason"], "done")

    def test_all_four_tools_ran_in_order(self):
        result = run_baseline()
        tools = [s["tool"] for s in result["trace"]]
        self.assertEqual(tools, [
            "read_dataset", "calculate_changes", "check_data_quality", "generate_summary",
        ])

    def test_summary_has_confirmed_changes(self):
        result = run_baseline()
        summary = result["result"]["summary"]
        # 3 个指标 × 2 个年度变化 = 6 条
        self.assertEqual(len(summary["confirmed_changes"]), 6)

    def test_summary_respects_boundaries(self):
        result = run_baseline()
        summary = result["result"]["summary"]
        self.assertTrue(summary["data_limitations"])
        text = " ".join(summary["data_limitations"])
        self.assertIn("不给买卖建议", text)

    def test_format_summary_reads_nested_result(self):
        # 回归测试：summary 嵌在 result["result"] 里，不是最外层
        result = run_baseline()
        text = format_summary(result)
        self.assertIn("星河数据工具", text)
        self.assertIn("确认的变化", text)


if __name__ == "__main__":
    unittest.main()
