"""
Mavzu:Fayllar bilan ishlash
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:3-qism

"""

# Papka ichidagi fayllarni ochish

# Agar siz ochayotgan fayl dasturimiz bilan bir papkada emas, 
# shu papka ichidagi papkada joylashgan boʻlsa, fayl nomidan 
# avval papka nomi yoziladi:

    
# faylnomi = 'Python 35-dars/Python 35-dars/pi.txt'
# with open(faylnomi) as fayl:
#     pi = fayl.read()

# Agar papkalar bir nechta qavat bo'lsa,fayl nomini va 
# ungacha bo'lgan papkalarni alohida yozib olgan afazal:

faylnomi = 'D:/Python dasturlash asoslari/Python 35-dars/Python 35-dars/pi.txt'
with open(faylnomi) as fayl:
    pi = fayl.read()
print(pi)
# Windowsda papkalar orasida "\" belgisi ishlatilsada, Pythonda "/" 
# belgisini ishlataveramiz. Agar \ belgisini ishlatishni istasangiz, 
# bu belgini 2 marta yozing: C:\\python\\darslar\\data

 