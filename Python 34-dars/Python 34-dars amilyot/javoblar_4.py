"""
Mavzu:Dunder metodlar
Sana:21.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:4-qism amaliyot
"""

class Fan:
    """Fan klassi"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar = []
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
    def remove_talaba(self,qiymat):
        if qiymat in self.talabalar:
            self.talabalar.remove(qiymat)
        else:
            print("Bu talaba ga yozilmagan")
    def __sub__(self,qiymat):
        if isinstance(qiymat,Talaba):
            self.remove_talaba(qiymat)
        else:
            print(f"Fan ga ni ayirib  bo'lmaydi")

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

m - talaba1
print(m[:])