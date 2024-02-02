"""
Mavzu:To'plamlar amaliyot
Sana:21.01.2023
Maullif:Atadjanov Davronbek
@atadjanovd
"""

# # Uch xil ranglar nomi saqlangan to'plam yarating.
# uch_xil_ranglar = {'sariq','qora','kok'}
# uch_xil_ranglar.add('binafsha')
# print(uch_xil_ranglar)
# uch_xil_ranglar.update(['yashil'])
# print(uch_xil_ranglar)

# # Quyidagi ikki to'plam uchun umumiy elementlarni ajratib olib,yangi to'plam yarating:
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# c = set1|set2
# print(c)

# # Yuqoridagi ikki to'plam orasidagi farqlarni konsolga chiqaring.
# print(set1-set2) # 10 va 20 set1 da bor set2 da yo'q

# # Ikki to'plam orasidagi simmetrik farqni toping.
# print(set1.symmetric_difference(set2))

# # Sizda quyidagi ikki ro'yxat bor:
# bozorlik = ['choy','non','kartoshka','tuxum','sut']
# mahsulotlar = ['non','sut','tuxum','olma','un','tuz']
# # bozorlik - siz sotib olishingiz kerak bo'lgan narsalar:
# # mahsulotlar - do'londagi mavjud mahsulotlar.
# # Sotib olishingiz kerak bo'lgan mahsulotlarning qay biri do'konda bor ekanini alohida ro'yxatga (list) saqlang.
# bozorlik = set(bozorlik)
# mahsulotlar = set(mahsulotlar)
# bor_mahsulotlar = list(mahsulotlar.intersection(bozorlik))
# print(bor_mahsulotlar)
# # Do'konda mavjud bo'lmagan mahsulotlar ro'yxatini
# not_available_m = list(bozorlik.difference(mahsulotlar)) # do'kondagi mavjud bo'lmagan mahsulotlarni chiqarish
# print(not_available_m)
# # Do'kon egasi siz so'ragan mahsulotlarni olib keldi.Mahsulotlar ro'yxatiga yangi mahsulotlarni qo'shing.

# mahsulotlar.add('banan')
# print(mahsulotlar)
