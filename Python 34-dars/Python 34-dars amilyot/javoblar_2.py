"""
Mavzu:Dunder metodlar
Sana:21.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:2-qism amaliyot
"""

# Fan degan yangi klass yarating.Fan obhektlari
# tarkibida shu fanga yozilgan talabalarning ro'yxati
# saqlansin.Buning uchun Fanga add_studets(),__getitem__
# __setitem__,__len__ kabi metodlarni qo'shing.

class Fan:
    """Fan klassi"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar = []
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
    def __getitem__(self,index):
        return self.talabalar[index]
    def __setitem__(self,index,value):
        if isinstance(value, Talaba):
            self.talabalar[index]=value
    def __len__(self):
        return len(self.talabalar)
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1   
        
            
    def __repr__(self):
        return f"{self.familiya} {self.ism} {2023-self.tyil}-yoshda"

m = Fan("Oliy matematika")
f = Fan("Fizika")
talaba1 = Talaba("Davronbek","Atadjanov",2005)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2004)
talaba4 = Talaba("Hamid","Davlatov",2000)
talaba5 = Talaba("Jamshid","G'aniyev",2003)
talaba6 = Talaba("Botir","Nematov",2004)
m.add_student(talaba1)
m.add_student(talaba2)
m.add_student(talaba3)
f.add_student(talaba4)
f.add_student(talaba5)
f.add_student(talaba6)
print(m.talabalar)
print(f.talabalar[1])


talaba7 = Talaba("Sandibek","Kenjaliyev",2005)
m[1]=talaba7
print(m[1])
print(m.talabalar)

print(len(m))
