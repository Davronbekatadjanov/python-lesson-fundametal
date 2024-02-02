"""
Mavzu: Moslashuvchan funkiya (*argss,**kwargs) amaliyot
Sana:04.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Istalgan sonlarni qabul qilib,ularning ko'paytmasini qaytrauvchi funkdiya yozing:
# def kopaytmasi(*sonlar):
#     kopaytma =1
#     for son in sonlar:
#         kopaytma *= son

#     return kopaytma
# print(kopaytmasi(1,20))


# def mutiply(*sonlar):
# #     bolinma = 30 # Bu yerda bo'linuvchini   kiritasiz
# #     for son in sonlar:
# #         bolinma /= son
# #     return bolinma
# # print(mutiply(3,10)) # Bu yerga esa bo'luvchini

# # Tabalar haqidagi ma'lumotlarni lug'at ko'rnishida qaytaruvchi funksiya yozing.Talabaning ismi va familiyasi majburiy argument,qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

# def talaba_info(ism,familiya,**malumotlar):
#       """Talaba haqidagi ma'lumotlarni qaytaruvchi funksiya"""
#       malumotlar['ism']=ism,
#       malumotlar['familiya']=familiya,
#       return malumotlar
# talaba1 = talaba_info("Davronbek","Atadjanov",t_yil=2005,manzil="Qoraqolpog'iston")
# talaba2 = talaba_info("Amirbek","Xudayberganov",t_yil=2005,kurs=4)
# print(talaba1)
# print(talaba2)
