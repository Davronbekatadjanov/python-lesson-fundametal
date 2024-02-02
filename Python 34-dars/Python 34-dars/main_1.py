"""
Mavzu:Dunder metodlar
Sana:14.03.2023
Muallif:Atadjanov
telegram:@atadjanovd

Bo'lim:1-qism

"""

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
        Avto.__num_avto +=1

# Pythonda obyektlar bilan ishlashni yanada qulay qilish uchun 
# bir nechta maxsus metodlar bor.Bu metodlarning nomi 
# ikki pastki chiziq bilan yozilgani uchun double underscore
# (ikki pastki chiziq) yoki qisqa qilib dunder metodlar  deb ataladi.
# Dunder metodlar yordamida obyektlarga qo'shimcha qulayliklar va 
# vazifalar qo'shishimiz mumkin.
# Klass yoki obyektga oid dunder metodlar ro'xyatini ko'rish
# uchun dir() funksiyasidan foydalanamiz.

dir(Avto)

# Dunder metodlarida biz __init__ metodi bilan tanishdik.
# Bu metod klassdan obyekt yaratishda chaqiriladi va obyektnig 
# xususiyatlarini belgilaydi.Ushbu darsimizda esa maxsus metodlarning
# ba'zilari bilan tanishamiz.

# Obyekt haqida ma'lumot 

# Obyektga print() yoki str() orqali murojaat etilganda 
# obyekt haqida tushunarli ma'lumot qaytarish uchun __repr__
# va _str__ metodlaridan fodalanamiz.Tushunarli bo'lishi
# uchun avvalgi darsimizdagi Avto klassiga qaytamiz.

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narx = narx
        self.__km = km
        Avto.__num_avto +=1

# Yuqoridagi klassdan yangi obyekt yaratamiz va obyekt haqida
# ma'lumot olish uchun print() funksiyasini chaqiramiz

avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1) # obyekt haqida ma'lumot

# Qandaydir tushanarsiz ma'lumot.Ekrandagi natijadan biz
# faqat avto1 obyektimiz Avto klassiga tegishli ekanini 
# ko'ramiz.Qanday qilib uning o'ringa obyekt haqida
# mazmunli ma'lumot olishimiz mumkin?
# Gap shundaki,biz har gal obyektga print() (yoki str()yoki 
# repr())oraqli murojaat etaginimizda Python obyekt ichida
# __str__ yoki __repr__ metodlariga murojaat etadi.
# Agar biz bu metodlarni yozmagan bo'sak,yuqoridagi kabi umumiy
# ma'lumot qaytaradi.

# Biz ushbu metodlarni yangidan yozib, biz istagan 
# ma'lumotni qayataradian qilishimiz mumkin. Odatda,
# yuqoridagi ikki metoddan birini yozish kifoya.
# Odatda, __repr__ umumiyorq, __str__ esa batafsilroq
# ma'lumot olish uchun ishlatiladi.
# Ikkalasidan birini tanlaganda, __repr__ metodiga
# yon bosiladi, sababi bu metod print(), str() va 
# repr() funksiyalarining hammasi bilan ishlaydi. 
# Keling biz ham yuoqirdagi klassimizga __repr__ 
# metodini qo'shamiz:
    
class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx):
        """Avtomobil xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        Avto.__num_avto += 1
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto:{self.rang} {self.make} {self.model}"
    
# Qaytadan print() funksiyasini chaqiramiz

avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1) # obyekt haqida ma'lumot

# Mana,endi natijamiz ancha tushanarli ko'rinishda chiqdi.