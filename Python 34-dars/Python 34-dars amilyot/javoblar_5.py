"""
Mavzu:Dunder metodlar
Sana:21.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:5-qism amaliyot
"""

# Fan obyektlarini chaqiriladigan  qiling
# (masalan,fizika() yoki fizika(talaba1)) .
# Bu metodlarni o'zingiz istagandek talqin eting


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
    def __call__(self,*param):
        if param:
            for talaba in param:
                self.add_student(talaba)
        else:
            return [talaba for talaba in self.talabalar]
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

matem = Fan("Oliy matematika")
fizika = Fan("Fizika")
talaba1 = Talaba("Davronbek","Atadjanov",2005)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2004)
talaba4 = Talaba("Hamid","Davlatov",2000)
talaba5 = Talaba("Jamshid","G'aniyev",2003)
talaba6 = Talaba("Botir","Nematov",2004)
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)
fizika.add_student(talaba4)
fizika.add_student(talaba5)
fizika.add_student(talaba6)

talaba7 = Talaba("Vali","Jashidov",2001)
matem(talaba7)
print(matem())
