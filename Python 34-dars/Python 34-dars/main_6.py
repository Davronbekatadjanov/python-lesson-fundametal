"""
Mavzu:Dunder metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Bo'lim:6-qism

"""


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
    def __repr__(self):
        return f"Avto:{self.rang} {self.model} {self.make}"
    
class AvtoSalon:
    """AvtoSalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosalon"
    def __len__(self):
        return len(self.avtolar)
    def __getitem__(self,index):
        return self.avtolar[index]
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto ):
                self.avtolar.append(Avto)
            else:
                print("Avto obyektini kiriting")

    def __add__(self,qiymat):
        if isinstance(qiymat, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon

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

    # Qoshish operatorini tekshirib ko'ramiz
salon3  = salon1 + salon2
print(salon3)