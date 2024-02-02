"""
Mavzu:Inkapsulyatsiya,klassga xos xususiyat va metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Bo'lim:3-qism

"""

# Klassning xususiyatlarini
# Inkapsulyatsiya qilish

# KLassga oid xususiyatlar ham xuddi yuqoridagi kabi nomidan
# avval ikki pastki chiziq qo'shish bilan inkapsulyatsiya qilinadi:

from uuid import uuid4
class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto +=1

# Klassga oid metodlar

# Klasslarning o'ziga xos metodlari ham bo'lishi mumkin.
# Misol uchun yuqoridagi num_avto xususiyatini ko'rish
# uchun alohida metod yozishimiz mumkin. Klassga oid 
# metodlar @classmethod dekoratori bilan boshlanadi va
# obyektga oid metodlardan farqli ravishda self emas 
# cls (class) argumentini qabul qiladi.

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0 
    def __init__(self,make,model,rang,yil,narx,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
# Klass metodlarga klassning nomi orqali murojat qilinadi:
    

avto1 = Avto("GM","Malibu","Qora",2023,35000)
avto2 = Avto("GM","Lacetti","Oq",2023,20000)
avto3 = Avto("Toyota","Camry","Silver",2023,45000)
print(Avto.get_num_avto())

# @classmethod bu maxsus dekorator.Dekoratorlar - o'z ichiga funksiya 
# oluvchi funksiyalar.

