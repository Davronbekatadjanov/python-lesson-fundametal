"""
Mavzu:OOP,Vorislik va Polimorfizm
Sana:13.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""


# Voris klassga xos xususiyatlar va metodlar

# Hozirgi ko'rinishda Talaba va Shaxs klasslari o'rtasida hech
# qaday farq yo'q.Keling,Talaba klassimizga o'ziga xos xususiyatlar
# va metodlar qo'shaylik.Dastavval talabaning bosqichi va ID raqamini 
# xususiyat sifatida qo'shamiz.Bunda ID raqami obyekt yaratilishida parametr
# sifatida uzatiladi,bosqich esa standart qiymatga ega.
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Talaba(Shaxs):
    """Talaba klassi"""""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam 
        self.bosqich = 1
        
# Endi Talaba obyektini yaratishda qo'shimcha ID parametrini ham kiritish talaba qilinadi:

talaba = Talaba("Davronbek","Atadjanov","FA001122",2005,"0001122")

# Navbat bu qiymatlarni qaytaruvchi metodlarga:
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
    def  get_id(self):
        """Talabaning ID raqami """
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
        
# Metodlarni tekshirib ko'ramiz:
talaba = Talaba("Davronbek","Atadjanov","FA001122",2005,"hA0001122")

print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")

print(f"{talaba.get_bosqich()}-bosqich talabasi")

# Shu zayilda yangi klassimizga istalgacha yangi xususiyatlar va
# metodlar qo'shishimiz mumkin.Agar yangi xususiyat yoki 
# metod super klassga ham  aloqador bo'lsa,uni birdan super-klassga 
# qo'shish tavsiya qilinadi.

# Voris klass boshqa klass uchun super-klass  bo'lishi mumkin
