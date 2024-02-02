"""
Mavzu: Sting(Matn) amaliyot
Sana:07.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # 1.Pythonda quyidagi o'zgaruvchilarni yarating:
# kocha = "Bog'bon"
# mahalla = "Sag'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"

# # 2.Yuqoridagi o'zgaruvchilarni jamlab,quyidagi ko'rinishda konsulga chiqaring:Bog'bon ko'chasi,Sag'bon mahallasi,Bodomzor tumani,Samarqand viloyati.
# kocha = "Bog'bon"
# mahalla = "Sag'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(f"{kocha}  ko'chasi,  {mahalla}  mahallasi, {tuman} tumani, {viloyat}  viloyati")

# # Yuqoridagi o'zgaruvchilarning (ko'cha,mahalla,tuman,viloyat) qiyomatini foydalanuvchidan so'rang.Va avvalgi mashqni takrorlang.

# print("Iltimos,quyidagi ma'lumotlarni kiriting:")
# kocha = input("Ko'changiz:>>")
# mahalla = input("Mahallangiz:>>")
# tuman = input("Tumaningiz:>>")
# viloyat = input("Viloyatingiz:>>")
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati")
# print(f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# # 4.Yuqoridagi matnni konsulga chiqarishda bir verguldan keyin yangi qatordan yozing.
# print("Iltimos, quyidagi ma'lumotlarni kiriting:")
# kocha = input("Ko'changiz:")
# mahalla = input("Mahallangiz:")
# tuman = input("Tumaningiz:")
# viloyat = input("Viloyatingiz:")
# print(f"{kocha} ko'chasi,\n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati")

# print( kocha + " ko'chasi,\n " + mahalla + " mahallasi,\n " + tuman + " tumani,\n " + viloyat +" viloyati,")

# # 5.Yuqoridagi matnni f-string yordamida yangi,manzil deb nomlangan o'zgaruvchiga yuklang.
# print("Iltimos, quyidagi ma'lumotlarni kiriting:")
# kocha = input("Ko'changiz:")
# mahalla = input("Mahallangiz:")
# tuman = input("Tumaningiz:")
# viloyat = input("Viloyatingiz:")
# manzil = f"{kocha} ko'chasi,\n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati"
# print(manzil)

# # 6.manzil o'zgaruvchisiga biz yuqorida o'rgangan title(), upper(), lower(), capitalize() metodlarini qo'llab ko'ring.
# print("Iltimos, quyidagi ma'lumotlarni kiriting:")
# kocha = input("Ko'changiz:")
# mahalla = input("Mahallangiz:")
# tuman = input("Tumaningiz:")
# viloyat = input("Viloyatingiz:")
# manzil = (f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
# print(manzil.title())
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())
