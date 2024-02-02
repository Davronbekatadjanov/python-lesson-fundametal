"""
Mavzu:Lug'at elementlari bilan ishlash
Sana:18.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Avvaligi bo'limda lug'at elementlarga kalit so'z orqali murojaat etishni o'rgandik.Lug'atlar katta yoki kichik bo'lishi mumkin.Ba'zida lug'atdagi barcha kalitlarni yoki qiymatlarni bilmasligimiz mumkin.Bunday holatda qanday yo'l tutamiz?
# # Ushbu darslarimizda lug'at elementlarini turli usullar yordamida chiqarishni o'rganamiz.

# # .items() metodi

# # Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.
# talaba = {
#   'ism':'alijon',
#   'familiya':'shamsiyev',
#   'yosh':22,
#   'fakultet':'matematika',
#   'kurs':4
# }
# print(talaba.items())

# # Bu metodni to'g'rida to'g'ri emas,for sikl yordamida chaqirish orqali lug'atdagi barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.
# for kalit,qiymat in talaba.items():
#   print(f"Kalit: {kalit}")
#   print(f"Qiymat: {qiymat}")
  
# # Yuqoridagi dasturda talaba lug'atidagi har bir kalit va qiymat juftligini konsolga chiqardik.E'tibor bering,for siklida biz bir emas,ikkita o'zgaruvchi yaratib oldik (kalit va qiymat).
# # Bu usul lug'atlardagi ma'lumotlarni chiroyli ko'rinishda chiqarish uchun juda qulay.


# telefonlar = {
#   'ali':'iphone x',
#   'vali':'galaxy s9',
#   'olim':'mi 10 pro',
#   'orif':'nokia 3310'
# }
# for k, q in telefonlar.items():
#   print(f"{k.title()}ning telefoni {q}")

# # .key() metodi
# # Agar lug'atdagi kalit so'zlarni topish talab qilinsa, .key() metodidan foydalanamiz:

# mahsulotlar = {# Do'kondagi mahsulotlar
#   'olma':10000,
#   'anor':20000,
#   'uzum':40000,
#   'anjir':25000,
#   'shaftoli':30000
# }

# print(mahsulotlar.keys())

# # Bu yerda ham for siklidan foydalanish mumkin:
# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#   print(mahsulot.title())

# # Yuqoridagi kodimizda for siklida .keys() metodini ishlatmasak ham,xuddi shu natija chiqadi.

# # Ro'yxat va Lug'at
# # for sikli va if sharti yordamida lug'atdagi biror qiymatlarni alohida chiqarishimiz ham mumkin:
# mahsulotlar = {
#   'olma':10000,
#   'anor':20000,
#   'uzum':40000,
#   'anjir':25000,
# }

# bozorlik = ['anor','uzum','non','baliq']
# for m in mahsulotlar:
#   if m in bozorlik:
#     print(f"{m.title()} {mahsulotlar[m]} so'm")

# # Yuqoridagi kodga e'tibor bering.Biz avval bozorlik degan ro'yxat yaratdik (uyga bozor qilyapmiz),keyin esa mahsulotlar lug'atidagi har bir mahsulotni bizdagi bozorlik ro'yxati bilan solishtirdik.Agar mahsulot bizning bozorlik ro'yxatimizda bo'lsa,uning narxini konsolga chiqardik.
# # Quyidagi misolda esa,aksincha,bozorlik ro'yxatidagi har bir elementni do'kondagi mahsulotlar bilan solishtiramiz va mahsulot do'konda yo'q bo'lsa,do'konga murojaat qoldiramiz:
# for buyum in bozorlik:
#   if buyum not in mahsulotlar:
#     print(f"Kechirasiz, bizda {buyum} yo'q")

# # Lug'at elementlaarini tartib bilan chiqarish
# # Avval aytganimizdek,lug'at elementlari biz kiritgan tartibda saqlanadi.Agar elementlarini alifbo tartibida chiqarish talab qilinsa,sorted() funksiyasidan foydalanamiz:

# mahsulotlar = {
#   'olma':10000,
#   'anor':20000,
#   'uzum':40000,
#   'anjir':25000,
# }
# print("Do'konimzidagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#   print(mahsulot.title())

# # .values() metodi 
# # Yuqorida biz .key() metodi yordamida lug'atdagi elementlarning kalitlarini ko'rishni o'rgandik.Agar element qiymatlarni topish talab qilinsa, .values() metodidan foydalanamiz:
# telefonlar = {
#   'ali':'iphone x',
#   'vali':'galaxy s9',
#   'olim':'mi 10',
#   'orif':'nokia 3310'
# }
# print(telefonlar.values())

# # Quyidagi kodni ham bajarib ko'ramiz:
# print('Foydalanuvchilarning telefonlari:')
# for tel in telefonlar.values():
#   print(tel)

# Yuqoridagi usul bilan qiymatlarni chiqarganimizda lug'atdagi barcha qiymatlar chiqib keladi.Agar biror qiymat ko'p marta qaytarilsa,konsolga ham ko'p marta chiqadi.
# Quyidagi misolni ko'ramiz:
telefonlar = {
  'ali':'iphone x',
  'vali':'galaxy s9',
  'olim':'mi 10',
  'orif':'nokia 3310',
  'hamida':'galaxy s9',
  'maryam':'huawei p30',
  'tohir':'iphone x',
  'umar':'iphone x'
}
print('Foydalanuvchilarning telefonlari:') 
for tel in telefonlar.values():
  print(tel)

# Yuqoridagi natijaga e'tibor bersangiz,bir nechta foydalanuvchilar iphone x va galaxy s9 telefonidan foydalanar ekan va bu modellar qayta-qayta konsolga chiqdi.
# Buning oldini olish uchun set() funksiyasidan foydalanishimiz mumkin.Bu funksiya to'plam yaratish uchun ishlatiladi:
print('Foydalanuvchilarning telefonlari:')
for tel in set(telefonlar.values()):
  print(tel)
  
