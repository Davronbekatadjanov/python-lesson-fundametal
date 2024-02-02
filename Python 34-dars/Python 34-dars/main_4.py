"""
Mavzu:Dunder metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Bo'lim:4-qism

"""

# Obyekt elementlariga murojaat etish

# Ba'zi obyektlarning (matn,ro'yxat,lug'at va hokazo) 
# elementlariga alohida murojaat etish mumkin.

mevalar = ['olma','anor','uzum']
print(mevalar[0])

# Bizning salonimizda ham 3ta avto bor,ularni ko'rish uchun 
# yuqoridagi kabi element raqami orqali murojaat eta olamizmi?

# salon1[0]
# TypeError: 'AvtoSalon' object is not subscriptable

# Afsuski,yo'q.Ko'rib turganingizdek,bizning obyektimizga 
# bunday murojaat etib bo'lmas ekan.Obyektimizga bu xususiyatni
# qo'shish uchu __getitem__ metodini yozishimiz kerak.

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
    def __repr__(self):
        return f"Avto:{self.rang} {self.model} {self.make}"

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
    def __getitem__(self,index):
        return self.avtolar[index]

# Endi salon1 obyektimizning elementlariga murojaat etilganda
# __getitem__ metodi obyekt ichidagi avtolar ro'yxatidan
# ko'rsatilgan elementni (avtomobilni ) qaytardi.


salon1 = AvtoSalon("MaxSalon")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Honda","Accord","Oq",2017,40000)

salon1.add_avto(avto1,avto2,avto3)
print(salon1[0]) 

print(salon1[2])

print(salon1[:]) # salon1 dagi barcha elementlarni ko'rish

# Keling,obyekt elementlaridan birini o'zgartirib ko'ramiz

avto4 = Avto("Mazda","6","Qizil",2015,35000)
# salon1[0]=avto4
# TypeError: 'AvtoSalon' object does not support item assignment

# Yana xatolik.Gap shundaki.__getitem__ metodi o'z nomi
# bilan (get) element qaytaruvchi metoddir.Biror elementni
# o'zgartirish uchun esa __setitem__ metodini ham qo'shishimiz
# kerak.Bu metodimizga murojaat etilganda ham yangi qiymat
# Avto kassiga oid ekanligini tekshirib olish maqsadga muvofiq bo'ladi.

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
    def __repr__(self):
        return f"Avto:{self.rang} {self.model} {self.make}"

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
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value


salon1 = AvtoSalon("MaxSalon")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Honda","Accord","Oq",2017,40000)
avto4 = Avto("Mazda","6","Qizil",2015,35000)

salon1.add_avto(avto1,avto2,avto3)
# salon1[0]=avto4

# kutilgan natija chiqdi

