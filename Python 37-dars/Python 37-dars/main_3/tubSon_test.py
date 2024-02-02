"""
Mavzu:Funksiyalarni tekshirish
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:3-qism

"""

import unittest

from tubSonmi import tubSonmi
class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(19))
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(98))
        self.assertFalse(tubSonmi(512))
unittest.main()

# Test davomida tubSonmi() funksiyasini bir nechta
# tub(7,193,19) va tub bo'lmagan(6,98,512) sonlar bilan
# chaqirdik.Bunda assertTrue() metodi funksiyamiz haqiqatan
# ham True qiymatini qaytarishini,assertFalse() metodi esa 
# funksiyamiz False qiymat qaytarishin tekshiradi.

