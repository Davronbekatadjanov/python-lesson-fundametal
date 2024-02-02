"""
Mavzu:Funksiyalarni tekshirish
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:2-qism

"""

import unittest 
from name import get_full_name
class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('alijon', 'valiyev')
        self.assertEqual(formatted_name, 'Alijon Valiyev')
unittest.main()


# Dasturni tahlil qilamiz:

# Dastavval unittest modulini chaqiramiz 
# (import unittest)

# Keyingi qatorda name.py modulimizdan tekshirmoqchi
# bo'lgan funksiyamizni ham yuklab olamiz 
# (get_full_name).

# 4-qatorda test klassini yaratamiz, bu klassunittest.
# TestCase klassidan meros oladi. Bu klass berilgan 
# parametrlar uchun funksiyadan qaytgan qiymatlarni 
# tekshirishga mo'ljallangan. Klassimizga o'zimiz 
# istagan, tushunarli nom beramiz (NameTest). 

# Klassimiz ichida test_toliq_ism metodini yaratdik. 
# Bu metod get_full_name funksiyasidan qaytgan 
# qiymatni biz avvaldan bergan qiymatga teng yoki 
# yo'q ekanini tekshiradi. Buning uchun esa maxsus 
# .assertEqual() metodidan foydalandik. 

# E'tibor bering, test medotlarning nomi har doim 
# test so'zi bilan boshlanishi kerak.

# assertEqual() metodi ikki qiymat qabul qiladi 
# va ularning teng ekanligini tekshiradi (assert 
# ingliz tilidan tasdiqlash deb tarjima qilinadi). 
# Agar get_full_name('alijon','valiyev') funksiyamiz 
# to'g'ri ishlasa, funksiyadan 'Alijon Valiyev' 
# qiymati qaytishi kerak. assertEqual() metodi 
# aynan shuni tekshirishga mo'ljallangan.

# So'nggi qatorda unittest klassinini chaqiramiz, 
# bu esa o'z navbatida biz yuqorida yozgan testni 
# chaqiradi. 

# name_test.py dasturimizni bajaramiz va quyidagi 
# natijani olamiz

# Ran 1 test in 0.001s
# OK

# Natijadan bitta test bajarilganini va va bu test 
# muvaffaqiyatli o'tganini (OK) ko'rishimiz mumkin.
# Keling endi dars boshida yaratilgan get_full_name 
# funksiyamizga o'zgartirish kiritamiz:

# Bu safar funksiyamiz otasining ismini ham qabul 
# qiladi, lekin bu argument ixtiyoriy. 
# Testimizga ham o'zgartirish kiritamiz. Bu safar 
# ikki hil ism uchun ikkita alohida test bajaramiz:
    
import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('alijon','valiyev')
        self.assertEqual(formatted_name,'Alijon Valiyev')
    def test_toliq_ism_otasi(self):
        name = get_full_name('hasan','husanov','olimovich')
        self.assertEqual(name,'Hasan Olimovich Husanov' )
        
unittest.main()


# Test bajaramiz va quyidagi natijani olamiz:
# AssertionError: 'hasan olimovich husanov' != 'Hasan Olimovich Husanov'
# - hasan olimovich husanov
# ? ^     ^         ^
# + Hasan Olimovich Husanov
# ? ^     ^         ^


# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (failures=1)


# Bu safar funksiyamiz 1 ta testdan yiqildi 
# (failures=1). Biz kutgan natija (Hasan Olimovich 
# Husanov) va funksiya qaytargan natija 
# (hasan olimovich husanov) bir hil emas. 
# Ya'ni, ism familiya va otasining ismi katta 
# harflar bilan yozlishi kerak edi, lekin natija 
# unday emas. Demak funksiyamizda xato bor. 
# Xatoni to'g'rilaymiz:
    
# Bu safar funksiyamiz ikki testdan ham muvaffaqiyatli
# o'tdi.

