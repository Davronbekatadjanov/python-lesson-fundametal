"""
Mavzu: Funksiyalar So'ngso'z amaliyot
Sana:04.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Berilgan soni 10 ga ko'paytiruchi lambda funksiya yozing.
# b_son = lambda x : x *10
# print(b_son(10))

# # Ikki son qabul qilib,ularning yig'idisini qataruvchi lambda funksiya yozing.
# yigindi_son = lambda x,y : x+y
# print(yigindi_son(5,6))

# # random moduli ichidagi sample funksiyasi yordamida 0 dan 1000 gacha sonlar oralig'idagi tasodifiy 10 ta sonlar ro'yxatini yuzing.
# import random as r

# sonlar = r.sample(range(1001),10) # 0-1000 oralig'ida 10 ta tasodifiy sonlar
# print(sonlar)

# # map() va lambda funksiya yordamida sonlarning kvadratini hisoblang.

# kvadratlar = list(map(lambda x: x*x,sonlar))
# print(kvadratlar)

# # filter() va lambda funksiya yordamida ro'yxatdan toq sonlarni ajaratib oling.
# import random as r
# sonlar = r.sample(range(1001),10)
# toq_sonlar = list(filter(lambda son: son%2!=0,sonlar))

# print(sonlar)
# print(toq_sonlar)

# # Berilgan son tub bo'lsa,True,aks holda Fasle qaytaruvchi funksiya yozing.

# def tubmi(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(tubmi(5))

# # filter() va yuqoridagi funksiya yordamida 1 dan 10000 gacha oraliqdagi tub sonlar ro'yxatini tuzing.
# tub_sonlar = list(filter(tubmi,range(10001)))
# print(tub_sonlar)

import random
def son_topish(x=10):
    print(f"1 dan {x} gacha bolgan sonni o'yladim.Topa olsizmi?")
    tasodifiy_sonlar = random.randint(1,x)
    taxminlar = 0
    while True:
        taxminalar += 1
        taxmin = int(input(">>> "))
        if taxmin<tasodifiy_sonlar:
            print("Xato.Men o'ylagan son bundan kattaroq.Yana urinib ko'ring.")
        elif taxmin>tasodifiy_sonlar:
            print("Xato.Men o'ylagan son bundan kichikroq.Yana urib ko'ring.")
        else:
            break
    print("Tabrilaymiz!.Siz {taxminlar} ta taxmin bilan topdingiz")
son_topish()
