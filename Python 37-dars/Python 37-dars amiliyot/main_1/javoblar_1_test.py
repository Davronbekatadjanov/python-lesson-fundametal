

import unittest
from javoblar_1 import eng_katta

class Engkatta(unittest.TestCase):
    def test_eng_katta_son1(self):
        self.assertEqual(eng_katta(3,4,5),5)
    def test_eng_katta_son1_eng_katta_son2(self):
        self.assertEqual(eng_katta(54,55,99),99)
unittest.main()
