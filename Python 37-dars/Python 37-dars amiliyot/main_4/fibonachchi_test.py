import unittest
from fibonachchi import fibonachchi_ket_ketligida
class TestFibonachchi(unittest.TestCase):
    def test_fibonachchi(self):
        # test
        son1 = 8
        natija1 = fibonachchi_ket_ketligida(son1)
        self.assertTrue(natija1)
        # test 2
        son2 = 36
        natija2 = fibonachchi_ket_ketligida(son2)
        self.assertTrue(natija2)
unittest.main()

