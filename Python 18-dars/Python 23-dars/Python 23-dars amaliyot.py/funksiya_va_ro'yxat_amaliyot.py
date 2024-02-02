"""
Mavzu:Funksiya va ro'yxat amaliyot
Sana:07.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanov

"""
# # Matnlardan iborat ro'yxat qabul qilib,ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgartiruvchi funksiya yozing.
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[1]=matnlar[i].title()

# ismlar = ['ali','vali','hasan','husan']
# katta_harf(ismlar)
# print(ismlar)

# # Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring.
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i].title()
#     return matnlar
# ismlar = ['ali','vali','hasan','husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodida foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

talabalar = ['ali','vali','hasan','husan']

def  bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
baholar = bahola(talabalar)
print(baholar)
print(talabalar)