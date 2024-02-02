"""
Mavzu:Nesting amaliyot
Sana:22.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Adabiyot (ilm-fan,san'at,internet) olamidagi 4 ta mashhur shaxslar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.Lug'atlarni bitta ro'yxat ga joylang va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# buxoriy = {
#   'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#   'tyil':810,
#   'vyil':870,
#   'tjoy':'Buxoro'
# }

# qodiriy = {
#   'ism':'Abdulla Qodiriy',
#   'tyil':1894,
#   'vyil':1938,
#   'tjoy':'Toshkent'
# }

# vohidov = {
#   'ism':'Erkin Vohidov',
#   'tyil':1936,
#   'vyil':2016,
#   'tjoy':"Farg'ona"
# }

# navoiy = {
#   'ism':'Alisher Navoiy',
#   'tyil':1441,
#   'vyil':1501,
#   'tjoy':"Hirot"
# }

# shaxslar = [buxoriy,qodiriy,vohidov,navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy} joyda tavvalud topgan, "
#           f"{vyil-tyil} yil umr ko'rgan.")

# # Yuqoridagi lug'atlarga har bir shaxsning mashhur asarlari ro'yxatini ham qo'shing.for sikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# buxoriy = {
#          'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#          'tyil':810,
#          'vyil':870,
#          'tjoy':'Buxoro',
#          'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
# }

# qodiriy = {
#   'ism':'Abdulla Qodiriy',
#   'tyil':1894,
#   'vyil':1938,
#   'tjoy':'Toshkent',
#   "asarlar":["Otkan kunlar",'Mehribon chayon',',Obit ketmon']
# }

# vohidov = {
#   'ism':'Erkin Vohidov',
#   'tyil':1936,
#   'vyil':2016,
#   'tjoy':"Farg'ona",
#   "asarlar":['Menning yulduzm','Tong nafasi','Yurak aqla','Palatkada yozilgan doston']
# }
# navoiy = {
#   'ism':'Alisher Navoiy',
#   'tyil':1441,
#   'vyil':1501,
#   'tjoy':"Hirot",
#   "asarlar":['Xamsa','Lison tu-tayr','Nasoyim ul-muhabbat','Munojot']
# }

# shaxslar = [buxoriy,qodiriy,vohidov,navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashhhur asarlar:")
#     for asar in asarlar:
#         print(asar)


# # Oila a'zolaringizda (do'stlaringiz) 3 ta sevimli kino-seriali haqida so'rang.Do'stingiz ismi kalit,uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang.Natijani konsolga chiqaring.
# kinolar = {
#   'Ali':['Terminator','Mahabharat','Rembo'],
#   'Vali':['Tenet','Abdullajon','Xazina'],
#   'hasan':['Bomba','Gandi','Superman'],
#   'husan':['Tarzan','Buxoriy','al-termiziy']
#   }

# for ism, kinolar in kinolar.items():
#   print(f"\n {ism.title()}ning sevimli kinolari:")
#   for kino in kinolar:
#     print(kino)

# # Davlatlar degan lug'at yarating,lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.Har bir davlat haqida ma'lumotni konsolga chiqaring.
# davlatlar = {
#   "O'zbekiston":{'poytaxti':'Toshkent',
#                 'maydoni':448978,
#                 'aholisi':36_001_236,
#                 'pul_birligi':"so'm"
#                 },
#   'rossiya':{'poytaxti':'Moskva',
#             'maydoni':17_098_246,
#             'aholisi':145_478_097,
#             'pul_birligi':"rubl"
#             },
#   'Yaponiya':{'poytaxti':'Toshkent',
#           'maydoni':377835,
#           'aholisi':127_417_244,
#           'pul_birligi':"Yen"
#           },
#   'Xitoy':{'poytaxti':'Pekin',
#           'maydoni':9_596_962,
#           'aholisi':1_347_374_752,
#           'pul_birligi':"Yuan Renminbi"}
# }

# for davlat,info in davlatlar.items():
#   if davlat.lower()=='aqsh':
#     davlat = davlat.upper()
#   else:
#     davlat = davlat.capitalize()
#   print(f"\n {davlat}ning poytaxti {info['poytaxti'].title()}"
#        f"\nHudud: {info['maydoni']} kv.km"
#        f"\nAholisi: {info['aholisi']}"
#        f"\nPul birligi: {info['pul_birligi']}"
#        )
# # Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlar emas,foydalanuvchi so'ragan davlat haqida ma'lumot bering.Agar davlat sizning lug'atingizda mavjud bo'lmasa,"Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
# davlatlar = {
#   "o'zbekiston":{'poytaxti':'Toshkent',
#                'maydoni':448_978,
#                'aholisi':36_001_236,
#                'pul_birligi':"so'm"
#                },
#   'rossiya':{'poytaxti':'Moskva',
#            'maydoni':17_098_246,
#            'aholisi':145_478_097,
#            'pul_birligi':"rubl"
#            },
#   'yaponiya':{'poytaxti':'Tokio',
#           'maydoni':377_835,
#           'aholisi':127_417_244,
#           'pul_birligi':"Yen"
#               },
#   'xitoy':{'poytaxti':'Pekin',
#          'maydoni':9_596_962,
#          'aholisi':1_347_374_752,
#          'pul_birligi':"Yuan Renminbi"}
# }

# davlat = input('Davlat nomini kiriting:').lower()
# if davlat in davlatlar:
#   info = davlatlar[davlat]
#   print(f"\n {davlat.capitalize()}ning poytaxti {info['poytaxti'].title()}"
#        f"\nHudud: {info['maydoni']} kv.km"
#        f"\nAholisi: {info['aholisi']}"
#        f"\nPul birligi: {info['pul_birligi']}")
# else:
#   print("Bizda bunday davlat haqida ma'lumot mavjud emas:")
  