class Car:
    """(self,make,year,km=0,price=None)"""    
    def __init__(self,make,model,year,km=0,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
    def set_price(self,price):
        self.price = price
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km = km
        else:
            raise ValueError("Musbat qiymat kiriting!")
    def get_inf0(self):
        info = f"{self.make.upper()} {self.model.title()}, "
        info += f"{self.year}-yil, {self.__km} km yurgan"
        if self.price:
            info += f"Narxi: {self.price}"
        return info
    def get_km(self):
        return self.__km


# Metodlarni teshirish

# Obyektlarimiz bir nechta metodlardan iborat.Ularning
# har biri uchun alohida test yozamiz.Bu metodlarni CarTest
# ichida yozishni unutmang.

# Osonidan boshlaymiz:

# def test_set_price(self):
#     self.avto2.set_price(self.price)
#     self.assertEqual(self.price,self.avto2.price)
# # Endi add_km() metodini tekshiraylik.Bu metodimiz faqatgina
# # musbat qiymat qabul qilshi,manfiy qiymat uzatilganda 
# # ValueError xatosini qaytarishi kerak edi.Shuning uchun
# # metodni test qilishda avval musbat,keyin esa manfiy 
# # qiymat berib ko'ramiz

# def test_add_km(self):
#     #1 Musbat qiymat berib ko'ramiz
#     self.avto1.add_km(self.km)
#     self.asseertEqual(self.km,self.avto.get_km())
#     #2 Manfiy qiymat berib ko'ramiz
#     new_km = -5000
    
#     try :
#         self.avto1.add_km(new_km)
#     except ValueError as error:
#         self.assertEqual(type(error),ValueError)
        
        
# # Navbat get_info() metodiga.Bu metod ham obyektning
# # xususiyatlaridan kelib chiqqan holda 2 xil qiymat 
# # qaytarishi mumkin,demak,testimiz bu ikki holatni hisobga
# # olishi kerak.

# def test_get_info(self):
#     avto1_info = "GM Malibu,2023-yil,0 km yurgan"
#     self.assertEqual(avto1_info,self.avto1.get_info())
#     # avto1 narxi va km o'zgartiramiz
#     self.avto1.set_price(50000)
#     self.avto1.add_km(20000)
#     avto1_info = "GM Malibu,2023-yil,20000 km yurgan,Narxi: 50000"
#     self.assertEqual(avto1_info,self.avto1.get_info())
    
    