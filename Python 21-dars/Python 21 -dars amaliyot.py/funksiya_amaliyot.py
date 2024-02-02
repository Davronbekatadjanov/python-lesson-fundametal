"""
Mavzu:Funksiya 
Sana:04.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
 """
# # Foydalanuvchi ismi va yoshini so'rab,uning tug'ilgan yilini hisoblaydi
# # funksiya yozing.
# def yosh_hisobla(ism,tugilgan_yil,joriy_yil=2023):
#     """Foydalanuvchining tugilgan 
#        yilini sorab yoshini chiqaradigan funksiya"""
#     print(f"{ism} {joriy_yil-tugilgan_yil} yoshdasiz") 
# yosh_hisobla('olim',2005)

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yoshing.,
# def son_hisobla(son):
#     """Foydalanuvchidan son olib uning kvadrati va
#     kubini konsolga chiqaruvchi funksiya 
#     """
#     print(f"{son} kvadrati {son**2} ga teng,\n"
#           f"{son} kubi {son**3} ga teng")
# son_hisobla(5)  

# # Foydalanuvchidan son olib,son juft yoki toqligini konsoga  
# def juftmi(son):
#     """Kiritilgan soni juft yoki toqligin aniqlovchi funksiya
#     """
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
        
# juftmi(5)

# # Foydalanuvchidan ikkita son olib,ularda kattasini konsolga chiqaruvchi
# # funksiya yozing.Agar son teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

# def solishtir(x,y):
#     """Sonlarni solishtiruvchi funksiya """
#     if x>y:
#         print(f"{x}>{y}")
#     elif x<y:
#         print(f"{x}<{y}")
#     else:
#         print(f"{x}={y}")
# solishtir(10,20)
# solishtir(-29,87)
# solishtir(38,7)
# solishtir((4/7)*(-2/3),(49/16)*4/3)
# solishtir((4/7)*(-2/3),(16/49)*(-1/4))

# # Foydalanuvchidan x va n sonlarini olib,x ning n-darajasini konsolga chiqaruvchi funksiya yozing
# def daraja(x,n):
#     """Kiritilgan x va solarini olib, x ning n-darajasini chiqaruvchi funksiya"""
#     print(f"{x} ning {n} darajasi {x**n} ga teng")
# daraja(2,5)
# daraja(25,6)

# # Yuqoridagi funksiyadan n uchun 2 standart  qiymat bering.
# def daraja(x,n=2):
#     """Kiritilgan x va n soniga standart qiymat berildi, x ning 2 darajasini chiqaruvchi funksiya"""
#     print(f"{x} ning {n} darajasi {x**n}")
# daraja(6)

# # Foydalanuvchidan son qabul qilib,soning 2 dan 10 gacha bo'lagan sonlarga qoldiqsiz bo'linishini
# # tekshiruvchi funksiya yozing.Natijalarni konsolga chiqaring.
# # Natijani konsolga chiqaring("15 soni 3 ga qoldiqsiz bo'linadi")degan ko'rinishida 
# def bolinish_alomatlari(son):
#     for n in range(2,11):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi.")
# bolinish_alomatlari(96)

