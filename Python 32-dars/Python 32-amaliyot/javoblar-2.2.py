"""
Mavzu:OOP bilan ishlash yoki obyektlar bilan ishlash
Amaliyot oson
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
    def __init__(self, ism, familiya, yosh):
        """Shaxs xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
    
    def get_info(self):
        """Shaxsning ma'lumtolarini qaytaradi"""               
        return f"{self.ism} {self.familiya}, {self.yosh} yoshda"

class Professor(Shaxs):
    """Professor klassi"""
    def __init__(self, ism, familiya, yosh, fanlar):
        """Professorni xususiyatlari"""
        super().__init__(ism, familiya, yosh)
        self.fanlar = fanlar

    def get_info(self):
        """Professorni ma'lumotlarini qaytaradi"""
        return f"{super().get_info()}, professor, o'qitgan fanlari: {self.fanlar}"

inson = Professor("Davronbek","Atadjanov",18,"Matematika,fizika")

print(inson.get_info())


class Foydalanuvchi(Shaxs):
    """Foylanuvchi klassi"""
    def __init__(self, ism, familiya, yosh, email, parol):
        """Foydalanuvchini xususiyatlari"""
        super().__init__(ism, familiya, yosh)
        self.email = email
        self.parol = parol

    def get_info(self):
        """Foydalanuvchi ma'lumotlari"""
        return f"{super().get_info()}, foydalanuvchi email: {self.email},foydalanuvchi paroli:{self.parol}"
inson = Foydalanuvchi("Davronbek","Atadjanov",18,"atadjanovdavronbek@gmail.com","Davronbek")

print(inson.get_info())


class Sotuvchi(Shaxs):
    """Sotuvchi klassi"""
    def __init__(self, ism, familiya, yosh, dokon):
        """Sotuvchini xususiyatlari"""
        super().__init__(ism, familiya, yosh)
        self.dokon = dokon

    def get_info(self):
        """Sotuvchini ma'lumotlarini qaytaradi"""
        return f"{super().get_info()}, sotuvchi do'koni: {self.dokon}"
inson = Sotuvchi("Davronbek","Atadjanov",18,"Sultan Market")
print(inson.get_info())



class Mijoz(Shaxs):
    """Mijoz klassi"""
    def __init__(self, ism, familiya, yosh, hisob):
        """Mijozni xususiyatlari"""
        super().__init__(ism, familiya, yosh)
        self.hisob = hisob

    def get_info(self):
        """Mijozni ma'lumotlarini qaytaradi"""
        return f"{super().get_info()}, mijoz hisobi: {self.hisob}$"
inson = Mijoz("Davronbek","Atadjanov",18,1000)
print(inson.get_info())

# Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun
# Foydalanuvchi klassidan Admin klassini yarating

# Admin klassiga foydalanuvchida yo'q yangi metodlar 
# yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" 
# degan matn chiqarsin.  

class Admin(Foydalanuvchi):
    """Admin klassi"""
    def __init__(self, ism, familiya, yosh, email, parol, huquqlar):
        """Adminni xususiyatlari"""
        super().__init__(ism, familiya, yosh, email, parol)
        self.huquqlar = huquqlar

    def get_info(self):
        """Adminni ma'lumotlarini qaytaradi"""
        return f"{super().get_info()}, admin, huquqlar: {self.huquqlar}"
    
    def ban_user(self): 
        """Admin bloklagan foydalanuchilarni qaytaradi"""
        return f"{self.ism} {self.familiya} foydalanuvchi blokladi"

inson = Admin("Davronbek","Atadjanov",18,"atadjanovdavronbek@gmail.com","Davronbek","Foydalanuvchilarni bloklash")
print(inson.get_info())
print(inson.ban_user()) 
