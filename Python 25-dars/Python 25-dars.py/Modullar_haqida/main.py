"""
Mavzu: Modullar
Sana:07.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
# """
# # Modullar
# # Funksiyaning qulayliklaridan biri ko'p takrorlanadigan kodlarni funksiya ichida yashirishimiz va kerak bo'lganda funksiya nomi orqali murojaat etishimiz mumkinligida.Maqsadimiz dasturimizni ixcham va tushunarli qilib,kelajakda o'zimiz yoki boshqalar uchun ham "toza" kod qoldirishdir.
# # Bu yo'nalishda yana bir qadam qo'yib,dasturimizni modullarga ajaratishimiz mumkin.

# # Modul nima?

# # Modul loyihamiz ichidagi alohida fayl bo'lib,dasturimiz davomida ishlatiladigan funksiyalarni (va o'zgaruvchilarni) mana shu falyga joylab,ko'zdan yashirib qo'yishimiz mumkin.Bu bizga asosiy dastrumizda chalg'imasdan kod yozish imkoniyatini beradi.
# # Modul va uning ichidagi funksiyalarni istalgan payt asosiy dasturimizga yuklab olishimiz,modullarni boshqa dasturchilar bilan ulashishimiz yoki kelajakda o'zimizning boshqa loyihalarimizda foydalanishimiz mumkin.
# # Umuman olganda,katta dasturlar bir nechta o'nlab modullardan iborat bo'lishi tabiiy hol.

# # Modulni chaqirib olish

# # Modul ichidagi istalgan funksiyaga murojaat etish uchun import modul_nomi buyrug'idan foydalanmiz.Bunda modul ichidagi istalgan funksiyaga modul_nomi.funksiya_nomi() ko'rinishida murojaat etishimiz mumkin.Ya'ni avval modul nomi,keyin esa nuqta qo'yilib,modul ichidagi funksiya nomi yoziladi.
# # Keling, yuqoridagi modulimizdagi avto_info() va info_print() funksiyalariga murojaat etamiz.Buning uchun asosiy dasturimizni (main.py) quyidagicha yozamiz:

# import avto_info_mod # avto_info_mod modulini chaqiramiz:
# avto1 = avto_info_mod.avto_info("GM","Malibu","Qora","avtomat",2020,40000)
# avto_info_mod.info_print(avto1)

# # Ko'rib turganingizdek,dastrimiz qisqa,tushunali va muhimi toza bo'ldi.3 qator kod ortida 20 qatordan ortiq kodni yashirdik.
# # import modul_nomi komandasi bir martta,dastur boshida yoziladi.

# # Modulga qisqa nom berish

# # Yuqoridagi usul bilan modulni chaqirib olishda fayl nomi uzun bo'lsa bu o'ziga yarasha noqulayliklar tug'dirishi mumkin.
# # Buning oldini olish uchun esa,modulni chaqirganda unga as operatori yordamida qisqa nom berishimiz, va modulga qisqa nom orqali murojaat qilish mumkin.
# # Quyidagi misolda avto_info_mod ni qisqa qilib aim deb nomlab oldik,va 3-4-qatorlarda modulga murojat qilishda qisqa nomidan foydalandik.

# import avto_info_mod as aim # avto_info_mod ni qisqa nom aim bilan chaqiramiz
# avto1 = aim.avto_info("GM","Malibu","Qora","avtomat",2020,40000)
# aim.info_print(avto1)

# # Modulga qisqa nom berganigizda bunday nomli boshqa o'zgaruvchi yoki funksiya yo'qligiga amin boling.
# # Shuningdek,dastur davomida bu nomni boshqa o'zgaruvchilarga yoki funksiyalarga berib yubormang.

# # Modul ichidan ma'lum funksiyalarni ko'chirib olish

# # Agar katta modullardan faqatgina ba'zi funksiyalarga murojat qilish talab qilinsa,kerakli funksiyalarni from modul_nomi import funksiya1,funksiya2 komandasi yordamida o'zimizning
# # dasturimizga ko'chirib olishimiz mumkin.Bu usulning qulayligi,endi funksiyalarga to'g'ridan-to'g'ri murojat qilish mumkin(modul ismini yozmagan holda.)
# # Misol uchun avvalgi kodimizda biz faqatgina avto_info va info_print funksiyalaridan foydalanadik
# # shu funksiyalarni asosiy kodimizga ko'chirib olaylik:

# # from avto_info_mod import avto_info, info_print
# # avto1 = avto_info("GM","Malibu","Qora","avtomat",2020,40000)
# # info_print(avto1)

# # Funksiyalarga qisqa nom berish

# # Huddi avvalgidek,ko'chirib olgan funksiyamizga ham qisqa nom berishimiz mumkin.
# from avto_info_mod import avto_info as ainfo, info_print as iprint
# avto1 = ainfo("GM","Malibu","Qora","avtomat",2020,40000)
# iprint(avto1)

# Modul ichidagi barcha funksiyalarni ko'chirb olish

# Modul ichidagi barcha funksiyalarni asosiy dasturga ko'chirib olish uchun from modul_nomi import * komdasidan foydalanmiz.
from avto_info_mod import *
avto1 = avto_info("GM","Malibu","Qora","avtomat",2020,40000)
info_print(avto1)

# Diqqat! Bir nechta sabablarga ko'ra bu usuldan foydalanish tavsiya qilinmaydi.
# Katta modullarda yuzlab funksiyalar bo'lishi mumkin, va funksiya nomi sizning dasturingizdagi boshqa funksiya yoki o'zgaruvchi bilan bir hil nomga ega bo'lsa,dastur xato ishlashiga olib keladi.

# Modulda o'zgaruvchi saqlash
# Modullarning ichida nafaqat funksiyalar, balki turli o'zgaruvchilarni ham saqlash mumkin. Modul ichidagi o'zgaruvchilarga ham huddi yuqoridagi usullar bilan murojat qilish mumkin.

# PYTHON MODULLARI
# Python dasturlash tili tayyor modullar bilan keladi, modullarning to'liq ro'yxatini quyidagi bo'glama orqali kirib ko'rishingiz mumkin:
# https://docs.python.org/3/py-modindex.html

# Keling ulardan ba'zilari bilan tanishamiz.
