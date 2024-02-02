"""
Mavzu:Lug'at elementlari bilan ishlash amaliyot
Sana:19.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # Python izholi lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.Lug'atdagi har bir kalit va qiymatni for sikli yordamida,alifbo ketma-ketligida chiroyli  qilib konsolga chiqaring.
# lugat = {
#   'integer':'Butun son',
#   'float':"O'nlik son",
#   'string':'Matn',
#   'pen':'Ruchka',
#   'colors':'Ranglar',
#   'image':'Tasvir',
#   'list':"Ro'yxat",
#   'boolean':'Mantiqiy',
#   'file':'Fayl',
#   'eggs':'Tuxum',}

# for key, value in sorted(lugat.items()):
#   print(f"{key.title()} - {value}")

# # Davlatlar va ularning poytaxtlari lug'atini tuzing.Avval lug'atdagi davlatlarni,keyin poytaxtlarni alohida-alohida,alifbo ketma-ketligida konsolga chiqaring.
   
# davlatlar = { # avval davlatlar degan lug'at yaratamiz.
#   'Uzbekiston':'Toshkent',
#   'Jazir':'Jazir',
#   'Kazakistan':'Astana',
#   'Kyrgyzstan':'Bishkek',
# }
# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#   print(davlat.upper()) # .upper() metodi yordamida davlatlarni keyni katta hariflar bilan konsolga chiqaramiz

# print("Davlatlarning poytaxtlari:") 
# for poytaxt in sorted(davlatlar.values()):
#   print(poytaxt.title())
# # O'qishga qulay usulda chiqaramiz konsolga 
# print('Davlatlar va uning poytaxtlari:')
# for key, value in sorted(davlatlar.items()):
#   print(f"{key.title()} - {value}") # davlatlar va poytaxtlarin alifbo tartibda konsolga chiqaramiz.

# # Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,"Biz bunday ma'lumot yo'q" degan xabarni chiqaring.

# country = input('Qaysi davlatning poytaxtini bilishni istaysiz: ')
# capital = davlatlar.get(country)
# if capital==None:
#   print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
# else:
#   print(f"{country.upper()}ning poytaxti: {capital.title()} shahri")
  
# # Restoran menyusi lug'atini tuzing(kamida 10 ta taom-narx juftligini kiriting).Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.Fodalanuvchi kiritgan taomlarni menyu bilan solishtiring,agar taom menyuda bo'lsa,narxini ko'rsating,aks holda,"bizda bunday taom yo'q" degan xabarni chiqaring.

# menu = { # yangi menyu yaratamiz va narx larini lug'at ko'rinishida kiritamiz values qilib.
#   'osh':25000,
#   'manti':20000,
#   'non':4000,
#   "lag'mon":15000,
#   'somsa':9000,
#   'shashlik':8000,
#   'tabaka':35000
# }

# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:

#          print(f"Kechirasiz, bizda {buyurtma} yo'q.")

           