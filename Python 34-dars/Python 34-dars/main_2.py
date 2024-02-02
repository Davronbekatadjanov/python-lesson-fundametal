"""
Mavzu:Dunder metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Bo'lim:2-qism

"""

# Obyektlarni taqqoslash

# Taqqoshlash operatorlari yordamida biz turli obyektlarni
# solishtirishimiz mumkin.Taqqoslash natijasi mantiqiy 
# qiymat (True yoki False) ko'rinishda bo'ladi

x,y = 5,10
print(x>y)

# Keling,endi Avto klassidna 2ta obyekt yaratamiz va ularni
# taqqoslab ko'ramiz:
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
        
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# print(avto1>avto2)

# Xatolik.Demak,bu ikki obyektni solishtirib bo'lmas ekan.
# Biz taqqoslash operatorlariga murojaat etganimizda Python
# obyektlar ichida taqqoslash uchun maxsus metodlarni qidiradi,
# agar metodlar topilmasa,yuridagi kabi TypeError
# qaytaradi.

# Ikki obyektni taqqoslash,uchun yoqridagi obyektlardan yarmi uchun 
# metodlar yozishimiz kifoya,masalan,x<y uchun metod yozsak,
# x> metodini yozishimiz shart emas yoki __le__ metodi __ge__
# metodini ham o'z ichiga oladi va hokazo.

# Tushunarli bo'lish uchun Avto klassiga obyektlarni
# solishtirish uchun metod yozamiz.Deylik,biz obyektlarni narxi
# bo'yicha solishtirmoqchimiz,unda klassimizga quyidagi 
# metodlarni qo'shamiz (klassni to'liq yozmadik,faqat qo'shilgan
# metodlarni keltiramiz):
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
    

    def __eq__(self,boshqa_avto):
        """Tenglik"""
        return self.narx == boshqa_avto.narx
    
    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narx<boshqa_avto.narx
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.narx<=boshqa_avto.narx
# Kodimizga e'tibor qilsangiz,biz tenglik(__eq__) yoki 
# kichiklikni(__lt__) tekshirmoqchi bo'lganimizda avtoning
# aynan narxi bo'yicha solishtiramiz (self.narx == boshqa_avto.narx)
# Mana,endi avtolarni solishrisak bo'ladi.


avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)

print(avto1>avto2)

avto3 = Avto("Honda","Accord","Oq",2017,40000)
print(avto1==avto3)


