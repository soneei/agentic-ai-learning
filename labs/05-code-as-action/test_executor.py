import unittest

from executor import execute_model_output


class CodeAsActionTests(unittest.TestCase):
    def test_executes_multi_step_plan(self):
        output = """<execute_python>
values = [3, 1, 2]
ordered = sorted(values)
answer = sum(ordered)
</execute_python>"""
        self.assertEqual(execute_model_output(output), {"status": "success", "result": 6})

    def test_refuses_missing_tags(self):
        result = execute_model_output("answer = 1")
        self.assertEqual(result["status"], "error")
        self.assertIn("execute_python", result["message"])

    def test_refuses_file_access(self):
        output = "<execute_python>\nanswer = open('secret.txt').read()\n</execute_python>"
        result = execute_model_output(output)
        self.assertEqual(result["status"], "error")
        self.assertIn("Forbidden name", result["message"])

    def test_returns_runtime_error(self):
        output = "<execute_python>\nanswer = missing_value\n</execute_python>"
        result = execute_model_output(output)
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["error_type"], "NameError")


if __name__ == "__main__":
    unittest.main()
