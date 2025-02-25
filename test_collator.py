import unittest
from typing import List


class TestResult:
    pass


class TestCollator:
    def endrun(self) -> List[TestResult]:
        return []


class CollatorTest(unittest.TestCase):
    def test_endrun_with_no_tests_returns_empty(self):
        result: List[TestResult] = TestCollator().endrun()
        self.assertSequenceEqual([], result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
