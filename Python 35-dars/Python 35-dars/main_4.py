"""
Mavzu:Fayllar bilan ishlash
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:4-qism

"""

# Faylni qaytorma-qator o'qish

# Baʻzida faylni toʻliqligicha emas, qatorma-qator oʻqish 
# talab qilinishi mumkin. Masalan, faylda talabalarning ismi 
# yoki kundalik ob-havo maʻlumotlari saqlangdanda va hokazo. 
# Bunday hollarda for tsiklidan foydalanamiz:

filename = 'D:/Python dasturlash asoslari/Python 35-dars/Python 35-dars/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)
        
# Qatorlarni ro'yxat ko'rinishida saqlab olish
# uchun .readlines() metodidan foydalanamiz:
with open(filename) as file:
    talabalar = file.readlines()
print(talabalar)

# E'tibor bering,har bir talaba ismidan so'ng
# qator tashlash belgisi(\n) tushib qolgan
# Biz bu belgilarn .rstrip() metodi yordamida 
# olib tashlashimiz mumkin:
    
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)

