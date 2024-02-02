#super
class Fan:
    def __init__(self,name):
        self.name=name
        
    def fan_nomi(self):
        return self.name
    def __repr__(self):
        return f"{self.name}"
# Sub bu ingliz tilidagi subjectni qisqatrmasi
sub1=Fan('Math')
sub2=Fan('Chemistry')
sub3=Fan("English")


# Quyidagi kodda byear bu birthday year, number 
class Talaba(Fan):
    def __init__(self,ID,name,fam,byear):
        self.fam = name
        self.name = fam
        self.ID = ID
        self.byear = byear
        self.fanlar = [] #Fanlar bu talaba boradigan fanlar ro'yhati
        self.Fan = Fan
    def fanga_yozil(self,Fan):
        self.fanlar.append(Fan)
         
        
        
    def say(self):
        print(f'{self.name} {self.fam},ID: {self.number}.Was born: {self.byear}')
        

    
    def inf(self): #information about subject, the student learn
        return self.fanlar   # [Fan.fannomi(self) for subj in self.fanlar]


        
t1=Talaba('Abdulloh','Akmalov',26,2021)

t1.fanga_yozil(sub1)
t1.fanga_yozil(sub2)
t1.fanga_yozil(sub3)

# t1.inf()=lis1[:]
print(t1.inf())