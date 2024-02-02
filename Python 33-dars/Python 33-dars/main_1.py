"""
Mavzu:Inkapsulyatsiya,klassga xos xususiyat va metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
Bo'lim:1-qism
"""  
# Inkapsulyatsiya

# Obyektga yo'naltirigan dasturlashning tayoyillaridan
# biri inkapsulatsiya,ya'ni obyektning xususiyatlariga 
# to'g'ridan to'g'ri(nuqta orqali) murojaat etishni va 
# ularning qiymatini o'zgartirishni taqiqlab qo'yishdir.
# Pythonda bunday yopiq xususiyatlarnng nomi ikki pastki
# chiziq(__)bilan boshlanadi.

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
    
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    
# Yuqoridagi klassni yaratishda __init__ metodi
# ichidagi ikki xususiyatga e'tibor qarating:__km va __id
# Bu ikki xususiyat inkapsulyatsiya qilingan,ya'ni ularga
# tashqaridan to'g'ridan to'g'ri murojaat etib bo'lmaydi.

avto1 = Avto("GM","Malibu","Qora",2023,40000,100000)
# avto1.__km

# Ko'rib turganingizdek, __km xususiyatiga murojaat etishda
# kodimiz AttributeError xatosini qaytadi.
# Inkapsulyatsiya qilingan xususiyatlarni ko'rish
# uchun alohida metodlar yozish maqsadga muvofiq bo'ladi
# (get_kim()) va get_id()

print(f"ID: {avto1.get_id()}")

# Har bir avto uchun noyob (takrorlanmas)ID yaratish
# uchun biz maxsus uuid4() funksiyadan foydalandik.

# Inkapsulyatsiyalangan xususiyatlarni o'zgartish ham metolar
# orqali amalga oshirilishi kerak.Masalan,mashinaning necha
# km yurganini o'zgartirish uchun klassimizga quyidagi metodni 
# qo'shamiz.

class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
    
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            return "Mashina km kamaytitib bo'lmaydi"
avto1 = Avto("GM","Malibu","Qora",2023,40000,100000)

avto1.add_km(1500)
print(avto1.get_km())

# Inkapsulyatsiyaning maqsadi obyektning ma'lum 
# xususiyatlarini tashqi ta'sirdan himoya qilish.
# Misol uchun yuqoridagi misolimizda mashinaning qancha
# yurganini faqat musbat tarafga o'zgartirish mumkin,
# noyob ID raqamini esa umuman o'zgartirib bo'lmaydi

