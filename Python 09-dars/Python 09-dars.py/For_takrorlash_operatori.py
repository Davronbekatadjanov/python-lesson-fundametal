"""
Mavzu:For takrorlash operatori
Sana:11.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # for silkli

# # Dasturlash davomida kodimizning biror qismini bir necha bor takrorlash talab etilishi mumkin.Misol uchun,
# # ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish yoki bo'lmasa har bir elementni kvadratga oshirish va hokazo.
# # Mana shunday vaziyatda bizga for operatori yordam beradi.Bu operator yordamida biz kodlarni qayta-qayta takrorlashimiz mumkin.
# # Dasturlashda bu sikl(loop) deb ataladi.
# # Quyidagi misolni ko'ramiz.Biz mehmonlar ro'yxati bor,har bir mehmonning ismini yangi qatordan chiqarmoqchimiz.
# # Buning uchun quyidagi kodni yozamiz.
# mehmonlar = ['Ali', ' Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in  mehmonlar:
#     print(mehmon)

# # Kodni tahlil qilaylik:
# # 1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan to'ldirdik.
# # 2-qatorda for siklini boshladik.Bu qator Pythonga mehmonlar degan ro'yxatdan har bir elementini olib,uni yangi,mehmon degan o'zgaruvchiga yuklashni buyuryapti (o'zgaruvchiga istalgan nom berishingiz mumkin.Biz tushunarli bo'lishi uchun mehmon deb ataladi).
# # 3-qatorda mehmon degan o'zgaruvchining qiymatini konsolga chiqardik.Bu sikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.

# # "for" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.
# # Yuqoridagi kodni oddiy tilga tarjima qilsak, mehmonlar ro'yxatidagi har bir mehmon uchun uning ismini konsolga chiqar degan ma'no kelib chiqadi.

# # for sikli qanday ishlaydi:
# mehmonlar = ['Ali', ' Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#   print(f"Hurmatli {mehmon}")
#   print("Siz 20-mart kuni nahorgi oshga taklif qilamiz.")
#   print("Hurmat bilan,Palonchiyevlar oilasi")

# # Yuqoridagi kodda 2-qator sikl sharti deyiladi.Aynana shu qator kodimiz nech marta takrorlanishini belgilaydi.Bizning holatimizda sikl mehmonlar ro'yxati ichidagi elementlar tugagunga qatar takrorlanadi.Sikl sharti ikki nuqta (:) bilan tugaydi.Undan keyingi 3 qator siklning badani deyiladi.
# # Sikl badani surilish (indentation) bilan ajratiladi,ya'ni siklning takrorlanuvchi qismi asosiy koddan birmuncha o'ngroqqa surilgan bo'ladi.Agar biz mana shu surilishni tark etsak,kodimiz xato beradi:
# mehmonlar = ['Ali','Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
# print(f"Hurmatli {mehmon}")
# print("Siz 20-mart kuni nahorgi oshga taklf qilamiz.")
# print("Hurmat bilan,Palonchiyevlar oilasi")

# # Ko'rib tuganingizdek,for dan keyingi qatorni o'ngga surmaganimiz uchun indentation error (surish xatolik) degan xabarni oldik.
# # Sikl shartidan so'ng o'ngga surib yozilgan barcha qatorlar sikl badanida deb hisoblanadi (garchi qatorlar orasidan joy tashlab yozsak ham).
# mehmonlar = ['Ali','Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#   print(f"Hurmatli {mehmon}")
#   print("Siz 20-mart kuni nahorgi oshga taklf qilamiz.")
#   # keyingi qator ham sikl ichida hisoblanadi.
#   print("Hurmat bilan,Palonchiyevlar oilasi")
# # Sikl badanidan chiqish uchun kodni yana qator boshidan yozish kifoya:
# cars = ['nexia', 'tico', 'tico']
# for car in cars: # <- sikl badani 
#   print(car.title()) # <- sikl badani 
# print("Ko'rganlar qilar havas!") # <- sikl keyingi kod
# # # Agar yuqoridagi kodimizda 4-qatorni surmasdan yozsak,Python bu qatorni ham siklning ichida deb qabul qiladi va qayta-qayta takrorlaydi.
# cars = ['nexia', 'tico', 'damas']
# for car in cars:
#   print(car.title())
#   print("Ko'rganlar qilar havas!")

# # for yordamida sonli ro'yxatlar bilan ishlash

# # Ushbu misolni ko'zdan kechiramiz:
# sonlar = list(range(1,11))
# for son in sonlar:
#   print(f"{son} ning kvadrati {son**2} ga teng")
  
# # for yordamida yangi ro'yxat ham shakllantirish mumkin.Quyidagi dastur avval 1 dan 10 gacha sonlar ro'yxatini yaratib olyapmiz.Keyin esa sonlar kvadratini joylash uchun bo'sh ro'yxat yaratdik.for sikli ichida esa har bir sonning kvadratini hisoblab, sonlar_kvadrati ro'yxatiga qo'shib boryapmiz.
# sonlar = list(range(1,11))
# sonlar_kvadrati = []
# for son in sonlar:
#   sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

# for va input()
# for operatori va input() funkisiyasi yordamida foydalanuvchidan bir nechta qiymatlar qabul qilish va olingan qiymatlarni ro'yxatga joylash mumkin:

dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
  dostlar.append(input(f"{n+1}-ismini kiriting: "))
print(dostlar)

# Kodni tahlil qilamiz:
# 1-qatorda bo'sh do'stlar ro'yxatini yaratdik.
# 2-qatorda ekranga "5 ta eng yaqin do'stingiz kim?" degan xabarni xabarni chiqardik.
# 3-qatorda siklni boshladik,range(5) funksiyasi 0 dan 5 gacha sonlar ketma-ketligini yaratadi.(0,1,2,3,4,) sikl esa n shularning har biriga teng bo'lib chiqqncha davom etadi.
# 4-qatorda sikl badani kegan.Bu yerda biz foydalanuvchidan n+1 do'stingizni kiriting deb so'radik.Nima uchun n+1 (n emas)? Sababi,n 0 dan 4 gacha qiymatlarni oladi,foydalanuvchiga tushunarli bo'lshi uchun esa biz,"0-ismni kiriting:" deb emas,balki n+1,ya'ni 1-ismni kiriting deb murojaat etyabmiz.
# 5-qatorda shakllangan ro'yxatni konsolga chiqardik.for sikli har qanday dasturlash tilining muhim qismlaridan hisoblanadi va biz bu operatorga hali takror-takror qaytamiz.

