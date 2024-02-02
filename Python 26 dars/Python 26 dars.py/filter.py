"""
Mavzu: Funksiyalar So'ngso'z
Sana:04.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # filter() funksiyasi

# # Bu funksiya ham argument sifatida ro'yxat va boshqa funksiyani qabul qilib oladi va berilgan ro'xyat elementlarini funksiya yordamida saralaydi.Bunda argument sifatida uzatilgan funksiya mantiqiy qiymat qaytarishi kerak (True yoki False)

# # Keling bunga ham bir misol ko'ramiz: tasodifiy sonalar ro'yxatidan juft sonlarni ajratib oluvchi dastur yozamiz.Dasturimiz 3 qismdan iborat:

# # 1.Avvalo,random modulidagi sample() funksiyasi yodamida 0-99 oralig'idagi 10 ta tasodifiy sonlar ro'yxatini tuzib oldik
# # 2.Berilgan son juft (True) yoki (Fasle) ekeanligini qaytaruvchi funksiya yozdik
# # 3.filter() fuksiyasiga  yangi yaratgan juftmi funksiyasi va tasodifiy sonlar ro'yxatini uztib,yangi juft_sonlar ro'yxatini shakllantridik.

# import random as r
# sonlar = r.sample(range(100),10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar

# def juftmi(x):
#     """x juft bo'lsa True,aks holda False qaytaruvchi funksiya"""
#     return x%2==0

# juft_sonlar=list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)

# Keling endi shu dasturni lambda yordamida yozamiz:
import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)

# Kurib turganingizdek,lambda funksiya yordamida dastur bir muncha qisqaroq chiqadi.Agar juftmi funksiyasi kelajakda shart bo'lmasa,alohida funksiya yaratib o'tirmasdan,bir marttalik lambda funksiyasidan foydalangan afzal.
# Keling endi filter() funksiyasi yordamida matnlarni saralashga ham misollar ko'raylik

# Quyidagi dastur mevalar ro'yxatidan b harfiga boshlanuvchi mevalarni ajratib oladi.Bu yerda biz matnlarga tegishli bo'lgan .startswith() metodidan foydalandik.
# Bu metod,berilgan matn shu harfdan boshlanadimi yoki yo'q tekshiradi va True yoki False qiymat qaytardi.

mevalar = ['olma','anor','anjir','shaftoli',"o'rik",'tarvuz','qovun','banan']
mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)

# Quyidagi dastur esa mevalar ro'yxatidan nomi 5 yoki undan kam harfdan iborat mevlarni saralb oladi.
mevalar2 = list(filter(lambda meva:len(meva)<=5,mevalar))
print(mevalar2)

# Topingchi,quyidagi kod qanday vazifani bajaradi?
mevalar3 = list(filter(lambda meva: (meva.startswith('a') and meva.endwith('r'),mevalar)))
print(mevalar3)

# SO'NGSO'Z
# Ushbu darsimiz bilan biz dasturlash asoslarining katta bir qismiga yakun yasadik, navbat Object Oriented Programming va boshqa katta mavzularga. Lekin, bu mavzularga o'tishdan avval, keyingi darslarimizni bir nechta sodda loyihalar qilishga bag'ishlaymiz.

# E'tiboringiz uchun rahmat