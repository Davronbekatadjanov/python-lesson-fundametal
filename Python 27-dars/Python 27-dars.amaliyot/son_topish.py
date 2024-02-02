"""
Mavzu: "SON TOPISH" O'YINI
Sana:04.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# "Son topish" va "So'z topish"
# Ushbu bobda biz ikkita yangi o'yin ustida ishlaymi.Dasturni yaratish jarayonida avval o'rgangan bilimlarimizni amalda qo'llaymiz.Shuningdek,yangi loyiha boshlashda mumkin bo'lgan algoritm tushunchasi bilan tanishamiz.

# "Son topish" o'yini
# Birinchi dasturimiz sodda "Son topish" o'yini bo'ladi.Bu o'yin quyidagicha o'ynaladi:
# 1.Kompyuter biror berilgan oraliqda (masalan,1 dan 10 gacha) son "o'ylaydi"
# 2.Foydalanuvchi kompyuter o'ylagan sonni topishga urinadi va biror qiymat taxmin qilib kiritadi.
# 3.Agar taxmin to'g'ri bo'lsa,o'yin tugaydi,agar xato bo'lsa,kompyuter foydalanuvchi taxmin qilgan son o'ylagan sondan katta yoki kichikligini aytadi va yangi son taxmin qilishni so'raydi.
# 4.Dastur shu zaylda foydalanuvchi to'g'ri sonni topguniga qadar davom etadi.

# Algoritm

# Dasturlashning muhim qismi to'g'ri reja qilish va dasturni mayda qadamlarga bo'lib olishdir.Bu Algoritm deyiladi.Xuddi ovqat pishirishda retseptdan foydalangandek,dastur yozishda ham.Algoritmdan foydlanamiz.
# Yuqoridagi o'yin qoidasi ham bir nechta sodda qadamlarga bo'lib olamiz:
# 1.Kompyuter ma'lum oraliqda son "o'ylaydi":Albatta,kompyuter o'ylashga qodir emas,shuning uchun biz berilgan oraliqda biror tasodifiy sonni qaytarishimiz kifoya(random) .
# 2.Foydalanuvchi taxmin qilgan sonni qabul qilib olish (input()).
# 3.Taxmin va tasodifiy sonlarrni taqqoslash(==)
# 4.Taqqoslash natijasiga ko'ra (if-else):
# a. yo o'yinni to'xatish:
# b.yo foydalanuvchiga ishora berish va qayta taxmin qilishni so'rash va 3-4 qadamlarni takrorlash (while).
# Sodda alogritm tayyor,endi bevosita dastur yozishga kirishsak ham bo'ladi.

# import random

# def sontop(x=10):
#     print(f"1 dan {x} gacha son o'yladim.Topa olasizmi.")
#     toplangan_son = random.randint(1,x)
#     taxminlar = 0
#     while True :
#         taxminlar += 1
#         taxmin = int(input(">>> "))
#         if taxmin < toplangan_son:
#             print("Xato.Men o'ylagan son bundan kattaroq.Yana urinib ko'ring.")
#         elif taxmin > toplangan_son:
#             print("Xato.Men o'ylagan son bundan kichikroq.Yana urinib ko'ring.")
#         else:
#             break
#     print(f"Tabriklaymiz!.Siz {taxminlar} ta taxmin bilan topdingiz")
#     return taxminlar

# def sontop_pc(x=10):
#     input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman.")
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         if quyi != yuqori:
#             taxmin = random.randint(quyi,yuqori)
#         else:
#             taxmin = quyi
#         javob = input(f"Siz {taxmin} sonini o'yladingiz: tog'ri (t),"
#                       f"men o'ylagan son bundan kattaroq (+),yoki kichikroq (-)".lower())
#         if javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f"Men {taxminlar} ta taxmin bilan Topdim!")
#     return taxminlar

# def play(x=10):
#     yana = True
#     while yana:
#         taxminlar_user = sontop(x)
#         taxminlar_pc = sontop_pc(x)
#         if taxminlar_user>taxminlar_pc:
#             print(f"Sizda {taxminlar_user}ta taxmin bilan yutqazdingiz")
#         elif taxminlar_user<taxminlar_pc:
#             print(f"Men esa {taxminlar_pc} yutqazdim")
#         else:
#             print(f"Durang!.Ikkalamiz ham {taxminlar_user} ta taxmin bilan topdik")
#         yana = int(input("Yana o'ynaysiz? Ha(1)/Yo'q(0):"))

import random
def sontop(x=10):
    print(f"1 dan {x} gacha son o'yladim.Topa olsizmi?")
    tasodifiy_sonlar = random.randint(1,x)
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_sonlar:
            print("Xato,Men o'ylagan son bundan kattaroq,Yana urinib ko'ring")
        elif taxmin > tasodifiy_sonlar:
            print("Xato,Men o'ylagan son bundan kichroq,Yana urinib ko'ring")
        else:
            break
    print(f"Tabriklaymiz,Siz {taxminlar} ta urinshda topdingiz ")       
    return taxminlar
def sontoppc(x=10):
        input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman.")
        quyi = 1
        yuqori = x
        taxminlar = 0 
        while True: 
            taxminlar += 1 
            if quyi != yuqori:
                taxmin = random.randint(quyi,yuqori)
            else: 
                taxmin = quyi
            javob = input(f"Siz {taxmin} sonini o'yladingiz : tog'ri (t),"
                          f"men o'ylagan son bundan kattaroq (+),yoki kichikroq (-)".lower())           
            if javob == "-":
                yuqori = taxmin - 1
            elif javob == "+":
                quyi = taxmin + 1
            else:
               break
        print(f"men {taxminlar} ta urinish bilan topdim! ")
        return taxminlar
    
                
    