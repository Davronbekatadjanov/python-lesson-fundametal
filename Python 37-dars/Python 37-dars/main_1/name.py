"""
Mavzu:Funksiyalarni tekshirish
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:1-qism

"""

# Dasturni tekshirish


# Dastur davomida yangi funksiya yoki klass yozar 
# ekanmiz, ularni to'g'ri ishlashini ham tekshirishimiz 
# tabiiy. Kodni tekshirish, kelajakda dasturimiz xato 
# ishlashining oldini oladi. Odatda, funksiya va 
# klasslarni tekshirish uchun alohida test dasturlar 
# yozishimiz mumkin. Bunday dasturlar funksiyaga turli 
# parametrlar orqali murojat qilib, undan qaytgan 
# qiymatlar to'g'ri yoki xato ekanini tekshiradi. 

# Pythonda bu jarayonni osonlashtirish uchun maxsus 
# unittest moduli mavjud. unittest yordamida alohida
# funksiya, obyekt yoki butun boshli modulni ham 
# tekshirshimiz mumkin. Lekin, tavsiya qilingan 
# usuli bu testni dastavval kichik qismlardan 
# boshlab, kengaytirib borish. 

# Funksiyani tekshirish

# Boshlanishiga sodda funksiya yozamiz va uni tekshiramizni
# o'rganamiz.Quyidagi funksiya foydalanuvchi ismi va 
# familiyasini qabul qiladi,ism-familiyani jamlab qaytaradi.

def get_full_name(ism,familiya,otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

# Funksiyani tekshiramiz:
    

# Keling endi shu funksiyamizni tekshirish uchun dastur yozamiz.
# Bu yerda ikki narsaga ahamiyat beramiz: avvalo funksiyamizni 
# alohida modulda saqlaymiz (name.py), ikkinchidan test 
# dasturimizni ham alohida modulda yozamiz va unga ham 
# tushunarli nom beramiz (masalan, name_test.py).
# Test faylimizning (name_test.py) tarkibi quyidagicha bo'ladi:
    
    
    