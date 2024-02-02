"""
Mavzu:OOP,Vorislik va Polimorfizm
Sana:13.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""

# Vorislik va Polimorfizm


# Obyektga yo'naltirilgan dasturlashning qulayliklaridan biri klasslardan
# boshqa klass yaratish imkoniyatidir.Bizga kerak bo'lgan yangi
# klassning avval yaratilgan boshqa klass bilan o'xshashlik joylari
# bo'lsa,bu klassdan voris klass yaratishimiz mumkin.Bunda asl
# klass ota yoki super-klass deb ataladi.Super-klassdan yaratilgan
# voris klass otaning barcha yoki tanlangan xususiyatlari va metodlarini
# meros olish bilan birga o'ziga xos  xususiyat va metodlariga ega bo'ladi.
# Keling,Shaxs klassin yaratamiz,bu klassimiz keyinchalik
# boshqa klasslar uchun super-klass vazifasin bajaradi:
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
inson = Shaxs("Hasan","Alimov","FB001122",1995)
print(f"{inson.get_info()},{inson.get_age(2023)} yoshda.")
