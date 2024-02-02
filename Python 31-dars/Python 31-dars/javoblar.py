"""
Mavzu:OOP bilan ishlash yoki obyektlar bilan ishlash
Amaliyot
Sana:10.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""

# Avto degan yangi klass yarating.Unga avtomobillarga doir bo'lgan
# bir nechta xususiyatlar (model,rangi,korobka,narxi va hokazolar) qo'shing.
# Ayrim xususiyatlarga standart qiymat bering(masalan,koometer=0)

class Avto:
    """Avto nomi klass yaratamiz"""
    def __init__(self,model,rangi,karobka,narxi):
        self.model = model
        self.rangi = rangi
        self.karobka = karobka
        self.narxi = narxi
        self.km = 0
    def get_model(self):
        """Avto modelni qaytaradi"""
        return self.model
    def get_rangi(self):
        """Avto rangini qaytaradi"""
        return self.rangi
    def get_karobka(self):
        """Avto karobkasini qaytaradi"""
        return self.karobka
    def set_km(self,km):
        """ Avto ni yurgan yo'li"""
        self.km = km
    def update_km(self):
        """Avto yurgan yolini kilometrajini yangilab boradi"""
        self.km += 100
# Avto ga oid xususiyatlarini qaytardigan metod yozing
# get_info metodi avto haqida to'liq ma'lumotni  matn ko'rinishida qaytarsin.
# Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing
# update_km() metdoi son qabul qilib olib,avtomobilning yurgan 
# kilometrajini yangilab borsin
    def get_info(self):
        """Avto haqida to'liq ma'lumotlar qaytaradi"""
        return f"Modeli:{self.model} rangi:{self.rangi} Karobka: {self.karobka} Narxi: {self.narxi},{self.km}km-yurgan yo'li"
class Avtosalon():
    """Avtosalon nomi klass yaratamiz:"""
    def __init__(self,salon_name,manzili,sotuvdagi_cars):
        self.salon_name = salon_name
        self.manzili = manzili
        self.sotuvdagi_cars = sotuvdagi_cars
    def get_username(self):
        """Avto salon  nomini qaytaradi"""
        return self.salon_name
    def get_address(self):
        """Avto salon manzili qaytaradi"""
        return self.manzili
    def get_marketplace_cars(self):
        """Avto salondagi mashinalarni qaytaradi"""
        return self.sotuvdagi_cars
    def get_info_cars(self):
        """Avtosalon haqida ma'lumotlarni qaytaradi"""
        return f"Avtosalon nomi:{self.salon_name},Manzili:{self.manzili},Mavjud mashinalar:{self.sotuvdagi_cars}"
avto1 = Avto("GENTRA","QORA","MEXANIKA",20000)
print(avto1.get_info())
print(avto1.get_rangi())
print(avto1.get_karobka())
avto_salon1 = Avtosalon("GM", "Toshkent shahri", "Gentra,Cobalt,Kaptiva,Spark")
print(avto_salon1.get_address())
print(avto_salon1.get_info_cars())

# dir() funksiyasi va __dict__ metodi yordamida o'zingiz yozgan
# obyektlarning xususiyatlari va metodlarini toping.
dir(Avto)    
dir(Avtosalon)
def see_methods(klass):
    return [method for method in dir(klass) if \
            method.startswith('__') is False]
print(see_methods(Avto))
print(see_methods(Avtosalon))

dir(int)
dir(str)
dir(print)
print(see_methods(str))
print(see_methods(int))
print(see_methods(print))

