"""
Mavzu:Bir nechta shartlarni tekshirish amaliyot
Sana:15.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
# # Foydalanuvchidan juft son kiritishni so'rang.Agar foydalanuvchi juft son kiritsa,"Rahamt",agar toq son kiritsa,"Bu son juft emas" degan xabarni chiqaring.
# son = int(input("Juft son kiriting:"))
# if (son%2==0):
# 	print("Rahmat!")
# else:
#   print("Bu son juft emas!")

# # Foydalanuvchi yoshini so'rang va muzeyga kirish uchun chipta narxini quyidagicha chiqaring:
# # Agar foydalanuvchi 4 yoshdan kichkina 60 dan katta bo'lsa,bepul.
# # Agar foydalanuvchi 18 dan kichik bo'lsa,10000 so'm.
# # Agar foydalanuvchi 18 dan katta bo'lsa,20000 so'm.

# yosh = int(input("Yoshinin kiriting:"))
# if yosh>=60:
#   price = 0
# elif yosh<=4:
#   price = 0
# elif yosh<=18:
#   price = 10000
# elif yosh>=18:
#   price = 20000
# print(f"Sizga kirish {price} so'm")

# # Foydalanuvchidan ikkita son kiritishi so'rang,sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring.
# a = float(input("Birinchi soni kiriting:"))
# b = float(input("Ikkinchi soni kiriting:"))
# if (a>b):
# 	print(f"{a} soni katta {b} dan")
# elif (a<b):
# 	print(f"{a} soni kichik {b} dan")
# else:
# 	print(f"{a} soni teng {b} ga")

# # mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.Yangi,savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.Savatdagi elementlarni mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'sa,"Mahsulot do'konimizda bor",aks holda,"Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
# # Yuqoridagi dasturni quyidagi o'zgarrtiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi,bor_mahsulotlar degan ro'yxatga,do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.Agar mavjud_emas ro'yxati bo'sh bo'lsa,"siz so'ragan barcha mahsulotlar do'konimizda bor " degan xabarni,aks holda,"Quyidagi mahsulotlar do'konimizda yo'q" degan xabarni chiqaring:
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# # foydalanuvchilar degan ro'yxat tuzing va kamida 5 ta login qo'shing.Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritga loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.Agar ro'yxatda bunday login mavjud bo'lsa,"Login band,yangi login tanlash!",aks holda,"Xush kelibsiz, {foyalanuvchi}!" xabarini chiqaring.
# user = ['davron','xasan','gang','husan','amirbek']
# login = input("Yangi login kiriting:")
# if login.lower() in user:
#   print("Login band,yangi login kiriting!")
# else:
#   print(f"Xush kelibsiz, {login.title()}!")

# # Foydalanuvchidan biror butun son kiritishni so'rang.Foydalanuvchi kiritgan sonning 2 dan 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
# son = int(input("Butun son kiriting:"))
# for n in  range(1,10000000):
#   if not (son%n):
#     print(f"{son} soni {n} soniga qoldiqsiz bo'linadi")

# 