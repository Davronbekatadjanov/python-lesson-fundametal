"""
Mavzu:Qiymat qaytaruchi funksiya
Sana:06.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Qiymat qaytaruvchi funksiya
# # Avvalgi darsimizda yaratgan barcha funksiyalarimiz natijalarni konsolga chiqarayotgan edi.
# # Aslida,aksar holatlarda bu g'ayrioddiy.Sababi,dasturchi sifatida biz konsolga chiqqan
# # ma'lumotdan unumli foydalana olmaymiz.Konsoldagi qiymatni o'zgaruvchiga yuklab,undan kelajakda
# # foydalanib ham bo'lmaydi.Funksiyadan unumli foydalanish uchun undan biror qiymatni qaytarish
# # maqsadga muvofiq bo'ladi.

# # Funksiyadan yagona qiymat qaytarish

# # Avvalgi bo'limdagi toliq_ism funksiyamizga o'zgartirish kiritamiz.Bu safar funksiyamiz natijani
# # konsolga chiqarmasdan,qiymat sifatida qaytaradi.Buning uchun maxsus return operatoridan foydalanamiz.

# def toliq_ism_yasa(ism,familiya):
#     """Toliq_isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# # Yuqoridagi funksiyamizga ahamiyat bersangiz,uning badanida endi print() funksiyasi yo'q.
# # Buning o'rniga funksiyamiz return operatori yordamida toliq_ism degan o'zgaruvchining qiymatini qaytar adi.
# # Funksiya badani to return operatoriga qadar bajariladi.returndan so'ng yozilgan kodlar funksiya badanida bo'lsa ham,bajarilmaydi.
# # Endi funksiyadan to'g'ri foydalanish uchun u qaytargan qiymatni biror o'zgaruvchiga yuklashimiz kerak:

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov')

# # Yuqoridagi kodlarni bajarganimizda konsolga hech narsa chiqmaydi.talaba1 va talaba2 o'zgaruvchilarining qiymatini
# # ko'rish uchun esa print() funksiyadan foydalanamiz.
# print(f"Darsga kemagan talabalar: {talaba1} va {talaba2}")

# # Demak,qiymat qaytaradigan funksiyaning afzalligi shundaki,biz bu qiymatlardan keyin ham bemalol foydalanishimiz mumkin.

# # Funksiya ichidagi o'zgaruvchilar mahalliy yoki ichki o'zgaruvchilar deyiladi(local variables).Ichki  o'zgaruvchilar
# # faqtagina funksiya ichida mavjud bo'ladi,ularga tashqaridan murojaat etib bo'lamaydi.Shuning uchun ham funksiya o'zgaruvchi
# # emas qiymat qaytaradi.

# # Ixtiyoriy argumentlar
# # Avvalgi darsimizda funksiyalarga standart parametr berishni ko'rib chiqqan edik.Xuddi shu usul bilan ba'zi argumentlarni ixtiyoriy
# # qilishimiz mumkin.Ya'ni funksiya ishlashi uchun bu argumentlarni kiritish majburiy emas,ixtiyoriy bo'ladi.
# # Keling,avvalgi funksiyamizni o'zgartiramiz va unga yana bitta otasining_ismi degan parametr qo'shamiz,lekin bu parametr ixtiyoriy bo'ladi.
# # Buning uchun funksiya yaratishda  otasining_ismi = '' deb yozib ketamiz.

# def toliq_ism_yasa(ism,familiya,otasining_ismi=''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjud bo'lsa.
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# # Yuqoridagi funksiyani tahlil etadign bo'lsak, 3-qatorda biz otasining_ism parametr bo'sh yoki yo'ligini tekshirdik.Pythonda

# # if dan so'ng bo'sh  bo'lmagan matn(string) yozsak,bu shart True qaytardi.Demak,bu ixtiyoriy parametr kiritilgani yoki yo'qligiga qarab
# # funksiyamiz turlicha qiymat qaytaradi.
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# #  Funksiyaga lug'at qaytarish
# # Funksiyadan sodda qiymat emas,ro'yxat,lug'at va boshqa ma'lumot turlarini ham qaytarishimiz mumkin.Quyidagi funksiya mashina
# # haqidagi ma'lumotlarni jamlab,ularni lug'at ko'rinishida qaytaradi:
# def avto_info(make,model,rangi,korobka,yili,narxi=None):
#     avto = {'kompaniya':make,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narx':narxi}
#     return avto


# # # E'tibor bering,narxi nomli parametriga None standart qiymatini berib ketdik.None Pythonda mavjud emas ma'nosini beradi va
# # # if yordamida tekshirganda False mantiqiy qiymatini qaytardi.

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar=[avto1,avto2]
# print('Onlayn bozordagi mavjud avtomashinalar: ')
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narxi:{narx}")


# # Dastur natijasini tahlil qilishni sizga vazifa sifatida qoldiramiz:
# # Onlayn bozordagi mavjud avtomashinalar:
# # Qora Malibu.Narxi:Noma'lum
# # Oq Gentra.Narxi:15000

# Funksiyadan ro'yxat qaytaramiz

# # Biz avvalroq range() funksiyasi bilan tanishgan edik.Bu funksiya 2 ta qabul qilib,shu ikki son
# # oralig'idagi sonlarni ro'yxat ko'rinishida qaytarsin.
# def oraliq(min,max,):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))

# # Yuqoridagi funksiyaga uchinchi,qadam deb nomlangan ixtiyoriy parametrni qo'sha olasizmi?
# print(oraliq(0,21,2))

# # Funksiyalarni siklda ishlatish

# # Funksiyalarni takrorlash uchun sikldan foydalanishimiz mumkin.Quyidagi misolda biz while yordamida
# # avvalroq yaratgan avto_info funksiyamizni bir necha bor chaqiramiz va salondagi avtomashinalar  ro'yxatini shakllantiramiz.
# # Bunda ro'yxatning har bir elementi avto_info funksiyasidan qaytagan lug'at bo'ladi.

# def avto_info(make,model,rangi,korobka,yili,narxi=None):
#     avto = {'kompaniya':make,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narx':narxi}
#     return avto


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = [] # salondagi avtolar uchun bo'sh ro'yxat

# while True:
#     print("Quyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("\nIshlab chiqaruvchi:")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narxi=input("Narxi:")
#     # Kiritilgan ma'lumotlardan  avto_info  yordamida
#     # lug'at shakllantirib ,ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narxi))

#     # Yana avto qo'shish-qo'shmaslik so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes\no): ")
#     if javob=='no':
#         break
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} karobka. Narxi:{narx}")


# # Yuqoridagi funksiyani Pythonda bajarib ko'ring.Ro'yxatga bir necha qiymatlar qo'shing.
# # Natijalarni konsolga chiroyli qilib chiqaring.
