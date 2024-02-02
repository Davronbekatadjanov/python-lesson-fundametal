"""
Mavzu:Kutubxonalar
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:1-qism

"""

# Kutubxonlar

# Python dasturlash tili yildan yilga ommalashib
# borishiga sodda va tusharli sintaksis sabab Pythonning
# keng qamrovli kutubxonalar to'plamidir.Ushbu bobda 
# Pythonda dasturlash tilining ichida va tashqi kutubxonasidagi
# ba'zi muhim modullar bilan tanishamiz.

# Kutubxona - boshqalar tarafidan yozilgan tayyor
# funksiyalar,o'zgaruvchilar va obyektlar to'plami.

# Python standart kutubxonasi
# Python dasturlash tili yuzlab tayyor modullar bilan
# o'rnatiladi.Bu modullar jamlanmasi standart kutubxona
# deb ataladi.Ushbu bo'limda standart kutubxonasiga kiruvchi 
# ba'zi modullar bilan tanishamiz.Kutubxonaning to'liq 
# tarkibini esa quyidagi bog'lama orqali ko'rishingiz mumkin:
# https://docs.python.org/3/library/

# datetime - sana va vaqt

# Ushbu modul yordamida Pythonda sanalar bilan ishlaymiz.
# Har qanday moduldan foydalanishdan avval uni import 
# yordamida chaqirib olishimiz kerak:
    # import datetime as dt 
    # Hozirgi vaqt va sanani ko'rish uchun datetime.now() 
    # metodiga murojaat etamiz:
import datetime as dt
hozir = dt.datetime.now()
print(hozir)


# Kurib turganingizdek,natija yil,oy,kun,soat,minut,sekund
# mikrosekund ko'rinishida chiqdi.Biz bu qiymatlarning
# har birini maxsus metodlar yordamida ajratib olishimiz mumkin:
    
# sanani ajratib olish
print(hozir.date())
# vaqtni ajratib olish
print(hozir.time())
# soatni ajratib olish
print(hozir.hour)
# minutni ajratib olish
print(hozir.minute)
# sekundni ajratib olish
print(hozir.second)

# Agar bugungi kunning sanasi talaba qilinsa,datetime moduli 
# ichidagi date.today() metodiga murojaat etamiz:
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")
# Agar biror sanani qo'lda kiritish talaba qilinsa, .data()
# metodiga kerakli sanani(yil,oy,kun ko'rinishida) kiritamiz.
ertaga = dt.date(2023,4,4)
print(f"Ertangi sana: {ertaga}")

# Faqatgina vaqt bilan ishlash uchun .datetime.now().time()
# metodiga murojaat etamiz:
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")
   
# Istalgan vaqtni qo'lda kiritish uchun esa .time() 
# metodiga kerakli vaqtni (soat,minut,sekund ko'rinishida)beramiz:
    
# >>> vaqtkeyin = dt.time(23,45,00)

# Ayirish operatori yordamida sanalar va vaqtlar orasidagi
# farqni hisoblashimiz mumkin:
bugun = dt.date.today()
yangi_yil = dt.date(2023 , 12, 31)
farq = yangi_yil-bugun
print(f"Yangi yilga {farq.days} kun qoldi")
 
# Natija:
    # Yangi yilga 272 kun qoldi
# Xuddi shu kabi ikki vaqt oralig'ini sekundlarda yoki soatlarda 
# ham ko'rishimiz mumkin:
hozir = dt.datetime.now()
futbol = dt.datetime(2023 , 4 , 6,  1, 45,00)
farq = futbol-hozir
sekundlar = farq.seconds 
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")
# Yuqorida sanalar AQSH standartiga  ko'ra yil-oy-kun 
# ko'rinishida chiqyapti.Sanani o'zimizga moslab chiqarish
# uchun .strftime() metodini chaqiramiz va sanani o'zimizga qulay
# formatda chiqaramiz:

# vaqtni millisekundsiz chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat:{vaqt}")
# sanani kun-oy-yil ko'rinshida chiqaramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")
# sanni kun/oy/yil ko'rinishida chiqaramiz
sana_vaqt = hozir.strftime("%d/%m/%Y,%H:%M")
print(sana_vaqt)


# math-matematika funksiyalar

# Bu modul bilan 8.6-bo'linda qisqacha tanishgan edik.
# math o'z ichiga matematikaga oid turli funksiyalar 
# o'zgaruvchilarni oladi.Keling,ularning ba'zilari bilan tanishamiz.

# pi ning qiymati
import math
PI = math.pi
print(f"Pi ning qiymati: {PI}")


# e-natural logarifm asosi
E = math.e
print(f"e ning qiymati: {E}")

# Trigonametriya
# math moduli tarkibida deyarli barcha trigonometrik
# funksiyalar mavjud(cos,sin,tangens,arcos va hokazo);

math.sin(math.pi/2)
math.cos(0)
math.tan(PI)

# Shuningdek,degrees va radians metodlari yordamida
# burchakdan raidanga va , aksincha,konvertatsiya qilishimiz
# ham mumkin:
math.degrees(math.pi/2)
math.radians(90)

# Logarifmlar 
# log() va log10() funksiyalari yordamida natural va o'n asosli
# logarifmlarni hisoblash mumkin:
# natural logarifm
math.log(5)
# 10 asosli logarifm
math.log10(100)

# Sonlarni ysxlitlash
# Sonlarni yaxlitlash uchun Pythonda maxsus round() funksiyasi
# mavjud.
# Bunga qo'shimcha ravishda math moduli ichidagi ceil() funksiyasi
# yordamida berilgan o'nlik sonni keyingi butun songa,
# floor() yordamida esa quyi butun songa yaqinlashtirish
# mumkin:

x = 4.6
print(math.ceil(x))
print(math.floor(x))
    
# Ildiz va daraja

# Berilgan sonning kvadrat ildizini hisoblash uchun sqrt(),
# sonni darajaga oshirish uchun esa pow() funksiyalariga murojaat
# etamiz:

x = 81 
# Kvadrat ildiz
math.sqrt(x)
# Darajaga oshirish
math.pow(x,3) # x ning kubi
math.pow(x,5) # x ning 5-darajasi
math.pow(123,1/3) # 125 dan kub ildiz


# math moduli tarkibida boshqa funksiyalar ham  mavjud.
# Yuqoridagi biz ularning ba'zilari bilan tanishdik.
# Bu modul asosan butun va o'nlik sonlar bilan ishlashga
# mo'ljallangan
# Kompleks sonlar bilan ishlash uchun esa alohida cmath moduli mavjud.

# pprint - chiroyli print
# pprint moduli yordamida turli o'zgaruvchilarni chiroyli
# ko'rinishda konsolga chiqarishimiz mumkin.Bu bizga uzun 
# lug'atlar,JSON fayllar yoki matnlar bilan ishlashda juda asqatadi.


# Misol uchun,avvalgi darslarimizning birida yaratgan bemor.json
# faylini ochamiz va avval print(),keyin pprint() yordamida
# konsolga chiqaramiz:
    

from pprint import pprint
import json 
filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
print(bemor)

pprint(bemor)

