"""
Mavzu:Nesting 
Sana:21.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Nesting 
# # Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yo boshqa lug'atni yoki,aksincha,ro'yxat ichida lug'atni saqlash ham qo'l kelishi mumkin.Bu ingliz tilida Nesting deyiladi.Nesting Pythondagi foydali xususiyatlardan biridir.Keling,bunga bir nechta misollar ko'rib chiqamiz.

# # Lug'atlar ro'yxati
# # Biz avvalgi darsimizda talabalarning ma'lumotlarini lug'at shaklida saqlashni ko'rgan edik.Shunday talabalardan yuzlab bo'lganda ularning har biriga alohida lug'at qilishimiz tabiiy,lekin bu lug'atlar bilan ishlash qiyinchilik tug'dirishi mumkin.Shunday halotda barcha lug'atlarni (talabalarni) bitta ro'yxatga joylab,ular ustida turli amallar bajarish mumkin.
# # Quyidagi misolda 3 ta alohida lug'atda 3 ta avtomobil haqida ma'lumotlar saqlangan:
# car0 = {
#   'model':'lacetti','color':'oq',
#   'year':2018,'price':13000,
#   'km':50000,'korobka':'avtomat'
# }

# car1 = {
#   'model':'nexia 3','color':'qora',
#   'year':2015,'price':9000,
#   'km':89000,'korobka':'mexanika'
# }

# car2 = {
#   'model':'gentra','color':'qizil',
#   'year':2019,'price':15000,
#   'km':20000,'korobka':'mexanika'
# }

# # Agar biz har bir avtomobil haqida ma'lumot olmoqchi bo'lsak,har bir lug'atga alohida murojaat etishimiz talab qilinadi:
# car = car0
# print(f"{car['model'].title()},\
#   {car['color']} rang,\
#   {car['year']}-yil, {car['price']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['color']} rang,\
#   {car['year']}-yil, {car['price']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['color']} rang,\
#   {car['year']}-yil, {car['price']}$")

# # Yuqoridagi natijani chiqarishning osonroq usuli barcha avtolarni bitta ro'yxatga joylab,gor siklidan foydalanishdir:
# cars = [car0,car1,car2] # Lug'atlar ro'yxati
# for car in cars:
#   print(f"{car['model'].title()}, "
#         f"{car['color']} rang, "
#         f"{car['year']}-yil, {car['price']}$")

# # Ishimiz birmuncha yengillashdi,kodimiz ham qisqardi.Natija esa bir xil.
# # Ro'yxat ichidagi istalgan lug'atga indeks bo'yicha murojaat etishim ham mumkin(lug'at nomini yodlab qolish shart emas).
# print(cars[0])

# # Biror lug'atdagi elementga murojaat etish uchun esa quyidagi usuldan foydalanishimiz mumkin:
# print(cars[0]['model'])
# print(f"{cars[2]['color'].title()} "
#       f"{cars[2]['model']}")

# # for sikli yordamida biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin:
# malibus=[] # Malibus mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = {# har bir yangi avto uchun lug'at yaratamiz
#          'model':'malibu',
#          'color':None, # rangi noaniq
#          'year':2020,
#          'price':None, # rangi belgilanmagan 
#          'km':0,
#          'korobka':'avto'
#          }
  
#     malibus.append(new_car) # lug'atni ro'yxatga qo'shamiz

# # Yuqoridagi misoda biz 10 ta Malibu mashinasidan iborat ro'yxat tuzdik.E'tibor qiling,'rang' kalitiga qiymat bermadik va None deb qoldirdik.
# # Endi ishlab chiqarish jarayonida mashinalarga turli ranglarni berishimiz mumkin.Misol uchun,birinchi 3 ta mashinaga qizil rang beramiz:
# for malibu in malibus[0:3]:
#   malibu['rang']='qizil'
# # Keyingi uchtasi esa qora:
# for malibu in malibus[3:6]:
#   malibu['rang']='qora'

# # Oxirgi 4 ta malibuni qora,karobkasini mexanika qilamiz:
# for malibu in malibus[6:]: # oxirgi 4 ta mashinaning 
#     malibu['rang']='qora' # rangi qora 
#     malibu['korobka']='mexanika' # korobkasi maxanika
# # Keling,endi mashinalarning karobkasidan kelib chiqqan holda narx belgilaymiz:
# for malibu in malibus:
#   if malibu['korobka']=='avto':
#       malibu['price']=40000
#   else:
#       malibu['price']=35000

# # Mashinalar ro'yxatin konsolga chiqaramiz:
# for malibu in malibus:
#     print(malibu.values())
  
# # Lug'at ichida ro'yxat
# # Bir kalitga bir nechta qiymatlar berish talab etilganda qiymatlarni ro'yxat ko'rinishida yozish o'rinlidir.Misol uchun,bir tashkilotda bir nechta dasturchilar ishlaydi va har bir dasturchi turli dasturlash tillarini biladi.Keling,dasturchilar lug'atini tuzamiz va har bir dasturchi haqidagi ma'lumotni konsolga chiqaramiz:
# dasturchilar = {
#   'ali':['python','c++'],
#   'vali':['html','css','js'],
#   'hasan':['php','sql'],
#   'husan':['python','php'],
#   'maryam':['c++','c#'] 
# }
# for ism, tillar in dasturchilar.items():
#   print(f"\n{ism.title()}:", end='')
#   for til in tillar:
#     print(f'{til.upper()}:', end='')

# # print() funksiyasi har bir matndan so'ng yangi qator tashlaydi.Buning oldini olish uchun quyidagi usuldan foydalanish mumkin.
# # print(string, end='')

# # Lug'at ichida lug'AttributeError
# # Bunday qilish tavsiya etilmagan-da,istisno holatlarda lug'at ichidagi qiymatlarni lug'at ko'rinishida ham saqlash mumkin.Misol,uchun joyingizdagi hamkasblaringiz haqidagi ma'lumotlarni saqlashda hamkasbingizning ismi kalit,u haqidagi ma'lumotlar esa lug'at ko'rinishida berilishi mumkin.

# hamkasblar = {
#   'ali':{'familiya':'valiyev',
#         'tyil':1995,
#         'malumot':'oliy',
#         'tillar':['pytho','c++']
#         },
#   'vali':{'familiya':'aliyev',
#          'tyil':2001,
#          'malumot':"o'rta mavsus",
#          'tillar':['html','c++','js']
#          },
#   'hasan':{'familiya':'husanov',
#            'tyil':1999,
#            'malumot':'maxsus',
#            'tillar':['python','php']
#           }
            
# }

# # Hamkasblar to'g'risidagi ma'lumotlarni esa quyidagicha ko'rish mumkin:
# for ism,info in hamkasblar.items():
#   print(f"\n{ism.title()} {info['familiya'].title()}, "
#         f"{info['tyil']}-yilda tug'ilgan. \n "
#         f"Ma'lumot: {info['malumot']}. \n"
#         "Quyidagi dastulash tillarini biladi: ")
#   for til in info['tillar']:
#     print(til.upper())
# # Lug'at ichidagi lug'atlar bir xil tuzilishga ega bo'lgani ishingizni ancha yengillashtiradi,aks holda,kodingiz murakkablashib ketishi mumkin.abs
    
    