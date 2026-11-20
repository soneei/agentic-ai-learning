import unittest

from executor import Scenario, choose_path


class BranchDecisionTests(unittest.TestCase):
    def test_missing_data_fetches_from_source(self):
        result = choose_path(Scenario("missing", ["revenue"], True, False, False))
        self.assertEqual(result["next_step"], "fetch_from_source")

    def test_ambiguous_definition_asks_for_clarification(self):
        result = choose_path(Scenario("ambiguous", [], False, True, False))
        self.assertEqual(result["next_step"], "ask_for_clarification")

    def test_abnormal_result_enters_verification(self):
        result = choose_path(Scenario("abnormal", [], False, False, True))
        self.assertEqual(result["next_step"], "verify_source_and_calculation")

    def test_missing_from_source_stops_without_guessing(self):
        result = choose_path(Scenario("unavailable", ["debt"], False, False, False))
        self.assertEqual(result["next_step"], "stop_without_guessing")

    def test_normal_data_continues_analysis(self):
        result = choose_path(Scenario("normal", [], False, False, False))
        self.assertEqual(result["next_step"], "generate_hypotheses")


if __name__ == "__main__":
    unittest.main()
