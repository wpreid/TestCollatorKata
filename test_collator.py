import unittest
from typing import List, Literal

TestStatus = Literal["Pass","Fail","Disable","Abort","Unrun"]


class TestResult:
    def __init__(self):
        self.name = None

    pass


class TestCollator:
    def __init__(self):
        self.result_list = []

    def endrun(self) -> List[TestResult]:
        return self.result_list

    def add(self, name: str, status: TestStatus):
        new_result = TestResult()
        self.result_list.append(new_result)


class CollatorTest(unittest.TestCase):
    def test_endrun_with_no_tests_returns_empty(self):
        collator: TestCollator = TestCollator()
        self.assertSequenceEqual([], collator.endrun())

    def test_endrun_with_one_run_of_one_test(self):
        collator: TestCollator = TestCollator()
        collator.add("only test", "Pass")
        [result] = collator.endrun()
        # assert name matches
        self.assertEqual(result.name,"only test")
        # assert status matches
        # assesrt isNew is true



if __name__ == '__main__':
    unittest.main()
