"""
Mavzu:for takrorlash operatori amaliyot
Sana:11.01.2023
Muallif:Atadjanov Davronbek
@atdjanovd
"""
# # Kamida 5 elementda iborat ismlar degan tuzing va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ['Ali', 'Boris', 'Davronbek', 'Erdem', 'Dilshodbek']
# for ism in ismlar:
#     print(f"Hurmatli {ism} bizning xizmatimizdan foydalanganingiz uchun raxmat")

# # Yuqoridagi sikl tugaganidan so'ng ekranga "kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing.)
# print(f"Kod {len(ismlar)} ta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.Ro'yxatning har bir elementi kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for son in sonlar:
    print(f"{son} ning kubi {son**3} ga teng")
  # print(son**3) # ikkinchi hisoblash usuli

# # Foydalanuvchidan 5 ta eng sevimli kinolarini kiritishni so'rang konsolga chiqaring:
# kinolar = [] # bo'sh ro'yxat yaratamiz.
# print("5 ta eng sevimli kinolaringiz ni kirting:")
# for n in range(5):
#   kinolar.append(input(f"{n+1}-kinoni kiriting: "))
# print(kinolar)

# # Foydalanuvchidan bugun nechta odam bilan uchrashganini(suhbatlashganini) so'rang va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing.
# # Ro'yxatni konsolga chiqaring.
# n_people = int(input("Bugun nechta odam bilan suhbat qildingiz?>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi:"))
# print(ismlar)
