import unittest

from orchestrator import run_loop


VALID_DATASET = {
    "company": "星河数据工具",
    "unit": "百万元",
    "years": [2023, 2024, 2025],
    "metrics": {"revenue": [100, 140, 196]},
}


class RunLoopTests(unittest.TestCase):
    def test_normal_data_runs_to_completion(self):
        result = run_loop(VALID_DATASET)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["reason"], "done")
        # 走完四个工具：read → calculate → check → summary
        self.assertEqual(len(result["trace"]), 4)
        self.assertIsNotNone(result["result"]["summary"])

    def test_trace_records_each_tool_in_order(self):
        result = run_loop(VALID_DATASET)
        tools = [step["tool"] for step in result["trace"]]
        self.assertEqual(
            tools,
            ["read_dataset", "calculate_changes", "check_data_quality", "generate_summary"],
        )

    def test_missing_field_stops_without_running_tools(self):
        result = run_loop({"company": "星河数据工具"})
        self.assertEqual(result["status"], "stopped")
        self.assertEqual(result["reason"], "upstream_error")
        # read_dataset 一报错就停，后面工具没跑
        self.assertEqual(len(result["trace"]), 1)

    def test_abnormal_data_stops_for_human_verification(self):
        dataset = dict(VALID_DATASET)
        dataset["metrics"] = {"revenue": [100, 300, 50]}  # 暴涨暴跌
        result = run_loop(dataset)
        self.assertEqual(result["status"], "stopped")
        self.assertEqual(result["reason"], "no_tool_for_next_step")
        # 停在 check_data_quality，没进 generate_summary
        self.assertEqual(result["result"]["status"], "warning")

    def test_max_steps_prevents_infinite_loop(self):
        result = run_loop(VALID_DATASET, max_steps=1)
        self.assertEqual(result["status"], "stopped")
        self.assertEqual(result["reason"], "max_steps_reached")


if __name__ == "__main__":
    unittest.main()
