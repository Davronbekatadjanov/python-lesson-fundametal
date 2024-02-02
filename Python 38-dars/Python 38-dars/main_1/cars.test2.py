# setUp() metodi

# Yuqoridagi misolda bitta test davomida 2 ta obyekt
# yaratdik,obyektning parametrlarini qo'lda yangidan
# kiritdik.Agar shu yo'sinda davom etadigan bo'lsak,turli
# testlar uchun har gal yangi obyekt yaratishimiz va 
# ularning har biriga xususiyatlarni qayta-qayta kiritishimiz
# talab qilinadi.Buning oldini olish uchun test klassimizning 
# avvalida setUp() metodini yaratib,bu metod ichida 
# barcha kerakli qiymatlarni va obyektlarni saqlab qo'yishimiz,turli
# testlarda shu qiymatlarga murojaat etishimiz mumkin;

import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def setUp(self):
        make = 'GM'
        model = "Malibu"
        year = 2023
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make,model,year)
        self.avto2 = Car(make,model,year,price=self.price)
    def test_create(self):
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        self.assertIsNone(self.avto1.price)
        self.assertEqual(0,self.avto1.get_km())
        self.assertEqual(self.price,self.avto2.price)
unittest.main()


# E'tibor bering,setUp() metodi ichida ba'zi o'zagaruvchilar self
# yordamida berilgan(self.price,self.km,self.avto1,self.avto2).
# Bu o'zgaruvchilarga biz CarTest() klassining ichida istalgan joydan
# murojaat etishimiz mumkin.Shuning uchun ham 
# test_ceate() funksiyasi ichida yangi obyekt yaratmasdan,setUp() 
# ichidagi avto1 va avto2 obyektlariga murojaat etdik.


