"""
Mavzu:Inkapsulyatsiya,klassga xos xususiyat va metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Amaliyot 1-qism
"""

# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga
# yopiq xususiyatlar qo'shig va ularning qiymatini ko'rsatuvchi
# va o'zargartiruvchi metodlar yarting
class Talaba():
    """Talaba klassi"""
    def __init__(self,ism,familiya,tyil,passport,bosqich = 1):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__bosqich = bosqich
    def get_bosqich(self):
        return self.__bosqich
    def add_bosqich(self,bosqich):
        """Talabaning kursini  qo'shish"""
        if bosqich>=0:
            self.__bosqich += bosqich
        else:
            return "Talabaning  kursini kamaytitib bo'lmaydi"
        
talaba = Talaba("Davronbek","Atadjanov",2005,"AD001122")
talaba.add_bosqich(3)
print(talaba.get_bosqich())


class Shaxs:
    """Shaxs klassi"""  
    def __init__(self,ism,familiya,passport,yosh):
        """Shaxs xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.__yosh = yosh
    def get_yosh(self):
        return self.__yosh
    def add_yosh(self,yosh):
        """Shaxsning yoshini qo'shish"""
        if yosh>=0:
            self.__yosh += yosh
        else:
            print("Shaxs yoshini kamaytirib bolmaydi")

shaxs1 = Shaxs("Davronbek","Atadjanov","AD001122",18)
shaxs1.add_yosh(4)
print(shaxs1.get_yosh())
