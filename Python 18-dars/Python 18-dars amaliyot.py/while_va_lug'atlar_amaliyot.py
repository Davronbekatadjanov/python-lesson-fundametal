""" 
Mavzu: while,Ro'yxatlar va lug'atlar bilan ishlash amaliyot
Sana:02.02.2023
Muallif:Atadjanov Davronbek
telegram: @atadjanovd
"""
# # Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# # Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# mahsulotlar = []
# print("Foydalanuvchilardan buyurtma qabul qiluvchi dastur.")
# n=1 # mahsulot sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-mahsulotni nomini kiriting:"
#     mahsulot = input(savol)
#     mahsulotlar.append(mahsulot)
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi.")
# print("Mahsulotlar ro'yxati:")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
    
    
# e-bozor uchun mahsulotlar va ularning narxlari lug'atini shakllantiruvchi
# dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narxi)
# kiritishni so'rang.
buyurtmalar = ['olma','anjir','anor','tarvuz']
mahsulotlar ={'olam':20000,
              'anjir':15000,
              'anor':20000,
              'tarvuz':25000}
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh =  mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
        
# Yuqoridagi ikki dasturni jamlaymiz.Foydalanuvchi buyurtmasi ro'yxatidagi 
# har bir mahsulotni e-bozordagi mahsulotlar bilan solishtiring
# (tayyor ro'yxat ishlatishingiz mumkin).Agar e-bozorda mavjud bo'lsa,mahsulot 
# narxini chiqaring,aks holda, "Bizda bu mahsulot yo'q" degan xabarni ko'rsating.
