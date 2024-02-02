"""
Mavzu:while,Ro'yxatlar va lug'atlar
Sana:27.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # while,Ro'xyatlar va lug'atlar
# # Ro'yxatlar (lug'atlar) bilan ishlashda while siklining foydalari juda ko'p.
# # Misol uchun, foydalanuvchidan bir nechta ma'lumotlarni qabul qilib olish,
# # ro'yxatdan takrorlanuvchi qiymatlarni o'chirib tashlash yoki bir ro'yxatni 
# # ikkinchi ro'yxatga ko'chirishda while siklidan foydalanish mumkin.

# # while yordamida ro'yxatni to'ldirish
# # Quyidagi dasturga e'tibor bering,avval ismlar degan bo'sh ro'yxat yaratib oldik.
# # Keyin esa while sikli yordamida foydalanuvchidan ro'yxatga ism qo'shishni so'rayapmiz.
# # So'ngra foydalanuvchidan yana ism qo'shmoqchi yoki yo'q ekanini so'raymiz va 
# # foydalanuvchining javobiga ko'ra yo sikl boshiga qaytamiz,yo siklni to'xtatamiz.

# ismlar = []
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True :    
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q):")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi")

# # Ro'yxat tarkibini ko'ramiz:
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
    
# # while yordamida lug'atni to'ldirish 
# # Yuqoridagi usul bilan while sikli yordamida lug'atlarni ham shakllantirishimiz mumkin.
# # Quyidagi kodda ism bu kalit, yosh esa kalitga mos keluvchi qiymat.while siklining 
# # davomiyligi esa ishoraning qiymatiga bog'liq.

# print("Do'stlaringiz yoshini saqlaymiz")
# dostlar = {}
# ishora = True 
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")    
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q):")
#     if javob == "yo'q":
#         ishora = False
        
# # Lug'atdagi qiymatlarni chiqaramiz:
    
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# # Ro'yxat elementlarini o'chirish 

# # Avvalgi darslarimizning birida ro'yxat elementini o'chirish uchun .remove(qiymat)
# # metodi ro'yxatdan eng birinchi uchragan qiymatni o'chiradi.Agar ro'yxatimizda
# # ma'lum bir qiymat bir necha bor takrorlangan bo'lsa, ularning barchasini o'chirish
# # uchun while siklidan foydalanishimiz mumkin:

# cars = ['lacetti','nexia','toyota','nexia','malibu','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)
# # Yuqoridagi sikl toki cars ro'yxatida nexia qiymati tugagunga qadar takrorlanaveradi.

# # Ro'yxatdan ro'yxatga element ko'chirish
# # Tasavvur qiling,bizda ma'lum bir ro'yxat bor,biz ro'yxatdagi har bir element ustida biror
# # amalni bajarib, uni birinchi ro'yxatdan ikkinchi ro'yxatga ko'chirib olmoqchimiz.
# # Shunday holatlarda while sikli juda qo'l keladi.
# # Quyidagi misolni ko'raylik.Biz talabalar ro'yxati bor.while sikli,toki ro'yxatda talabalar
# # bor ekan, ayalanuveradi.Sikl ichida biz .pop() metodi yordamida talabaning ismini ro'yxatdan 
# # sug'irib oldik va foydalanuvchidan talabani baholashni so'radik.Talabaning ismi va bahosini 
# # lug'at elementi ko'rinishida saqlab qo'ydik (talaba - kalit,baho - qiymat).

# talabalar = ['hasan','husan','olim','botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
    
# # Yuqoridagi biz while sikli yordamida ro'yxat va lug'atlar ustida bajarish mumkin bo'lgan ba'zi
# # misollarni ko'rdik.Albatta,dasturlash davomida bundan boshqa holatlar ham uchrashi tabiiy.
