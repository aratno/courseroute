import unittest

import src
from src import parse

class TestPredicateParsing(unittest.TestCase):
    def test_ambiguous_selection(self):
        self.assertTrue(parse.is_desc_complex('Any half-course on computing'))
        self.assertTrue(parse.is_desc_complex('Any CSC half-course'))
        self.assertTrue(parse.is_desc_complex('Five CSC half-courses at the 200-level or higher'))

    def test_english_desc(self):
        self.assertTrue(parse.is_desc_complex('CSC108H1/(equivalent programming experience)'))
        self.assertTrue(parse.is_desc_complex('60% or higher in CSC148H1/CSC150H1'))
        self.assertTrue(parse.is_desc_complex('60% or higher in CSC148H1/CSC150H1, 60% or higher in CSC165H1'))
        self.assertTrue(parse.is_desc_complex('60% or higher in CSC148H1/CSC150H1, 60% or higher in CSC165H1/CSC240H1'))
        self.assertTrue(parse.is_desc_complex('CSC240H1 or an A- in CSC236H1'))
        self.assertTrue(parse.is_desc_complex('CSC209H1/(CSC207H1, proficiency in C or C++); MAT221H1/MAT223H1/MAT240H1, (MAT136H1 with a minimum mark of 77)/(MAT137Y1 with a minimum mark of 73)/(MAT157Y1 with a minimum mark of 67)/MAT235Y1/MAT237Y1/MAT257Y1'))
        self.assertTrue(parse.is_desc_complex('(MAT136H1 with a minimum mark of 77)/(MAT137Y1 with a minimum mark of 73)/(MAT157Y1 with a minimum mark of 67)/MAT235Y1/MAT237Y1/MAT257Y1, MAT221H1/MAT223H1/MAT240H1; STA247H1/STA255H1/STA257H1'))
        self.assertTrue(parse.is_desc_complex('CSC258H1; CSC209H1/proficiency in C'))
        self.assertTrue(parse.is_desc_complex('CSC318H1; STA247H1/STA255H1/STA257H1,(STA248H1/STA250H1/STA261H1)/(PSY201H1, PSY202H1)/(SOC202H1, SOC300H1); CSC209H1/proficiency C++ or Java'))
        self.assertTrue(parse.is_desc_complex('CSC351H1/(CSC336H1 (75%))/equivalent mathematical background; MAT237Y1/MAT257Y1; APM346H1/APM351Y1/(MAT244H1/MAT267H1 and exposure to PDEs)'))

    def test_engineering_prereqs(self):
        self.assertTrue(parse.is_desc_complex('CSC165H1/CSC240H1/(MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1; CSC207H1.\n  Prerequisite for Engineering students only: ECE345H1/CSC190H1/CSC192H1'))
        self.assertTrue(parse.is_desc_complex('CSC165H1/CSC240H1/(MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1; CSC207H1.\n Prerequisite for Engineering students only: ECE345H1/CSC190H1/CSC192H1'))
        self.assertTrue(parse.is_desc_complex('CSC336H1/CSC350H1/CSC351H1/CSC363H1/CSC365H1/CSC373H1/CSC375H1/CSC463H1, (MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1, CSC209H1/proficiency in C or C++;\n &nbsp;Prerequisite for Engineering students only:  ECE345H1 or ECE352H1'))

    def test_simple(self):
        self.assertFalse(parse.is_desc_complex('CSC207H1'))
        self.assertFalse(parse.is_desc_complex('CSC207H1, CSC236H1/CSC240H1; STA247H1/STA255H1/STA257H1'))
        self.assertFalse(parse.is_desc_complex('CSC209H1, CSC263H1/CSC265H1'))
        self.assertFalse(parse.is_desc_complex('CSC301H1'))
        self.assertFalse(parse.is_desc_complex('STA247H1/STA255H1/STA257H1/PSY201H1/ECO227Y1, (MAT135H1, MAT136H1)/MAT137Y1/MAT157Y1'))
        self.assertFalse(parse.is_desc_complex('CSC209H1'))
        self.assertFalse(parse.is_desc_complex('CSC263H1/CSC265H1'))
        self.assertFalse(parse.is_desc_complex('CSC148H1/CSC150H1; MAT133Y1(70%)/(MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1, MAT221H1/MAT223H1/MAT240H1'))
        self.assertFalse(parse.is_desc_complex('CSC209H1, CSC258H1, CSC263H1/CSC265H1, STA247H1/STA255H1/STA257H1/ECO227Y1'))
        self.assertFalse(parse.is_desc_complex('CSC209H1, CSC258H1'))
        self.assertFalse(parse.is_desc_complex('CSC263H1/CSC265H1'))
        self.assertFalse(parse.is_desc_complex('CSC263H1/CSC265H1, STA247H1/STA255H1/STA257H1'))
        self.assertFalse(parse.is_desc_complex('CSC207H1/CSC209H1; STA247H1/STA255H1/STA257H1'))
        self.assertFalse(parse.is_desc_complex('CSC301H1/CSC318H1/CSC384H1/CSC418H1'))
        self.assertFalse(parse.is_desc_complex('CSC207H1, CSC236H1/CSC240H1'))
        self.assertFalse(parse.is_desc_complex('CSC263H1/CSC265H1, MAT(135H1,136H1)/MAT137Y1/MAT137Y1/MAT157Y1, STA247H1/STA255H1/STA257H1'))
        self.assertFalse(parse.is_desc_complex('CSC411H1'))
        self.assertFalse(parse.is_desc_complex('CSC263H1/CSC265H1, (MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1, MAT221H1/MAT223H1/MAT240H1'))
        self.assertFalse(parse.is_desc_complex('CSC336H1/CSC350H1'))
        self.assertFalse(parse.is_desc_complex('(CSC363H1/CSC463H1)/CSC365H1/CSC373H1/CSC375H1/MAT247H1'))
        self.assertFalse(parse.is_desc_complex('CSC343H1, CSC369H1, CSC373H1/CSC375H1'))
        self.assertFalse(parse.is_desc_complex('CSC236H1/CSC240H1'))
        self.assertFalse(parse.is_desc_complex('CSC209H1, CSC258H1, CSC263H1/CSC265H1, STA247H1/STA255H1/STA257H1/ECO227Y1'))
        self.assertFalse(parse.is_desc_complex('CSC236H1/CSC240H1'))
        self.assertFalse(parse.is_desc_complex('CSC236H1/CSC240H1/MAT309H1')) 

    '''
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    '''

if __name__ == '__main__':
    unittest.main()
