"""
Mavzu:OOP,Vorislik va Polimorfizm
Amaliyot 
Sana:13.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""
# Talaba klassiga yana bir fanlar degan xususiyat qo'shing
# Bu xususiyat parametr sifatida uzatilmasin va obyetk yaratilganida 
# bo'sh ro'yxatdan ibora bo'lsin (self.fanlar = []).
class Talaba():
    """Talaba klassi"""
    def __init__(self,ism,familiya,tyil,passport):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.bosqich = 1
        self.fanlar = []
        
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def fanga_yozil(self,fan):
          self.fanlar.append(fan)
    def get_fanlar(self):
        return self.fanlar
    def get_info(self):
        # info = f"{self.ism} {self.familiya},Yoshi:{self.yosh} "
        return f"{self.ism} {self.familiya}, {self.yosh} yoshda, "
    def remove_fan(self, fans):
            if fans in self.fanlar:
                self.fanlar.remove(fans)
            else:
                print("Siz bu fanga yozilmagansiz")
   
class Fan:
    """Fan klassi"""
    def __init__(self,nomi):
        """Fan xususiyatlari"""
        self.nomi = nomi
    def  get_fanlar(self):
        return [fans.get_fanlar() for fans in self.fanlar]
    def __repr__(self):
        return f"{self.nomi}"

talaba1 = Talaba("Davronbek","Atadjanov",18,"AD00111122")
talaba2 = Talaba("Amirbek","Xudaberganov",18,"AD111122")


m = Fan("Matematika")
f = Fan("Fizika")
talaba2.fanga_yozil(f)
talaba1.fanga_yozil(m)
talaba1.fanga_yozil(f)
print(talaba1.get_fanlar())
print(talaba2.get_fanlar())
# print(talaba1.remove_fan(m))
print(talaba1.get_fanlar())
















# # Tog'risi buni xori xato ekan


    
# class Fan:
    
#     """Fan kssi"""
#     def __init__(self,nomi,ustoz):
#         self.nomi = nomi
#         self.ustoz = ustoz
#     def get_fan(self):
#         return f"Fani nomi:{self.nomi} ustoz: {self.ustoz}"
    
# class Talaba:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,yosh,talaba_id,fan):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.talaba_id = talaba_id
#         self.fanlar = []
#         self.fan = fan
        
#     def fanga_yozil(self,fan):
#         self.fanlar.append(fan)

# fan = Fan("Matematika","Yuldashev Aybek")
# 
# talaba.fanga_yozil(fan)

# print(f"{talaba.get_info()},{talaba.fan.get_fan()}")
# print(fan.remove_fan())