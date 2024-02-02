"""
Mavzu: Moslashuvchan funkiya (*argss,**kwargs)
Sana:07.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# def avto_info(kompaniya,model,rangi,korobka,yili,narxi=None):
#   avto = {
#     'kompaniya':kompaniya,
#     'model':model,
#     'rang':rangi,
#     'korobka':korobka,
#     'yili':yili,
#     'narx':narxi
#   }
#   return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info(',GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar=[avto1,avto2]
# print('Onlayn bozordagi mavjud avtomashinalar: ')
# for avto in avtolar:
#   if avto['narx']:
#       narx = avto['narx']
#   else:
#       narx = "Noma'lum"
#   print(f"{avto['rang']} {avto['model']}.Narxi:{narx}")

# # Moslashuvchan funksiya (*args,**kwargs)
# # Agar funksiyagiz bir nechta argument qabul qilishi kerak bo'lsa-yu,lekin siz argumentlar sonini aniq bilmasangiz,
# # Pythonda istalgancha qiymat qabul qiluvchi funksiya yaratish imkoniyat bor.

# # *args usuli

# # Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa va parametrlar yagona qiymatlar,
# # ko'rishida uzatilsa,funksiya yaratishda argumentdan avval yuduzcha qo'yildi (*arguments).
# # Quyidagi misolni ko'ryalik summ() nomli funksiyamiz istalgancha sonlarni qabul qilib oladi
# # va ularning yig'indisini hisoblaydi:


# def summa(*sonalar):
#     """Kiritilgan sonalar yig'idisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonalar:
#         yigindi += son
#     return yigindi

# # Bu funksiyani istalgancha parametr bilan chiqarish mumkin:

# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))

# # *args() usulida uzatilgan parametrlar (bir dona bo'lsa ham) funksiya  ichida o'zgarmas ro'yxatga (tuple) joylanadi.
# # Bundan kelib chiqib yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin

# def summa(*sonlar):
#     """Kitilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     return sum(sonlar)

# Funksiyamizni ishlatib ko'ramiz.

# print(summa(4,5))

# # # Agar funksiya bir nechta argument qabul qilsa, *args argumenti doim oxirida yoziladi:
# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     return x+y+sum(sonlar)
# # Yuqoridagi funksiyamiz 2 ta majburiy parametr qabul qiladi(x va y), undan keyingi qiymatlar esa ixtiyoriy bo'ladi:
# # print(2) Bitta qiymat bersangiz typeError xatolik beradi.
# print(summa(9,10,21))
# print(summa(-10,10))

# # **kwargs usuli
# # Agar funksiyaga kalit-qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa va bunday parametrlar soni noma'lum bo'lsa, argument oldida ikkita yuduzcha qo'yiladi(**kwargs).

# # **kwargs - keyword arguments (kalit so'zlar argumentlar).
def avto_info(kompaniya,model,**malumotlar):
     """Avto haqidagi ma'lumotlarni lug'at
       ko'rinishda qaytaruvchi funksiya"""
     malumotlar['kompaniya']=kompaniya,
     malumotlar['model']=model,
     return malumotlar
# Yuqoridagi funksiyamiz kompaniya va model degan ikki qiymatni qabul qiladi, undan keyin esa funksiyaga istalgancha parametr uzatish mumkin.Bunday funksiyaga parametrlar kalit=qiymat ko'rinishda uzatiladi.
# Funksiya ichida avval foydalanuvchi kiritgan qo'shimcha qiymatlardan iborat ma'lumotlar deb nomlangan lug'at shaklantiriladi.Undan keyin esa majburiy parametrlarni lug'atga qo'shamiz.
avto1= avto_info("GM","malubu",rangi='qora',yil=2018)
avto2 = avto_info("Kia","K5",rangi='qizil',narx=35000,yili=2000)
print(avto2)