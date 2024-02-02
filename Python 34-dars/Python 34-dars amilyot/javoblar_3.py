"""
Mavzu:Dunder metodlar
Sana:21.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:3-qism amaliyot
"""
class Fan:
    """Fan klassi"""
    def __init__(self,name):
        self.name = name
        self.talabalar = []
    def add_student(self,*talaba):
        self.talabalar.append(talaba)
    def __add__(self,qiymat):
        if isinstance(qiymat,Talaba):
            self.add_student(qiymat)
        else:
            print(f"Fan ga {type(qiymat)} ni qo'shib bo'lmaydi")
    def __getitem__(self,index):
        return self.talabalar[index]
    def __setitem__(self,index,value):
        if isinstance(value, Talaba):
            self.talabalar[index]=value
    def __len__(self):
        return len(self.talabalar)
    
    
    
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil 
        
    def __repr__(self):
        return f"{self.ism} {self.familiya} {2023-self.tyil}-yoshda"


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

m + talaba6
print(m[:])
print(m.talabalar)

