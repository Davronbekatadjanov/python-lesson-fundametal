"""
Mavzu:if-else amaliyot
Sana:12.01.2023
Muallif:Atdjanov Davronbek
telegram:@atadjanovd
"""
# # Quyidagi dasturlarni Pythonda bajarib ko'ring:

# avtolar =  ['audi','bmw','volvo','kia','hyudai']
# for avto in avtolar:
#     if avto == 'bmw':
#       print(avto.upper())
#     else:print(avto.title())
 
# javoblar = float(input("12x6 nechiga tengiz?>>>"))
# if javoblar!=72:
#   print("Javob xato!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18:
#   print('Xush kelibsiz!')
# else:
#   print('Kirish mumkin emas!')

# yil = int(input("Tug'ilgan yilingizni kirting:"))
# if 2023-yil<18:
#   print(f"Yoshingiz {2023-yil}da ekan") 
#   print("Krish mumkin emas!")
# else:
#   print("Xush kelibsiz!")

# login = input("Yangi login tanlang:")
# if len(login)<=5: # login uzunligini tekshiramiz
#   print("Login 5 harfdan ko'roq bo'lishi shart!")
# else:
#   print("Assalom alaykum ",login)

# Quyidagi vazifalarni bajaring:

# # Yangi cars = ['toyota', 'mazda', 'hyudai', 'gm', 'kia'] degan ro'yxat tuzing,elementlarining birinchi harfini katta qilib konsolga chiqaring.GM uchun ikkala harfni katta qiling.
# cars = ['toyota','mazda', 'hyudai', 'gm', 'kia']
# for car in cars:
#   if car == 'gm':
#     print(car.upper())
#   else:
#     print(car.title())\

# # Yuqoridagi mashqni teng emas (!=) opertori yordamida bajaring.
# for car in cars:
#   if car != 'gm':
#     print(car.title())
#   else:
#     print(car.upper())

# # Foydalanuvchi login ismini so'rang.Agar login admin bo'lsa,"Xush kelibsiz!,Admin.Foydalanuvchilar ro'xatini ko'rasizmi?" xabarini konsolga chiqaring.Aks holda,"Xush kelibsiz,(foydalanuvchi_ismi)!" matnini konsolga chiqaring.

# login = input("Iltimos login kiriting:")
# if login == 'admin':
#   print("Xush kelibsiz,Admin.Foydalanuvchilar ro'xatini ko'rasizmi!")
# else:
#   print("Xush kelibsiz ", login)

# # Foydalanuvchidan 2 ta son kirtishini so'rang.Agar ikki son bir biriga teng bo'lsa,"sonlar teng" ekan degan yozuvni konsolga chiqaring.
# a = float(input("Birinchi soni kiriting:"))
# b = float(input("Ikkinchi soni kiriting:"))
# if a==b:
#   print("Sonlar teng")
# else:
#   print("Sonlar teng emas")

# # Foydalanuvchidan istalagan soni kiritishini so'rang.Agar son manfiy bo'lsa,konsolga "Manfiy son",agar son musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
# son = float(input("Istalgan sonni kiriting:"))
# if son>0:
#     print("Son musbat")
# else:  
#     print("Son manfiy")


# Foydalanuvchidan son kiritishini so'rang.Agar son musbat bo'lsa,uning ildizini hisoblab konsolga chiqaring.Agar son manfiy bo'lsa,"Musabat son kiriting" degan xabarni chiqaring.
# son = float(input("Istalgan son kiriting:"))
# if son>0:
#   print(son**0.5)
# else:
#   print("Musbat son kiriting:")

# # Kiritilgan sonning toq yoki juftligini konsulga chiqaruvchi dasturni yozing.
# son = int(input("Istalgan soni kiriting:"))
# if (son%2==0):
#    print("Bu son juft son")
# else :
#   print("Bu son toq son")
  