import unittest

import src
from src import parse

class TestPredicateParsing(unittest.TestCase):
    # TODO
    def test_CSC263_satisfied_by_courseload(self):
        # "CSC263H1 : CSC207H1, CSC236H1/CSC240H1; STA247H1/STA255H1/STA257H1"
        pass

    def test_CSC263_unsatisfied_by_courseload(self):
        pass

if __name__ == '__main__':
    unittest.main()
