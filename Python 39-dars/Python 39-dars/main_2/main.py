"""
Mavzu:Kutubxonalar
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:2-qism

"""

# RegEx - Andoza yordamida matn izlash

# Pythondagi juda foydali modullardan biri re(
# regular expressions) modulidir.Bu modul yordamida,
# biror matn berilgan anodozaga tushish-tushmasligini
# tekshiramiz.Yoki berilgan anodoza asosida matnlar orasidan
# kerakli matnlarni ajratib olish mumkin.

# Keling,boshlanishiga sodda misol keltiramiz.Quyida biz
# 3 ta so'z va so'zlarni tekshirish andoza yaratdik.
# Quyidagi andozamiz t harfidan boshlanuvchi (^t),p harfi bilan 
# tugovchi(p$),5 harfdan iborat so'zlarni qidiradi(^t...p$).

# Avvaliga andozalarni tushunish biroz qiyin bo'lishi mumkin.
# lekin vaqt o'tishi bilan andoza qanday ishlashini tushunib 
# olasiz deb umid qilamiz.

# So'zlarni andozaga solishtirish uchun re.match() funksiyasidan
# foydalanamiz.Agar tekshirgan so'zimiz andozaga mos tushsa,
# re.match() metodi so'zning o'zini qaytaradi,aks holda,None 
# None qiymatini qaytaradi.


import re 
word1 = "темур"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р"
print(re.match(andoza,word1))
print(re.match(andoza,word2))
print(re.match(andoza,word3))

# Natijadan ko'rishimiz mumkinki,word1 va word2 o'zgaruvchilari 
# andozaga tushdi,word3 esa tushmadi.

# Andozlar biror matnda biz uchun kerakli ma'lumolarni
# ajratib olish uchun juda qulay.Masalan,Telegram oraqli
# yuborilgan xabardan e-mail manzilini yoki telefon raqamini
# ajratib olish uchun maxsus andoza yozishimiz mumkin.
# ihateregex.io sahifasidan esa loyihangiz uchun tayyor
# andozalarni topishingiz mumkin.

# rasmdagi ihateregax.io sahifasida e-email uchun andoza.


# Keling,yuqoridagi andoza asosida biror matndan e-mail
# manzilini ajaratib olamiz.Buning uchu re.findall() funksiyasidan
# foydalanamiz.

matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)

# Andoza yordamida foydalanuvchi kiritgan qiymatlarning
# ham ma'lum shartalarga javob berishini tekshirib olishimiz 
# mumkin:

# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'    
msg = "Yangi parol kiriting"
msg += '(kamida: 8 xona,1 ta lotin bosh va 1 ta kichik, '
msg += "1 ta son va 1 ta maxsus belgi bo'lishi kerak): " 
while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
    else:
        print("Maxfiy so'z talabga javob bermadi")
        

# Python kutubxonasi yuzlab foydali modullardan iborat.
# Biz ulardan ba'zilari bilan tanishdik,xolos 

