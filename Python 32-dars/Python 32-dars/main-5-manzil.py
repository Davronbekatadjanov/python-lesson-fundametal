"""
Mavzu:OOP,Vorislik va Polimorfizm
Sana:13.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""
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
    
# Obyekt ichida obyekt

# Ba'zida klassimiz xususiyatlar va ular bilan ishlaydigan
# metodlarga to'lib ketishi,bu esa,o'z navbatida,obyektga murojaat
# etishni qiyinlashtirishi mumkin.Shunday holatlarda
# ba'zi xususiyatlarni alohida klass ko'rinishida yozish va keyinchalik
# bu klassdan yaratilgan obyektdan boshqa obyektning xususiyati sifatida 
# foydalanish mumkin.
# Misol uchun,yuqoridagi Shaxs klassimizga yana bir manzil degan xususiyat
# qo'shaylik.Odatda,manzil bir nechta qismlardan iborat bo'ladi(xonadon,ko'cha,
# mahalla,tuman/shahar,viloyat,indeks va hokazo) va ularning har biri uchun 
# Shaxs ichida alohida xususiyat yaratmasdan,alohida Manzil degan
# klassga yuklash maqsadga muvofiq.

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    def get_manzil(self):
        """Manzil ko'rish"""
        manzil = f"{self.viloyat} viloyati,{self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi,{self.uy}-uy"
        return manzil
    
# Talaba klassimizga ham qo'shimcha manzil xususiyatini qo'shamiz:
    
class Talaba(Shaxs):
    """Talaba klass"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabanign xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil 
    def get_idraqam(self):
        """Talabaning ID raqamini qaytardi"""
        return self.idraqam
    def get_bosqich(self):
        """Talabaning o'qish bosqichini qaytaradi"""
        return self.bosqich
    def get_info(self):
        """Talaba haqidagi ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich.ID raqami: {self.idraqam}"
        return info
    
# Keling,endi talaba obyektini qayta yaratamiz.Bu safar talabaning manzili ham
# alohida sifatida talaba ga uzatiladi:
manzil = Manzil(12,"Olmazor","Bog'bon","Samarqand")
talaba = Talaba("Davronbek","Atadjanov","AF0002211",2005,"00001223",manzil)

print(talaba.manzil.get_manzil())
print(talaba.manzil.tuman)
