"""
Mavzu:OOP , obyektaga yo'naltirilgan dastrulash yoki Object oriented programming
Sana:10.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""
# # Klasslar
# # Klasslar object oriented dasturlashning poydevorlaridan biridir.
# # Klasslar bizga dasturlashga va dastur elementlariga real hayotdagi buyumlarga(obyektlarga )
# # yondashgandek yondashish imkonini beradi.
# # Klasslar,obyektlar va ularning qanday ishlashini tushungan dasturchi mantiqiy
# # fikrlashda ham kuchli bo'ladi.Mukammal va kompleks muammolarga ham yechimni ko'ra oladi.

# # Pythonda klasslar
# # Klass tushunchasi siz uchun yangi bo'lishi mumkin,lekin biz shu vaqtgacha ulardan
# # doimiy ravishda foydalanib keldik.
# # Keling,x o'zgaruvchi yaratamiz,unga biror qiymat yuklaymiz va type() funksiyasi
# # yordamida uning turini ko'ramiz:

# x = 10
# print(type(x))
# # <class 'int'>
# matn = "Salom"
# print(type(matn))
# # <class 'str'>

# # Ko'ryapmizki, x int klassidagi, matn esa str klassidagi obyektlar ekan.
# # Demak,biz o'zgruvchi yaratgaimizda,aslida,Python int yoki str kalssidan
# # foydalangan holda yangi obyektlar yaratib kelayotgan ekan.
# # Xuddi shu kabi,agar yangi funksiya yaratib,uning ham turini tekshirsak,
# # funksiyamiz fuction klassiga tegishli obyekt bo'lib chiqadi.

# def salom_ber():
#     print("Assalom alaykum")
# print(type(salom_ber))

# # Natija: <class 'function' >
# # Demak,Pythondagi hat qanday o'zgaruchi,funksiya va boshqa elementlar,aslida,obyektlar ekan.

# # Metodlar
# # Har bir obyekt ustida bajarish mumkin bo'lgan funksiyalar bilan kealdi.
# # Bu funksiyalar obyekt ichida yashirin bo'ladi,biz ularga nuqta va funksiya nomi
# #  orqali murojaat etishimiz mumkin.
# # Bunday funksiyalar shu klassga (yoki obyektga) tegishli metodlar deyiladi.
# # Ba'zi metodlar bilan avvalgi darslarimizda tanishdik.Bir klassga tegishli metodlar
# # boshqa klassdagi obyektlar uchun mavjud bo'lmasligi tabiiy.
# # Masalan,matnlar uchun mavjud metodlarni butun yoki o'nlik sonlarga qo'llab bo'lmaydi.

# metn = "salom"
# print(matn.upper())

# # son = 10
# # print(son.lower())
# # AttributeError: 'int' object has no attribute 'lower'

# # Klass yaratish
# # Yangi klass yartish uchun class operatoridan foydalnamiz va klassimizga tushunarli nom beramiz.
# # Esingizda bo'lsa,klass hali obyekt emas,obyekt uchun shablondir.
# # Shuning uchun klass yaratishda mazkur klassdagi obyektlar uchun umumiy bo'lgan xususiyatlar va
# # funksiyalarni o'ylashimiz kerak.
# # Keling,Talaba degan klass yaratamiz:
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

# # Kodimizni tahlil qilamiz:
#   # class Talaba - Talaba nomli klass yaratdik.Klasslarga nom berishda uning
#     # birinchi harfini bosh harfdan boshlash tavsiya etiladi.Agar klass nomi 2
#     # va undan ko'p So'zdan iborat bo'lsa,har bir so'zni bosh harf bilan boshlang.

#   # def __init__(self) - klassga tegishli xususiyatlarni saqlovchi maxsus metod
#     # (funksiya). self so'zi ingliz tilidan "O'zi" deb tarjima qilinadi va
#     # bu klassdan yaratilgan obyektning o'ziga ishora qiladi.Ya'ni keyinchalik biz
#     # obyekt ichidagi metodga murojaat etganimizda shu obyektning o'zi birinchi bo'lib
#     # funksiyaga argument sifatida uzatiladi,obyekt ustida turli amallar bajarish imkonini beradi.

#   # def __init__(self,ism,familiya,tyil) - yaratayotgan klassimizga xos xususiyatlarni
#     # def __init__(self) funksiyasiga argument sifatida uzatamiz.Bizning Talaba klassimiz
#     # ism,familiya va tug'ilgan yilga (tyil) ega bo'ladi.
#   # Keyingi qatorlarda esa self.xususiyat = argument komandasi yordamida uzatilgan argumentlarni
#     # klassning xususiyatlari bilan bog'layapmiz.Bu yerda xususiyat nomi uzatilgan argument nomi bilan
#     # uzatilgan argument nomi bilan mos tushishi shart emas,xususiyatga istalgan nom berishimiz
#     # mumkin (masalan,self.name=ism).

# # def __init__ metodi yozilishida init so'zidan avval va keyin ikki pastki chiziq yoziladi.

# # Klassdan obyekt yaratish
# # Klassimiz tayyor, keling,endi klassimizdan yangi obyekt yaratamiz.
# talaba1 = Talaba("Alijon","Valijon",2000)
# # Mana,talaba1 obyektimiz tayyor.Obyektni yaratish uchun Talaba klassiga murojaat etdik
# # va talabaning ismi,familiyasi va tug'ilgan yilini parametr sifatida uzatdik.

# # Obyektning xususiyatlarini ko'rish
# # Obyekttning xususiyatlarini ko'rish uchun nuqta orqali Murojaat etishimiz mumkin.

# print(talaba1.ism)
# print(talaba1.familiya)

# # Klassdan bir nechta obyektlar yaratish

# # Yuqoridagi klassdan istalgancha obyektlar yaratishimiz mumkin.
# talaba2 = Talaba("Dilshodbek","Soburov",1996)
# talaba3 = Talaba("Sandibek","Kenjaliey",2006)
# talaba4 = Talaba("Amirbek","Davlatov",1985)

# # Bunda har bir obyekt o'zining alohida xususiyatlariga ega bo'ladi.

# print(talaba2.ism)
# print(talaba4.familiya)

# # Klassga metodlar qo'shamiz.
# # Obyektimizning xususiyatlarini aniqlab oldik,keling,
# # endi obyekt bajarishi kerak bo'lgan metodlarni qo'shaylik.

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
        
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}."
#               f"{self.tyil} yilda tug'ilganman.")
        
# # Boshlanishiga klassimizga bitta,tanishtir metodini qo'shdik.
# # Bu metodimiz,ko'rib turganingizdek,
# # bitta self(ya'ni obyektning o'zini ) argumentin qabul qiladi va
# # talaba haqidagi ma'lumotlarni konsolga chiqaradi.

# # Obyektning metodlariga murojaat etamiz.
# # Obyekt ichidagi funksiyaga,ya'ni obyektning metodiga murojaat etamiz:
    
# talaba5 = Talaba("Hasan","Akbarov",2005)
# talaba5.tanishtir()

# # Klassimiz istalgancha metodlarga ega bo'lishi mumkin.
# # Yuqoridagi klassga yana obyekt qo'shamiz:

#     # Kitobdagi kodlar cho'zilib ketmasligi uchun kodning qaytarilgan 
#     # qismini uch yulduzcha *** bilan bildirib ketamiz.
    
# class Talaba :
#     """Talaba nomli klass yaratamiz:"""
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
        
#     def get_name(self):
#         """Talabaning ismini qaytaradi."""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi."""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     # Metodlarni tekshirib ko'ramiz.

# talaba2 = Talaba("Dilshodbek","Soburov",1996)
# print(talaba2.get_fullname())
# print(talaba2.get_lastname())

# # Argument qabul qiluvchi metodlar 

# # Avvalfi misolimizda barcha metodlar faqatgina self parametrini
# # qabul qlyapti.Aslida,boshqa funksiyalar kabi klass ichidagi 
# # metodlar ham argumentlar qabul qilishi mumkin.
# # Yuqoridagi Talaba klssimizga yangi get_age() metodini qo'shamiz.

# class Talaba:
#     """Talaba nomli klass yaratamiz."""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def get_age(self,yil):
#         """Talabaning yoshini qaytaradi."""
#         return yil-self.tyil

# # get_age() metodi obyektning o'zidan tashqari qo'shimcha yil
# # argumentini ham qabul qiladi va talabaning yoshini qaytaradi.

# talaba2 = Talaba("Dilshodbek","Soburov",1996)
# print(talaba2.get_age(2023))

# # pass operatori
# # Pythonda hech qanday vazifani bajarmaydigan pass operatori mavjud.
# # Bu opertordan bo'sh metodlar yaratishda foydalanish mumkin.
# # Misol uchun,siz klassingiz uchun muhim metodlarni bilasiz,
# # lekin metod badani hali tayyor emas.Agar metod badanini bo'sh
# # qoldirsangiz,Pytho indentatitonError xatosini qaytaradi.
# # shunday holatlarda funksiya badaniga pass operatorini qo'yib ketishimiz mumkin:
    
# class User:
#     """User nomli klass yaratamiz"""
#     def __init__(self,name,username,email):
#         """Userning xususiyatlari"""
#         self.name = name
#         self.username = username
#         self.email = email
#     def describe():
#         """Klassimizni badani tayyor bo'lmagani sababli pass oraqli to'ldirib turamiz badanini"""
#         pass
#     def get_email():
#         """Klassimizni badani tayyor bo'lmagani sababli pass oraqli to'ldirib turamiz badanini"""
#         pass
    
# # Yuqoridagi klassimizda describe() va get_email() funksiyalar badani hali tayyor emas,
# # bo'shliqni to'ldirish uchun esa pass operatoridan foydalanganmiz.

# # pass operatori bilan if-else,for,while bloklarini ham vaqtinchalik to'ldirib turish mumkin.

