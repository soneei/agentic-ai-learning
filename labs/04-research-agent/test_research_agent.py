import unittest

from research_agent import run_full_pipeline, format_full_report


class ResearchAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pipeline = run_full_pipeline()

    def test_all_three_blocks_present(self):
        self.assertIn("baseline", self.pipeline)
        self.assertIn("reflection", self.pipeline)
        self.assertIn("evaluation", self.pipeline)

    def test_baseline_completed(self):
        self.assertEqual(self.pipeline["baseline"]["status"], "completed")

    def test_reflection_passed_clean_report(self):
        self.assertTrue(self.pipeline["reflection"]["all_pass"])

    def test_evaluation_found_five_failures(self):
        self.assertEqual(self.pipeline["evaluation"]["failure_count"], 5)

    def test_report_contains_all_three_sections(self):
        text = format_full_report(self.pipeline)
        self.assertIn("第一部分：基线小结", text)
        self.assertIn("第二部分：Reflection 自检", text)
        self.assertIn("第三部分：Evaluation 失败归因", text)

    def test_report_has_summary_conclusion(self):
        text = format_full_report(self.pipeline)
        self.assertIn("报告自检", text)
        self.assertIn("read_dataset", text)


if __name__ == "__main__":
    unittest.main()
