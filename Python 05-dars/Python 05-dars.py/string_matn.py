"""
Mavzu: String-matn
Sana:07.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# viloyat = 'Samarqand'
# avto = 'Nexia 3'

# matn = "Men yangi telefon oldim"
# print(matn)

# # Stringlar ustida amallar

# # Matnlarni qo'shish uchun + operatoridan foydalanamiz.
# ism = 'Ahmad'
# print("Maning ismim " + ism)

# # Yana bir misol o'zgaruvchilarni qo'shish orqali.
# ism =  'Ahmad'
# familiya = 'Qayum'
# print(ism + familiya)

# # Yuqoridagi misolga o'xshab so'zlar bir biriga yopishish qolmasliki uchun ikki o'zgaruvchi orasiga bo'sh joy qo'shib yozamiz,masalan:
# ism = 'Ahmad'
# familiya = 'Qayum'
# print(ism + ' ' + familiya)

# # f-string haqida.

# ism = 'Ahmad'
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# # f-string ichidagi o'zgaruvchilar katta qavslar ichida yoziladi.

# # Bu usul yordamida uzun matnlarni ham yasash mumkin:

# fname = "James"
# lname = 'Bond'
# matn = f"Salom,mening ismim {lname}. {fname} {lname}!"
# print(matn)

# # f-string yordamida nafaqat matnlarni,balki turli ifodalarni ham jamlab yozishingiz mumkin.

# tyil = 2002
# print(f"Siz {tyil}-yilda tug'ilgansiz.")
# print(f"Yoshingiz {2021-tyil} da")

# # Maxsus belgilar

# print('Hello World!')
# print('Hello \tWorld!') # \t bo'sh joy qo'shish
# print('Hello \nWorld!') # \n qator tashlash

# # upper() va lower() metodlari.
# # upper() metodi matndagi har bir harfni bosh harifga o'zgartiradi.
# ism = 'anvar'
# familiya = 'narzullayev'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())

# # lower() metodi  har bir harfni kichik harifga o'zgartiradi.
# ism = 'anvar'
# familiya = 'narzullayev'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.lower())

# # title() va capitalize() metodlari.

# # title() metodi matndagi har bir so'zning birinchi harfini bosh harf bilan yozadi.
# ism = 'anvar'
# familiya = 'narzullayev'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.title())

# # capitalizd() esa matndagi birinchi so'ning birinchi harfini katta bilan yozadi.
# ism = 'anvar'
# familiya = 'narzullayev'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.capitalize())

# # strip(),rstrip() va lstrip() metodlari.
# # Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.

# meva = "    olma    "
# print("Meva " + meva.lstrip() + " yaxshi ko'raman") # lstrip() matn boshidagi bo'shliqni olib tashlaydi.

# meva = "    olma    "
# print("Meva " + meva.rstrip() + " yaxshi ko'raman") # rstrip() matn oxiridagi bo'shliqni olib tashlaydi.

# meva = "    olma    "
# print("Meva " + meva.strip() + " yaxshi ko'raman") # strip() matn boshi va oxiridagi bo'shliqni olib tashlaydi.

# # Yuqoridagi metolar o'zgaruvchi ichidagi asl matnni o'zgartirmaydi! O'zgartirilgan matnni saqlab qolish uchun uni qaytadan o'zgaruvchiga yuklasj lozim: meva = "    olma    "

# # meva = "    olma    "
# # print("Men " + meva + " yaxshi ko'raman" )

# # meva = "    olma    "
# # meva = meva.strip()
# # print("Men " + meva + " yaxshi ko'rman")

# # input() -Foydalanuvchi bilan muloqot
# # input metodi sizdan malumotni qabul qilib,keyin sizdagi malumotni konsulga qicharadi.
# ism = input("Ismingiz nima?")
# print("Assalom alaykum, " + ism)

# # Yuqoridagi kodni va uning natijasini chiroyliroq ko'rinishga keltiramiz.Keyin esa title() metodidan foydalanamiz va bu safar f-string usulidan foydalanamiz.

# ism = input("Ismingiz nima?\n>>>")
# print(f"Assalom alaykum,{ism.title()}")
# da