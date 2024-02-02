"""
Mavzu:OOP bilan ishlash yoki obyektlar bilan ishlash
Sana:10.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""
# # Xususiyatlarga standart qiymat berish

# # Avvalgi bo'limda biz klass yaratish,unga xususiyatlar va metodlar 
# # qo'shishni ko'rib chiqdik.Klassdan obyekt yaratganimizda esa uning 
# # xususiyatlarini parametr sifatida uzatishni o'radik.
# # Pythonda obyektning ba'zi xususiyatlarini parametr yordamida uzatmasdan,
# # klass yaratishda unga standart qiymat berib ketishimiz mumkin.
# # Keling,Talaba klassimizga qaytamiz.Bu klassimiz 3 ta xususiyatga ega edi;
# # ism,familiya,tyil.Biz yana bitta qo'shimcha bosqich nomli xususiyat qo'shamiz
# # va unga standart qiymat sifatida 1 beramiz,e'tibor qiling,bu xususiyat obyekt 
# # yaratilishida parametr sifatida uzatilmaydi:
# class Talaba:
#     """Talaba nomli klass yaratamiz:
#         We create a class named student"""
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.boshqich = 1
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism 
#     def get_lastname(self):
#         """Talabaning familiyasi qaytaradi"""
#         return self.familiya
#     def get_age(self,yil):
#         return yil-self.tyil
#     def get_info(self):
#         """Talabaning ma'lumotlarni qaytaradi
#             Return the student's data(or infomation)"""
#         return f"{self.ism} {self.familiya},{self.boshqich}-boshqich talabasi."

# # Endi Talaba klassidan yangi obyekt yaratganimizda har bir yangi talabaning kursi
# # 1 ga teng bo'ladi.

# talaba1 = Talaba("Davronbek","Atadjanov",2000)
# print(talaba1.get_info())

# # Standart qiymatni o'zgartirish
# # Obyektning standart qiymatiga ham boshqa xususiyatlar kabi nuqta orqali 
# # murojaat etishimiz va uning qiymatini almashtirishimiz mumkin:
    
# talaba1.boshqich = 2
# print(talaba1.boshqich)

# # Yana boshqa usuli = obyekt xususiyatini yagilovchi metod yozish.
# class Talaba:
#     """Talaba nomli klass yartamiz:
#         We create a class named student"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari 
#         Characteristics of the student"""
#         self.ism = ism
#         self.familiya = familiya 
#         self.tyil = tyil
#         self.bosqich = 1
#     def get_info(self):
#         """Talaba ma'lumotlar qataradi
#             Return student's data(information)"""
#         return f"{self.ism} {self.familiya}.{self.bosqich}-boshqich talabasi."
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yagilovchi metod
#         Method that renews the student's course"""
#         self.bosqich = bosqich
# talaba1 = Talaba("Davronbek","Atadjanov",2005)   
# # Metodga murojaat etamiz:
# talaba1.set_bosqich(3)
# print(talaba1.get_info())

# # # Umman olganda,xususiyatlarni yangilashda turli usullardan 
# # # foydalanish mumkin.Misol uchun,talabaning bosqichli,odatda,
# # # 1 tadan ko'payib boradi,shuning uchun quyidagicha metod
# # # ham yozishimiz mumkin:

    
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1   
        
        
      
    def set_bosqich(self,yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich
        
    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1    
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    def __repr__(self):
        return f"{self.ism}"
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# Obyektlar o'rtasida munosabat
# Obyektga yo'naltirilgan dasturlarshning afzalligi turli 
# obyektlar o'rtasida o'zaro munosabatlarni oson yo'lga qo'yish
# mumkinligidadir.Keling,yangi Fan degan klass yaratamiz
# va fanimizga talabalar qo'shish uchun add_student() metodini yozamiz:
    
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1 
    
        
    

# E'tibor bering,Fan klass faqatgina yagona nomi degan parametrga ega.
# Qolgan xususiyatlariga esa standart qiymat berilgan:talabalar_soni=0,
# talabalar ro'yxati bo'sh.
# Fanimizga talaba qo'shish uchun add_student() metodini chaqiramiz.
# Bu metod parametr sifatida Talaba klassiga oid obyektni qabul qiladi va 
# uni talabalar ro'yxatiga qo'shadi.Shuningdek,bu metod yangi talaba 
# qo'shilganda talabalar_soni ni bittaga oshirib qo'yadi.
# Keling,boshlanishiga  yangi fan obyektini va bir nechta talabalarni yaratamiz:

matematika = Fan("Oliy matematika")
talaba1 = Talaba("Davronbek","Atadjanov",2005)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2004)



# Talabalarni yangi fanimziga qo'shamiz.
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
# Mana,fanimiz tayyor,talabalar qo'shildi.Keling,endi fan haqida ma'lumotlarni olamiz.
print(matematika.talabalar_soni)

# Fanimizga 3 ta talaba qo'shilibdi.Talabalar haqida ma'lumot olsak bo'ladimi?
print(matematika.talabalar)
# # 
# Talabalarning ism-familiyasi o'rniga qandaydir tushunarsiz ma'lumotlar.
# Aslida, hammasi to'g'ri,yuqorida fanimizga yangi talabalarni obyekt sifatida
# qo'shgan edik,yuqoridagi natija esa matematika.talabalar ro'yxatida Talaba klassiga
# oid 3 ta obyekt borligini ko'rsatmoqda.

# Fanimizga yozilgan  talabalar haqida tuhsunarli ma'lumot olish uchun
# Fan klassiga yangi get_students() metodini qo'shamiz.Bu metod talabalar ichidagi har bir
# talaba obyektiga murojaat etib,get_info() metodi yordamida talabaaning 
# ma'lumotlarini oladi,ro'yxtaga qo'shadi va shu ro'yxatni qaytarib:
# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
   
# # Shu o'rinda Pythonda ro'yxatlar bilan ishlashning qulayliklaridan birini ham
# # ko'rsatib o'tsak.get_students() metodiga e'tibor bersangiz,biz yangi ro'yxat
# # shakllantirishda 1 qator koddan foydalandik:
    
# # [talaba.get_info() for talaba in self.talabalar] 

# # Kodimizni tahlil qilsak,self.talabalar ichidagi har bir
# # talaba uchun get_info() metodini bajar degan ma'no kelib chiqadi.
# # Kodni kvadrat qavslar ichiga olganimiz uchun har bir sikl natijasi 
# # avtomatik ravishda ro'yxatga qo'shib boriladi.
# # Mana,endi metodiga murojaat etib,talabalar haqida ma'lumot olishimiz mumkin:

# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# # Shunday qilib,ikki bir-biriga bog'liq bo'lmagan obyektlar ustida turli munosabatlar o'ranatishimiz mumkin.

# # Nuqta va metod?

# # Pythondagi obyketlarning o'ziga xos xususiyatlaridan biri,
# # obyektning xususiyatiga nuqta orqali murojat qilish mumkin.
# # Misol uchun avval yaratagn talaba1 obyektining ismini bilish uchun
# # talaba1.ism deb yozish kifoya.
# # Bu o'ziga yarasha qulay bo'lsada, bu usuldan foydalanmagan afzal.
# # Sababi, vaqt o'tib klassingiz takomillashishi, uning ba'zi xususiyatlari
# # o'zgarishi, o'chirilishi yoki almashtirilishi mumkin.
# # Shunday holatlarda nuqta orqali murojat qilish siz kutgan natijani bermasligi
# # va dastur xato ishlashiga olib kelishi mumkin. Bunday holatlarning oldini olish uchun esa,
# # obyektning xususiyatlarini metod orqali olishni odat qilish tavsiya qilinadi.
# # Huddi shu kabi, obyektning xususiyatlarini yangilash uchun ham alohida metodlar yozga afzal.
# # Dasturchilar orasida obyektning xususiyatlarini o'zgartiradigan
# # metodlarni set (o'zgartir) so'zi bilan, xususiyatlarni qaytaradigan metodlarni
# # esa get (olish) so'zi bilan boshlash qoida qilib olingan. Masalan: set_name() va get_name() kabi.

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism 
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1 
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
#     def update_bosqich(self):
#         """Tabalaning bosqichlarini 1 taga ko'paytirsh """
#         self.bosqich += 1
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}.{self.bosqich}-bosqich talabasi"
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#     def get_age(self,yil=2023):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil
    
# # Xuddi shu kabi,Fan klasimizning yakuniy ko'rinishi quyidagicha bo'lidi:
# class Fan():
#     """Fan nomli klass"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
#     def add_student(self,talaba):
#         """Fanga talablar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#     def get_name(self):
#         """Fan nomi """
#         return self.nomi
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumotlar"""
#         return [x.get_info for x in self.talablar]
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni

# # Obyektning xususiyatlari va metodlarini ko'rish

# # Obyetklar bilan ishlaganda,o'z-o'zidan,shu obyektga tegishli 
# # xususiyatlar va metodlarni bilish talab qilinadi.Agar 
# # obyekt tegishli bo'lgan klassni o'zimiz yaratgan bo'lsak
# # istalgan payt klassni o'zimiz yaratagan bo'lsak,istalgan payt
# # klass ichini ko'rib olishimiz mumkin.
# # Lekin klass juda ham uzun bo'lsa yoki boshqalar yaratgan klass 
# # haqida ma'lumot olish talab qilinsa,buning bir nechta yo'li bor.

# # dir() funksiyasi
# # dir() funksiyasi yordamida istalgan obyekt yoki klassning metodlarini
# # ko'rib olishimiz mumkin:
# dir(Talaba)

# # Lekin bunda har bir klass bilan keluvchi maxsus dunder metodlar
# # ham chiqib keladi.Dunder metodlar ikki pastki chiziq(__) bilan
# # boshlanadi va maxsus holatlarda uchun saqlab qo'yligan.Biz hozircha
# #  faqat __init__ metodi bilan tanishdik,qolganlari bilan keyingi
# # darslarimizda yana ko'rishamiz.Dunder metodlardan keyin esa biz 
# # murojaat etishimiz mumkin bo'lgan metodlar ro'yati ketgan.

# # Keling,dunder metodlarni tashlab,bizga kerak metodlarni qaytaruvchi 
# # sodda funksiya yozamiz:

    
# def see_methods(klass):
#     return [method for method in dir(klass) if \
#             method.startswith('__') is False]
#     # Funksiya yordamida Talaba klassining metodlarini ko'ramiz:
# print(see_methods(Talaba))

# # Agar dir() funksiyasiga klass emas,obyekt uzatsak,metodlardan tashqari
# # xususiyatlar ham chiqib keladi.
# talaba5 = Talaba("Davronbek","Atadjanov",2005)
# print(see_methods(talaba5))

# # __dict__ metodi

# # Yuqorida zikr qilingan dundor metodlardan biri __dict__
# # metodi bo'lib,bu metod obyektning xususiyatlarini lug'at ko'rinishida qaytaradi:
# print(talaba5.__dict__)

# # Natijadan faqatgina kalitlarni ajratib olsak,obyektning xususiyatlari chiqadi:
# print(talaba5.__dict__.keys())
