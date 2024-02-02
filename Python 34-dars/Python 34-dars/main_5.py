"""
Mavzu:Dunder metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Bo'lim:5-qism

"""
# Operatorlarini qayta talqin qilish (overloading)

# Pythonda obyektlar o'rtasida turli arifmetik
# amallarni bajarish mumkin va bu amallar obyektning
# turiga qarab Python tomonidan turlicha talqin qilinadi.
# Masalan:
# Sonlar:
    
x,y = 10,20
print(x+y)
print(x*5)

# Matnlar
t1 = 'hello'
t2 = 'world'
print(t1+t2)
print(t1*5)

# Ro'yxatlar

l1 = [1,2,3]
l2 = [4,5,6]
print(l1+l2)
print(l1*2)

# va hokazolar
# Keling,bu amallarni bizning obyekimizga ham qo'llab ko'ramiz.
# Boshlanishiga 2 ta avtosalon yarataylik va har biriga alohida 
# avtomobillar qo'shaylik.Ishimizni osonlashtirish 
# uchun add_avto() metodimizni ham istagancha parametr qabul 
# qilishga moslab o'zgartiramiz:


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
        return f"{self.name} avtosalon"
    def __len__(self):
        return len(self.avtolar)
    def __getitem__(self,index):
        return self.avtolar[index]
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto ):
                self.avtolar.append(Avto)
            else:
                print("Avto obyektini kiriting")
# Obyektlarni yaratamiz:
    
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

# Mavzuga qaytamiz.Operatorlarni qayta taqin etish.
# Keling,boshlanishiga ikki obyektni qo'shib ko'ramiz:
    
# print(salon1+salon2)

# Demak,bu ikki obyektni qo'shib bo'lmas ekan.Biz obyekt egasi 
# sifatida qo'shish operatorii o'zimiz istagancha taqin 
# etishimiz mumkin.Misol uchun,AvtoSalon obyektiga boshqa AvtoSalon
# obyektini qo'shganda yangi AvtoSalon obyektini qaytaraylik va bu yangi
# obyekt avvalgi ikki obyektning avtolariga ega bo'lsin.

