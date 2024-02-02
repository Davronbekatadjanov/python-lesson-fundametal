"""
Mavzu: sonlar  amaliyot
Sana: 08.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # Quyidagi dasturlarning har birini alohida faly ko'rinishida yozing va bajring:

# # 1.Foydalanuvchi kiritgan sonning kvadrati va kubini konsulga chiqarish.

# # 1.1-foydalanuvchi dan avval soni kiritishini so'raymiz.
# son = int(input("Iltimos raqamni yozing:>>"))
# # 1.2-foydalanuvchini kiritgan soning kvadratini hisoblaymiz
# kvadrat_s = son**2
# # 1.3-foydalanuvchi kiritgan soning kubini hisoblaymiz
# kub_s = son**3
# # 1.4-foydalanuvchi kiritgan soning kvadrati va kubini konsulga chiqaramiz
# print(f"{str(son)} ning kvadrati: {str(kvadrat_s)} va {str(son)} ning kubi: {str(kub_s)}")
# print(str(son) + " ning kvadrati:" + str(kvadrat_s) + " va " + str(son) + " ning kubi:" + str(kub_s))

# # 2.Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini  hisoblab,konsulga chiqaruvchi dastur.

# # 2.1-foydalanuvchining yoshini kiritishini so'raymiz:
# yosh = int(input("Iltimos yoshingizni kiriting:>>"))
# # 2.2-foydalanuvchining tug'ilgan yilini hisoblaymiz:
# t_yil = 2023-yosh
# # 2.3-foydalanuvchining tug'ilgan yilini konsulga chiqaramiz:
# print(f"Siz {t_yil} yil tug'ilgan ekansiz")
# print("Siz " + str(t_yil) +" yil tug'ilgan ekansiz")

# # 3.Foydalanuvchidan ikki son kiritishini so'rab,kiritilfan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

# # 3.1-foydalanuvchidan birinchi soni kiritishini so'raymiz:
# son_1 = int(input("Iltimos birinchi raqamni kirting:>>"))
# # 3.2-foydalanuvchidan ikkinchi soni kiritishini so'raymiz:
# son_2 = int(input("Iltimos ikkinchi raqamni kirting:>>"))
# # 3.3-foydalanuvchi kiritgan ikkita soning qo'shib,ayirib,ko'paytirib va bo'lib yangi o'zgaruvchilarga joylab chiqamiz
# son_q = son_1 + son_2
# son_a = son_1 - son_2
# son_k = son_1 * son_2
# son_b = son_1 / son_2

# print(f"Sonlarni yig'indisi:{son_q},\n ayirmasi:{son_a}, ko'paytmasi:{son_k},\n bo'linmasi:{son_b} ")

# # 1.foydalanuvchi kiritgan soning kvadrati va kubini konsulga chiqarish
# x = int(input("Istalgan soni kiriting:>>"))
# print(x ," ning kvadrati", x**2, " ga teng")
# print(x," ning kubi", x**3, " ga teng")

# # 3.foydalnuvchidan ikkita son kiritishini so'rab,kiritilgan sonlarning yig'indisi,ayirmasi,ko'paytmasi va bo'linmasini chiqaruvchi dastur
# a = float(input("Birinchi soni kiriting:"))
# b = float(input("Ikkinchi soni kiriting:"))
# print(f"{a}+{b}=", a+b)
# print(f"{a}-{b}=", a-b)
# print(f"{a}*{b}=", a*b)
# print(f"{a}/{b}=", a/b)
