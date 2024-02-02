"""
Mavzu:Class tekshirish
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:1-qism

"""


# Klasslarni tekshirish

# Navbat klaslarni tekshiruvchi test dastrularga 
# Klass to'g'ri bo'lsa,undan yaratilgan obyektlarga
# ham to'g'ri ishlaydi.Keling,boshlanishiga biror klass
# yaratamiz:
  
class Car:
    """(self,make,year,km=0,price=None)"""    
    def __init__(self,make,model,year,km=0,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
    def set_price(self,price):
        self.price = price
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km = km
        else:
            raise ValueError("Musbat qiymat kiriting!")
    def get_inf0(self):
        info = f"{self.make.upper()} {self.model.title()}, "
        info += f"{self.year}-yil, {self.__km} km yurgan"
        if self.price:
            info += f"Narxi: {self.price}"
        return info
    def get_km(self):
        return self.__km
    
# Yuqoridagi klassimiz avtomobil haqida ma'lumotlarni 
# saqlaydi.Klassimizning e'tibor qaratishimiz kerak bo'lgan
# jihatlari:
    # km va price(narx) argumentlariga standart qiymat berilgan;
   
    # __km parametri inkapsulyatsiyalanga(self,__km):
   
    # avtomobil narxini set_price() metodi yordamida yangilash
    # mumkin:

    # add_km() metodi faqat musbat qiymat qabul qiladi.
    
    # Agar manfiy qiymat uzatilsa,raise operatori yordamida
    # ValueError xatosini qaytaradi:
    
    # get_info() metodidan qaytaradigan qiymat avtomobil 
    # narxi bor yoki yo'qligiga qarab turli ko'rnishda bo'lishi 
    # mumkin;
    
    # avtomobil kilometrajini ko'rish uchun get_km() metodiga
    # murojaat etamiz:
    
        
    