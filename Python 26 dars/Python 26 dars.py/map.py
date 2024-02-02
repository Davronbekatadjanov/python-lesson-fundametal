"""
Mavzu: Funksiyalar So'ngso'z
Sana:04.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # map() funksiyasi

# # Bu funksiya argument sifatida ro'yxat(yoki lug'at ) va boshqa bir funksiyani qabul qilib,ro'yxat elementlariga qabul qilingan funksiya yordamida ishlov beradi.Tushunarli bo'lish uchun quyidagi misolni ko'ramiz:

# from math import sqrt
# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))

# # Yuqoridagi misolda 0 dan 10 gacha sonlar ro'yxatini tuzib oldik,keyin esa map funksiyasiga ro'yxat va sqrt funksiyasini uztib,ro'yxatdagi barcha sonlarning ildizini hisoblab oldi.

# # map() funksiyasi map obyekt qaytargani sababli,qaytgan obyektni ro'yxatga o'tkazib olish uchun list() funksiyasidan foydalandik.

# # Yana bir misol ko'ramiz:

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz.

# # Yuqoridagi misolda biz avval berilgan sonning kvadratini hisoblochi funksiya yaratib oldik,undan keyine esa map yordamida sonlar ro'yxatidagi elementlarning kvadratini ham hisoblab oldik.


# # Endi keling huddi shu misolni lambda yordamida yozami:

# kvadratlar = list(map(lambda x:x*x,sonlar))
# print(kvadratlar)

# # Yuqoridagi misolda,endi daraja degan funksiyani yaratib o'tirmasdan,to'g'ridan-to'g'ri map() ni ichiga darajani hisoblovchi lambda funksiya uzatdik.

# # map() funksiyasi bo'lmaganida biz bunday dasturlarni for yodamida yozishimiz kerak bo'lar edi:
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)

# # map() funksiyasiga bir nechta ro'yatlar ham uzatish mumkin:

# a = [4,5,6]
# b = [7,8,9]
# a_plus_b = list(map (lambda x,y : x+y,a,b))
# print(a_plus_b)

# map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi:
ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))