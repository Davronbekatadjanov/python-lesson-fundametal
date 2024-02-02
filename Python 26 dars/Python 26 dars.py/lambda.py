"""
Mavzu: Funksiyalar So'ngso'z
Sana:04.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# Lambda yohud nomsiz funksiya

# Pythonning o'ziga xos xususiyatlaridan biri,nomsiz vaqtinchalik funksiyalar yaratish imkoniyati.
# Bunday funksiyalarni yaratishda def opertori o'rniga lambda operatori ishlatilgani uchun lambda funksiyalar deb ataladi.

# Nomsiz funksiyalar quyidagicha yaratiladi:
# lambda argument:ifoda

# Lambda funksiyalari istalgan miqdordagi argumentlarga ega bo'lishi mumkin,ammo funksiya badanida faqat bitta ifoda mavjud bo'ladi.
# Ifoda bajariladi va qaytariladi (return operatori shart emas.)
# Nomsiz funksiyalar biror ifodani tezda hisoblab olishda qulay.Misol uchun quyidagi lambda funksiya ikkita argument qabul qiladi(),va aylana uzunligini qaytaradi:

import math
uzunlik = lambda pi,r :2*pi*r
print(uzunlik(math.pi,10))

# Kodni tahlil qilamiz, 1-qatorda math modulini chaqirib oldik.2-qatorda lambda funksiyani yaratdik,funksiyamiz pi va r argumentlarini qabul qilib,2*pi*r qiymatni qaytaradi.Funksiyaga  bermadik,lekin unga uzunlik identifikatori olqali murojat qilishimiz mumkin.3-qatorda funksiyamizga murojat qildik va natijani konsolga chiqardik.

# Yana bir misol,topingchi quyidagi funksiyaning vazifasi nima?

"""Soni kvadratini aniqlovchi funksiya"""

product = lambda x,y : x **y
print(product(3,2))

# Shu yerda so'rashingiz mumkin,nima uchun lambda nomsiz deb ataladi,ahir unga hozirgina nomi bilan murojat qildikku?

# Gap shundaki,lambda funksiyalarning asl mohiyati boshqa funksiyalar bilan birga ishlaganda ko'rinadi.Keling,tushunarli bo'lishi uchun oddiyroq misol ko'ramiz.

# Quyidagi dasturda biz avval daraja degan funksiya yasadik,bu funskiyamiz n degan o'zgaruvchi qabul qilib oladi va funksiya ichidagi noma'lum x ning n-darajasini qaytaradi.Aslida daraja bu funksiya yasaydigan funksiya bo'ladi.Xo'sh,undan qanday foydalanamiz?4-5-qatorlarda esa daraja funksiyasidan yana 2 ta funksiya yasadik:

def daraja(n):
    return lambda x : x**n
kvadrat = daraja(2)
kub = daraja(3)
print(f"3 ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# Lambda funksiyalaridan argument sifatida boshqa funksyani qabul qiluvchi funksiyalar bilan ishlashda ham keyng foydalaniladi.Misol uchun map() va filter() funksiyalar