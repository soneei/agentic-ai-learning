import copy
import unittest

from baseline import run_baseline, RESEARCH_DATASET
from reflection import check_report


class ReflectionTests(unittest.TestCase):
    def test_clean_report_passes_all(self):
        r = check_report(run_baseline(), RESEARCH_DATASET)
        self.assertTrue(r["all_pass"])
        self.assertEqual(len(r["checks"]), 5)
        self.assertTrue(all(c["pass"] for c in r["checks"]))

    def _tampered_result(self, mutate):
        result = copy.deepcopy(run_baseline())
        mutate(result["result"]["summary"])
        return result

    def test_catches_wrong_number(self):
        def mutate(summary):
            # 把 40% 改成 90%——数字抄错
            summary["confirmed_changes"][0] = "revenue 2024：绝对变化 40，同比 90.0%"
        r = check_report(self._tampered_result(mutate), RESEARCH_DATASET)
        numbers = [c for c in r["checks"] if c["criterion"] == "数字正确"][0]
        self.assertFalse(numbers["pass"])

    def test_catches_buy_sell_advice(self):
        def mutate(summary):
            summary["confirmed_changes"].append("revenue 2025：值得投资，建议买入")
        r = check_report(self._tampered_result(mutate), RESEARCH_DATASET)
        boundary = [c for c in r["checks"] if c["criterion"] == "无越界建议"][0]
        self.assertFalse(boundary["pass"])

    def test_catches_speculative_wording(self):
        def mutate(summary):
            summary["confirmed_changes"].append("revenue 2026：预计将大幅增长")
        r = check_report(self._tampered_result(mutate), RESEARCH_DATASET)
        fact = [c for c in r["checks"] if c["criterion"] == "事实推测分开"][0]
        self.assertFalse(fact["pass"])

    def test_catches_untraceable_claim(self):
        def mutate(summary):
            summary["confirmed_changes"].append("公司前景良好：没有指标名和年份")
        r = check_report(self._tampered_result(mutate), RESEARCH_DATASET)
        trace = [c for c in r["checks"] if c["criterion"] == "结论可追溯"][0]
        self.assertFalse(trace["pass"])


if __name__ == "__main__":
    unittest.main()
