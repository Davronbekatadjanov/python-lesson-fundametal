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
