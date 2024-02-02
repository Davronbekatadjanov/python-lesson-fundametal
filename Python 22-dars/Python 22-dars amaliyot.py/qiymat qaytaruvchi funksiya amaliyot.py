"""
Mavzu:Qiymat qaytaruvchi funksiya amaliyot
Sana:07.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanov
"""

# # Foydalanvuchidan ismi,familiyasi,tug'ilgan yili,tug'ilgan joyi,elektron manzili
# # va telefon raqamini qabul qilib,lug'at ko'rnishida qaytaruvchi funksiya yozing.
# # Lug'atda foydalanlanuvchi yoshi ham bo'lsin.Ba'zi argumentlarni kiritishni ixtiyoriy
# # qiling(masalan,tel.raqam,el.manzili)
# def mijoz_info(ismi,familiyasi,tyil,tjoy,email,tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruchi funksiya"""
#     mijoz = {'ism':ism,
#                     'familiya':familiya,
#                     'tyil':tyil,
#                     'yoshi':2023-tyil,
#                     'email':email,
#                     'telefon':tel}
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting:")
# mijozlar = []
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili:  "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism,familiya,tyil,tjoy,email,telefon, ))
#     javob = input("Davom etasizmi?(ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#     f"{mijoz['yoshi']} yoshda,telefoni: {mijoz['telefon']}")


# Uchta son qabul qilib,ulardan eng kattasini qaytaruvchi funksiya yozing.

# def kattasi(x,y,z):
#     max = x
#     if y>max:
#         max = y
#     if z>=max:
#         max = z
#     return max

# kattasi(10,20,-5)

# # Foydalanuchidan aylananing radiusini qabul qilib olib,uning radiusini,diametrini,perimetr va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing.
# def aylana_info(radius,pi=3.14159):
#     aylana = {"radius":radius,
#               "diametr":2*radius,
#               "perimetr":2*radius*pi,
#               "yuza":pi*radius**2}
#     return aylana
# aylana_info(5)

# # Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar -faqat birga ba o'ziga qoldiqsiz bo'linuvchi,1 dan katta musbat sonlar)

# def tub_sonlar_top(min,max):
#     tub_sonlar = []
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#              tub = True
#         else:
#             for x in range(2,n):
#                 if (n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
# tub_sonlar_top(1,20)

# # Foydalanuvchidan son qabul qilib,shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi fuksiya yozing.Ta'rif:Har bir hadi o'zidan oldingi ikkita hadning yig'indisiga teng bo'lgan ketma-ketlik.Fibonachchi ketma-ketligi deyiladi.Bunda boshlang'ish had ko'pincha 1 deb olinadi

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
# print(fibonacci(10))