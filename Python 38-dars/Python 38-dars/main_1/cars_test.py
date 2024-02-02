# Xususiyatlarni tekshirish

# Klassdan obyekt yaratish jarayonida biz obyektning 
# xususiyatlarini parametr ko'rinishida beramiz.Quyidagi 
# testda aynan shu jarayon to'g'ri kechganini tekshiramiz:
    
    
import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def test_create(self):
       # avto1 obyektini km va narxini bermasdan yartamiz
        avto1 = Car('toyota','camry',2023)
       # assertTestNotNone() qiymat mavjudligini tekshirish
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)
       # assertIsNone qiymat mavjud emasligini tekshiradi
        self.assertIsNone(avto1.price)
       # assertEquals qiymatlar tengligini tekshiradi
        self.assertEqual(0,avto1.get_km())
        # yangi obyekt yaratamiz va narxini ham ko'rsatamiz
        avto2 = Car("toyota","camry",2023,price=75000)
        self.assertEqual(75000,avto2.price)
        
unittest.main()
        

# Testimizni tahlil qilamiz:
    
# Dastavval obeyktimiz to'g'ri yaratilayotganini tekshirish
# uchun avto1 obyektini 3 ta parametr bilan yaratib oldik.
# (make,model,year) va bu xususiyatlar obyekt xususiyatlariga 
# yozilganini assertIsNotNone() metodi bilan tekshirdik.

# avto1 obyektini yaratishda uning narxini ko'rsatmadik,demak,
# bu xususiyat standart qiymatga (None) teng bo'lishi kerak
# Buni tekshirish uchun esa assertIsNone() metodiga murojaat etdik.

# Nihoyat,avtomobil kilometraji 0 ga teng ekanligin assertEquals()
# metodi yordamida test qildik.

# Test so'ngida biz yana bir obyekt yaratdik(avto2) va bu safar
# avtomobil narxini ko'rsatganimiz uchun assertEquals() metodi
# yordamida bu qiymat to'g'ri saqlanganini tekshirib oldik.
# Testni bajaramiz va quyidagi natijani olamiz:

#     Ran 1 test in 0.001s

# OK


