"""
Mavzu:OOP,Vorislik va Polimorfizm
Sana:13.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""

# Polimorfizm-Super-klass
# Metodlarini qayta yozish

# Voris klassga super-klassdan meros qolgan istalgan metodni qayta
# taqin etish mumkin.Avvalgi misolimizdagi get_info() super metodini ko'zdan kechiraylik
# bu metod talabaning ismi,familiyasi,passport raqami va tug'ilgan yilini qaytaradi.

print(talaba.get_info())

# Keling,get_info() metodi talabaga mos ma'lumotlar qaytarishi uchun Talaba 
# klassi ichida xuddi shu nomli metodni qayta yozamiz:
talaba1 = Talaba("Amirbek","Xudayberganov","FA00022",2005,"0003344")

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya, passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
    def get_id(self):
        """Talabaning ID raqamini qaytaradi"""
        return self.idraqam
    def get_bosqich(self):
        """Talabaning o'qish bosqichini qaytaradi"""
        return self.bosqich
    def get_info(self):
        """Talaba haqida ma'lumotlarni qaytaradi"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich}-bosqich,ID raqami:{self.idraqami}"
        return info
# Metodni tekshirib ko'ramiz:

print(talaba1.get_info())