"""
Mavzu:Funksiyalarni tekshirish
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:2-qism

"""


import unittest
from circle import getArea , getPerimeter

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10),314.159)
        self.assertAlmostEqual(getArea(3),28.27431)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)

unittest.main()

# Bu safar har bir funksiya uchun ikkitadan test yozdik.
# Testni bajaramiz va quyidagi natijani olamiz:
    
