"""
Mavzu:OOP bilan ishlash yoki obyektlar bilan ishlash
Amaliyot qiyin ammo ishlasha boladi
Sana:10.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""

# Yuqoridagi Shaxs klassidan boshqa turli voris klasslar 
# yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi,
# Mijoz va hokazo)

# Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
# Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.

class Shaxs:
    """Shaxs klassi"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxs xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_ism(self):
        """Shaxsni ismini qaytari"""
        return self.ism
    
    def get_familiya(self):
        """Shaxsni familiyasin qaytardi"""
        return self.familiya
    
    def get_info(self):
        """Shaxs haqida ma'lumot qaytaradi"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaradi"""
        return yil - self.tyil

class Professer(Shaxs):
    """Professer klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam_ish):
        """Professerning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam_ish = idraqam_ish
        
    def get_id_ish(self):
        """Professerning id raqamini qaytaradi"""
        return self.idraqam_ish
    
    def get_info(self): # 
        """Professer haqida ma'lumotlarni qaytaruchi funksiya"""
        
        info = f"{self.ism} {self.familiya},Passport raqam:{self.passport}, "
        info += f"{self.tyil}-yil tug'ilgan,Professerni id raqami:{self.idraqam_ish}"
        return info 
inson = Professer("Davronbek","Atadjanov","AF0011122",2005,"AD001122")
print(inson.get_info())

class Foydalanuvchi(Shaxs):
    """Foydalanuvchi klassi"""
    def __init__(self,ism,familiya,passport,tyil,username,password):
        """Foydalanuchi xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.username = username
        self.password = password
    
    def get_info(self): #
        """Foydalanuvchi haqida ma'lumotlarni qaytaradi"""
        
        info = f"{self.ism} {self.familiya},Passport raqam:{self.passport}, "
        info += f"{self.tyil}-yil tug'ilgan,Foydalanuvchi logini:{self.username},"
        info += f"Foydalanuvchi paroli:{self.password}"
        return info
inson = Foydalanuvchi("Amirbek", "Xudayberganov", "PA001122", 2005, "Amirbek123","Amirbek123d")
print(inson.get_info())

# Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun
# Foydalanuvchi klassidan Admin klassini yarating

# Admin klassiga foydalanuvchida yo'q yangi metodlar 
# yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" 
# degan matn chiqarsin.  

class Admin(Foydalanuvchi):
    """Foydalanuvchi klassi"""
    def __init__(self,ism,familiya,passport,tyil,username,password,admin_keys,):
        """Admin xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil,username,password)
        self.admin_keys = admin_keys
      
    def get_info(self): 
        """Admin haqida ma'lumotlarni qaytaruchi funksiya"""
        
        info = f"{self.ism} {self.familiya},Passport raqam:{self.passport}, "
        info += f"{self.tyil}-yil tug'ilgan,Admin logini:{self.username}, "
        info += f"Adminni paroli:{self.password},Admin kalit so'zi:{self.admin_keys} "
        return info
    def ban_user(self): # Foydalanuvchini bloklandi deb chiqaradigan funksiya
        return f"{self.ism} {self.familiya} foydalanuvchi blokladi"
inson = Admin("Amirbek", "Xudayberganov", "PA001122", 2005, "Amirbek123","Amirbek123d","AmirbekXudayberganov")
print(inson.get_info())

print(inson.ban_user()) 

