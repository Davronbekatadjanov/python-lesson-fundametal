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
        
# Kurib turganingizdek,natija yil,oy,kun,soat,minut,sekund
# mikrosekund ko'rinishida chiqdi.Biz bu qiymatlarning
# har birini maxsus metodlar yordamida ajratib olishimiz mumkin:
    

# Agar bugungi kunning sanasi talaba qilinsa,datetime moduli 
# ichidagi date.today() metodiga murojaat etamiz:
    
# Faqatgina vaqt bilan ishlash uchun .datetime.now().time()
# metodiga murojaat etamiz:
    
# Istalgan vaqtni qo'lda kiritish uchun esa .time() 
# metodiga kerakli vaqtni (soat,minut,sekund ko'rinishida)beramiz:
    
# >>> vaqtkeyin = dt.time(23,45,00)

# Ayirish operatori yordamida sanalar va vaqtlar orasidagi
# farqni hisoblashimiz mumkin:
    
# Natija:
    # Ramazonga 35 kun qoldi
# Xuddi shu kabi ikki vaqt oralig'ini sekundlarda yoki soatlarda 
# ham ko'rishimiz mumkin:
    
# Yuqorida sanalar AQSH standartiga  ko'ra yil-oy-kun 
# ko'rinishida chiqyapti.Sanani o'zimizga moslab chiqarish
# uchun .strftime() metodini chaqiramiz va sanani o'zimizga qulay
# formatda chiqaramiz:
    
# math-matematika funksiyalar

# Bu modul bilan 8.6-bo'linda qisqacha tanishgan edik.
# math o'z ichiga matematikaga oid turli funksiyalar 
# o'zgaruvchilarni oladi.Keling,ularning ba'zilari bilan tanishamiz.

# pi ning qiymati


# e-natural logarifm asosi

# Trigonametriya
# math moduli tarkibida deyarli barcha trigonometrik
# funksiyalar mavjud(cos,sin,tangens,arcos va hokazo);

# Shuningdek,degrees va radians metodlari yordamida
# burchakdan raidanga va , aksincha,konvertatsiya qilishimiz
# ham mumkin:
    
# Logarifmlar 
# log() va log10() funksiyalari yordamida natural va o'n asosli
# logarifmlarni hisoblash mumkin:

# Sonlarni ysxlitlash
# Sonlarni yaxlitlash uchun Pythonda maxsus round() funksiyasi
# mavjud.
# Bunga qo'shimcha ravishda math moduli ichidagi ceil() funksiyasi
# yordamida berilgan o'nlik sonni keyingi butun songa,
# floor() yordamida esa quyi butun songa yaqinlashtirish
# mumkin:
    
# Ildiz va daraja

# Berilgan sonning kvadrat ildizini hisoblash uchun sqrt(),
# sonni darajaga oshirish uchun esa pow() funksiyalariga murojaat
# etamiz:

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
    

