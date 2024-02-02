"""
Mavzu:Dunder metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Bo'lim:3-qism

"""
# Obyekt uzunligi

# Pythonda len() funksiyasi yordamida turli 
# obyektlarning uzunligin bilishimiz mumkin,misol 
# uchun,matn,ro'yxat,lug'at,to'plam va hokazo.

matn = 'hello world'
print(len(matn))
sonlar = [1,2,3,4]
print(len(sonlar))

# Pythonda len() funksiyasiga murojaat etganimizda Python
# funksiyaga uzatilgan obyektning ichidagi maxsus __len__
# metodiga murojaat etadi.Agar bu metod mavjud bo'lmasa,
# dasturimiz xato qaytaradi.Misol uchun,bizning Avto klassimizda
# bu metod yozilmagan,shu bois Python TypeError xatosini qaytaradi.
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
        Avto.__num_avto +=1

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)

# len(avto1)

# Keling,endi __len__ metodini qanday ishlatishga ham misol
# keltiraylik.Boshlanishga yangi,AvtoSalon degan klass yaratamiz.
# Bu klassimiz 2 ta xususiyatga ega salon nomi (name) va 
# salondagi mashinalar (avtolar)

class AvtoSalon:
    """AvtoSalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosaloni"
    # Yuqoridagi klassdan yangi obyekt yaratamiz
    
salon1 = AvtoSalon("MaxAvto")
print(salon1)

# AvtoSalon klassimizga __repr__ metodini qo'shganimiz
# uchun natijamiz chiroyli ko'rinishda chiqdi.

# Endi salonga avtomobil qo'shish uchun yangi add_avto()
# metodini yozami.Bu metodimiz Avto klassiga oid obyektlarni
# qabul qilishi kerak.add_avto() ga uzatilgan parametr 
# Avto klassiga tegishli yoki tegishli emasligini tekshirish
# uchun maxsus isinstance() funksiyasidan foydalanamiz.

# Bu funksiya biror obyekt ma'lum klassga tegishli ekanligini
# tekshirish uchun ishlatiladi:
    
isinstance("salom",str)
# True #"salom" bu str
isinstance(9.5,int)
# False # 9.5 int (butun son) emas
isinstance(avto1,Avto)
# True # Avto klassiga tegishli

# add_avto() metodiga qaytaramiz:
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
      


class AvtoSalon:
    """AvtoSalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")
salon1 = AvtoSalon("MaxSalon")
# Metodimizni tekshirib ko'ramiz

# Avto obyektlarini yaratamiz

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Honda","Accord","Oq",2017,40000)

# Yuqoridagi obyektlarni salon1 ga qo'shamiz

salon1.add_avto(avto1,avto2,avto3)


# Navbat __len__ metodiga.Biz bu metod yordamida 
# len() funksiyasi salonimizdagi avtomobillar sonini
# qaytaradigan qilamiz:
    
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
        

class AvtoSalon:
    """AvtoSalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")
    def __len__(self):
        return len(self.avtolar)
salon1 = AvtoSalon("MaxSalon")

# Mana,endi bizning AvtoSalon klassimizga oid obyektlar
# uchun ham len() funksiyasini qo'llasak bo'ladi.

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Honda","Accord","Oq",2017,40000)

# Yuqoridagi obyektlarni salon1 ga qo'shamiz

salon1.add_avto(avto1,avto2,avto3)

print(len(salon1))

