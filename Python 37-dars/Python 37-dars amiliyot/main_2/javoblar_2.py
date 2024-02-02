"""
Mavzu:Funksiyalarni tekshirish
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Amaliyot
Bo'lim:2-qism

"""

# Matnlardan iborat ro'yat qabul qilib, ro'yxatdagi 
# har bir matnning birinchi harfini
# katta harfga o'zgatiruvchi funksiya

def get_text(text):
    new_text = []
    for matn in text:
        new_text.append(matn.capitalize())
    return new_text

# text = ['salom','davronbek','banan']
# new_text = get_text(text)
# print(new_text)

