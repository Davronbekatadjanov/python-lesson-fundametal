"""
Mavzu:Inkapsulyatsiya,klassga xos xususiyat va metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Amaliyot 2-qism
"""
# Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan 
# klassga oid xususiyatlar qo'shing
# Klassga oid xususiyatlar bilan ishlash uchun maxsus@ classmethod
# lar yozing


class Talaba():
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self,ism,familiya,tyil,passport,bosqich = 1):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__bosqich = bosqich
        Talaba.__talabalar_soni += 1
        
    @classmethod 
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
talaba1 = Talaba("Davronbek","Atadjanov",2005,"AD001122")
talaba2 = Talaba("Amirbek","Xudayberganov",2005,"AF001122")
talaba3 = Talaba("Sandibek",'Kenjaliyev',2005,"AH002233")
print(f"Talabalar soni {Talaba.get_talabalar_soni()}")


class Shaxs:
    """Shaxs klassi"""
    __odamlar_soni = 0    
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxs xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni += 1
    @classmethod 
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
shaxs1 = Shaxs("Davronbek","Atadjanov",2005,"AD001122")
shaxs2 = Shaxs("Amirbek","Xudayberganov",2005,"AF001122")
shaxs3 = Shaxs("Sandibek",'Kenjaliyev',2005,"AH002233")
print(f"Odamlar soni {Shaxs.get_odamlar_soni()}")
        