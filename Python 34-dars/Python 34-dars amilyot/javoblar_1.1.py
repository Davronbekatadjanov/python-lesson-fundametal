"""
Mavzu:Dunder metodlar
Sana:21.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:1.1-qism amaliyot
"""
class Talaba:
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,bosqich=1):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.bosqich = bosqich
    def __eq__(self,boshqa_talaba):
        """Tenglik"""
        return self.bosqich == boshqa_talaba.bosqich
    
    def __lt__(self,boshqa_talaba):
        """Kichik"""
        return self.bosqich < boshqa_talaba.bosqich
    
    def __le__(self,boshqa_talaba):
        """Kichik yoki teng"""
        return self.bosqich <= boshqa_talaba.bosqich
talaba1 = Talaba("Davronbek","Atadjanov","AD001122",2005)
talaba2 = Talaba("Amirbek","Xudayberganov","AD001122",2004,2)

print(talaba1<talaba2)
print(talaba1<=talaba2)
print(talaba1>talaba2)

