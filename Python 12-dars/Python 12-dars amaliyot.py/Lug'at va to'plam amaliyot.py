"""
Mavzu:Lug'at va to'plam amaliyot
Sana:18.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # otam(onam,akam,ukam va hakazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta ma'lumot kiriting(ism,tug'ilgan yili,shahri,manzili va hokazo).Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring:Otamning ism Movlutdin,1954-yilda,Samarqand viloyatida tug'ilgan.
# otam = {'ism':'aybek','t_yil':1973,'manzil':"qoraqolpog'iston"}
# print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda , {otam['manzil'].title()} Respulikasida tug'ilgan ")
# onam = {'ism':'gulnora','t_yil':1974,'manzil':"qoraqolpog'iston"}
# print(f"Onamning ismi {onam['ism'].title()}, {onam['t_yil']}-yilda, {onam['manzil'].title()} Respulikasida tug'ilgan ")

# # Oila a'zolaringizning sevimli taomlari lug'atini tuzing.Lug'atda kamida 5 ta ism-taom juftligi bo'lsin.Kamida uch kishining sevimli taomini konsolga chiqaring:
# taom = {
#   'amirbek':'tandir',
#   'davronbek':'qavoqli somsa',
#   'hasan':'manti',
#   'onam':"lag'mon",'otam':'kabob'
# }
# print(f"Oila a'zolarimni sevimli taomlari,otam:{taom['otam']},onam: {taom['onam']},ukam: {taom['davronbek']}.")
# taomlar = taom['davronbek']
# print(f"Davronbekning sevimli taomi {taomlar}")
# # Python izohli lug'ati tuzing.Lug'atga shu kunga qadar o'rgangan 10 ta so'zni (atamani) kiriting (masalan,integer,float,string,if,else va hokazo) va qiymat sifatida har birining qisqacha tarjimasini yozing:
# python_izohli_lugat = {
#   'integer':'Butun son',
#   'float':"O'nlik son",
#   'string':'Matn',
#   'list':"Ro'yxat",
#   'tuple':"O'zgarmas ro'yxat"
# # print(python_izohli_lugat['tuple'])
# }

# kalit = input("Kalit so'zni kiriting:").lower()
# print(python_izohli_lugat.get(kalit,"Bunday so'z mavjud emas!"))

# # Yuqoridagi vazifani if-else yordamida bajaring va natijani foydalanuvchiga tushunarli ko'rinshda chiqaring:

# kalit = input("Kalit so'zni kiriting:").lower()
# tarjima = python_izohli_lugat.get(kalit)
# if tarjima==None:
#   print("Bunday so'z mavjud emas!")
# else:
#   print(f"{kalit.title()} so'zi {tarjima} deb tajima qilinadi.")
  
