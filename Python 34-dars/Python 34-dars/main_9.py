"""
Mavzu:Dunder metodlar
Sana:21.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:9-qism

"""

# Parametr bilan chaqirish 

# Yuqoridagi salon1 ni parametrsiz chaqirishni ko'rib 
# chiqdik.Endi parametr bilan chaqirishni ham yo'lga 
# qo'yamiz.Bunda yuborilgan parametr yangi avto obyekt
# bo'lsin va bu parametr salondagi avtolar ro'yxatiga
# qo'shilsin.Metodini quyidagicha o'zgartiramiz:

class Avto:
    """Avto klassi"""
    def __init__(self,make,model,rang,yil,narx):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
    def __repr__(self):
        return f"{self.rang} {self.make} {self.model}"
class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)

    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
    
    def add_avto(self,*qiymat):
        for avto in qiymat: 
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")

    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat,Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")

    def __call__(self,*param):
        if param: # agar parametr bo'lsa
            for avto in param:
                self.add_avto(avto)
        else: # agar parametr bo'lmasa
            return [avto for avto in self.avtolar]        
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

# Endi bizning klassimizga ham parametr bilan,ham  
# parametrsiz chaqirsih imkoniyati qo'shildi

avto_new = Avto("Mercedes","E200","Silver",2015,80000)
salon1(avto_new) # Yangi avto qo'shamiz
print(salon1())
# __call__ metodini qanday talqin etish ham sizning ixtiyoringizda

# So'ngso'z

# Ushbu bo'limda biz maxsus metodlarning ba'zilari bilan tanishdik
# Bu metodlarning qulayligi shundaki,siz ularni
# istalgancha talqin etishingiz va har bir obyekt uchun mos
# keladigan qilib yaratishingiz mumkin.Ko'rib turganingizdek,
# dunder metodlar obyektingizning imkoniyatlarini kengatirdi va 
# ularga qo'shimcha vazifalar yuklaydi.

