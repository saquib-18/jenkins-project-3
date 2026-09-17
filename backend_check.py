# backend_check.py

import time
import unittest

from app import calculate_result


print("======================================")
print("       BACKEND MODULE CHECK")
print("======================================")

print("Checking examination evaluation logic...")

time.sleep(3)


class EvaluationTests(unittest.TestCase):

    def test_85_marks(self):
        percentage, result = calculate_result(85, 100)

        self.assertEqual(percentage, 85)
        self.assertEqual(result, "PASS")

    def test_40_marks(self):
        percentage, result = calculate_result(40, 100)

        self.assertEqual(percentage, 40)
        self.assertEqual(result, "PASS")

    def test_30_marks(self):
        percentage, result = calculate_result(30, 100)

        self.assertEqual(percentage, 30)
        self.assertEqual(result, "FAIL")

    def test_zero_marks(self):
        percentage, result = calculate_result(0, 100)

        self.assertEqual(percentage, 0)
        self.assertEqual(result, "FAIL")

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            calculate_result(110, 100)


print("\nRunning evaluation tests...\n")

test_result = unittest.TextTestRunner(
    verbosity=2
).run(
    unittest.defaultTestLoader.loadTestsFromTestCase(
        EvaluationTests
    )
)

print("\n======================================")

if test_result.wasSuccessful():
    print("Backend checks passed.")
else:
    print("Backend checks failed.")
    raise SystemExit(1)

print("======================================")
