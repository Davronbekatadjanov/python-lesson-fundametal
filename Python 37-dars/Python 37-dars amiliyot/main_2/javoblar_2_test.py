import unittest
from javoblar_2 import get_text
class Birnichi_harf_katta(unittest.TestCase):
    def katta_harf(self):
        matn1 = ['salom']
        natija1 = get_text(matn1)
        kutilgan_natija1 = ['Salom']
        self.assertEqual(natija1,kutilgan_natija1)     
unittest.main()

