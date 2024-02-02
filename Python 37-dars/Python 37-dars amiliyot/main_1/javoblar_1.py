"""
Mavzu:Funksiyalarni tekshirish
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Amaliyot
Bo'lim:1-qism

"""
# Quyidagi funksiyalarni yarating,ulening har biri uchun
# test dasturlar yozing.
# Ushta son qabul qilib,ulardan eng kattasini qaytaruvchi
# funksiya

def eng_katta(*sonlar):
    eng_katta_son = sonlar[0]
    for son in sonlar:
        if son>eng_katta_son:
            eng_katta_son=son
    return eng_katta_son

sonlar = eng_katta(3,6,7)
print(sonlar)

