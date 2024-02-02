"""
Mavzu:Inkapsulyatsiya,klassga xos xususiyat va metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Bo'lim:2-qism

"""

# Klassning xususiaytlari va metodlari

# Klassdan yaratilgan har bir obyektning xususiyatlarini
# kass ichidagi def __init__() metodi yordamida beryapmiz.
# Bu metod qanday ishlaydi?Biz har gal klassga murojaat
# etganimizda klass aynan shu __init__ metodini tushiradi
# va biz bergan xususiyatlar bilan yangi obyekt yaratadi.

# Pythonda xususiyatlarni nafaqat obyektga,balki tog'ridan
# klassga ham yuklash imkoniyati mavjud.Bunida klassning 
# xususiyatiga berilgan qiymat mavjud.Bunda klassning 
# xususiyatiga berilgan qiymat barcha obyektlar uchun umumiy
# bo'ladi. Bu xususiyat bir obyekt orqali o'zgartirilganda
# shu klassga oid barcha obeyktlarda ham uning qiymati o'zgaradi
# Klassga oid xususiyatlar def __init__() metodidan avval
# e'lon qilinadi.
# Keling,tushunarli bo'lishi uchun quyidagi misolni keltiramiz:

from uuid import uuid4
class Avto:
    num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.num_avto +=1
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
# Kodni tahlil etamiz:
# 1-qatorda Avto klassini e'lon qildik.
# 3-qatorda Avto klassiga oid bo'lgan xususiyat num_avto
# yaratdik va unga 0 qimatin berdik.

# Keyingi qatorlarda __init__ metodi yordamida klassdan 
# yaratiladigan obyektlarning xususiyatlarini e'lon 
# qildik va har gal bu metodga murojaat qilib qo'ydik:
# Avto.num_sum += 1
# Yuqoridagi usul bilan endi dastur davomida Avto klassidan
# jami nechta obyekt yaratilganini kuzatib borishimiz mumkin
# bo'ladi.Bunda num_avto o'zgaruvchisiga istalgan obyekt orqali
# yoki klass nomi orqali murojaat etish mumkin:
    
avto1 = Avto("GM","Malibu","Qora",2023,35000)
avto2 = Avto("GM","Lacetti","Oq",2023,20000)
print(avto1.num_avto)
avto3 = Avto("Toyota","Camry","Silver",2023,45000)
print(Avto.num_avto)

