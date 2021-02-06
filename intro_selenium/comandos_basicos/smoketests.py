from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from searchtests2 import SearchTests
from assertions import AssertionsTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)


smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": __file__
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)