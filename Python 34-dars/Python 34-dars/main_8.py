"""
Mavzu:Dunder metodlar
Sana:21.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:8-qism

"""

# Obyektni chaqirish

# Obyektlarni xuddi funksiyalarni chaqirgandek chaqirish
# ham mumkin.Odatda,biror funksiyaga murojaat etganda 
# funksiya nomidan so'ng qavslar ochiladi va yopiladi.
# Agar funksiya argument qabul qilsa,ular qavs ichida beriladi.

print(10)
print(len("Salon"))


# Biz obyektimizga ham shunday imkoniyat qo'shishimiz mumkin.
# Buning uchun maxsus __ceil__ metodidan foydalaniladi.

# Parametrsiz chaqirish

# AvtoSalon klassiga oid obyektlar chaqirilganda salondagi
# avtomobillar ro'yxatini ko'rsatadigan qilaylik.
# Buning uchun avtoSalon klassiga  quyidagi metodni qo'shamiz:



class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
    def __repr__(self):
        return f"Avto:{self.rang} {self.model} {self.make}"

class AvtoSalon:
    """AvtoSalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def __len__(self):
          return len(self.avtolar)
    def __getitem__(self,index):
        return self.avtolar[index]
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")

    def __call__(self):
        return [avto for avto in self.avtolar]
salon1 = AvtoSalon("MaxAvto")
salon2= AvtoSalon("Avto Lider")
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota","Carnila","Silver",2018,45000)
avto4 = Avto("Mazda","6","Qizil",2015,35000)
avto5 = Avto("Volkswagen","Polo","Qora",2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)
salon1.add_avto(avto1,avto2,avto3)
salon2.add_avto(avto4,avto5,avto6)
# Endi obyektni chaqiramiz
print(salon1())
