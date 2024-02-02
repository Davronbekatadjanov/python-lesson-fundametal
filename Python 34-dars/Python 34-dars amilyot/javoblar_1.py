"""
Mavzu:Dunder metodlar
Sana:21.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:1-qism amaliyot
"""

# Avvalgi darslarda yaratilgan obyektlarga (Shaxs,Talaba)
# turli dunder metodlarni qo'shish mashq qiling

    # Obyekt haqida ma'lumot(__repr__)
    # Talabalarni bosqichi bo'yicha solishtirish 
    # (__lt__,__eg__ va hokazo)
class Shaxs:
    """Shaxs klassi"""
    __num_shaxs = 0
    def __init__(self,ism,familiya,passport,yosh):
        self.ism = ism
        self.familiya = familiya 
        self.passport = passport
        self.yosh = yosh
        Shaxs.__num_shaxs +=1 
        
    def __repr__(self,*qiymat):
        return f"{self.familiya} {self.ism} {self.yosh}-yosh"
shaxs1 = Shaxs("Davronbek","Atadjanov","AF001122",18)
print(shaxs1)

