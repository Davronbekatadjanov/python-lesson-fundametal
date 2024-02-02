"""
Mavzu:Funksiya va ro'yxat
Sana:07.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanov

"""
# # Funksiya va ro'yxat
# # Biz avvalgi darslarimizda funksiyaga parametr sifatida yagona qiymat berayotgan edik.
# # Aslida, bu bilan cheklanmasdan,funsiyaga ro'yxat (list) ham berishimiz mumkin.
# # Bunda funksiya ro'yxat qiymatlariga to'g'ridan-to'g'ri murojaat eta oladi.
# # Keling,talabalarni baholaydigan funksiya yozamiz.Funksiyamiz talabalar ro'yxatini qabul qilib oladi,
# # ro'yxatdan har bir talabani sug'urib olib,bahosini kiritishni so'raydi. Talaba ismi va bahosini
# # lug'atga joylab,yakuniy lug'atni foydalanuvchiga qaytaradi.

# def bahola(ismlar):
#   baholar={}
#   while ismlar:
#      ism = ismlar.pop()
#      baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#      baholar[ism]=int(baho)
#   return baholar
# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(baholar)

# # Ro'yxatga o'zgartirish kiritish

# # Funksiyaga ro'yxat uzatganimizda funksiya ro'yxat elementlariga to'g'ridan to'g'ri murojaat eta oladi.
# # Ro'yxatga funksiya ichidsa kiritilgan o'zgartirishlar funksiya tashqasidagi asl ro'yxatga ham ta'sir qiladi.
# # Avvalgi misolimizga qaytaylik.

# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(talabalar)
# # Natija: []

# # Yuqoridagi funksiya unga uzatilgan ro'yxat ichidagi talabalarning ismini .pop() 
# # yordamida sug'irib olgani uchun bizning asl ro'yxatimi ham bo'shab qoldi.E'tibor bering,
# # funksiya tashqarisidagi va ichidagi ro'yxatlar ikki xil nomlangan bo'lsa-da(talabalar va ismlar),
# # ikkilasi ham xotiradagi bitta ro'yxatga bog'langan.

# # Asl ro'yxatga o'zgartirish kiritishning oldini olish

# # Agar funksiya asl ro'yxatga o'zgartirish kiritishni istamasangiz,funksiyaga ro'yxatning o'zini emas,
# # uning nusxasini uztish mumkin.Buning uchun funksiya parametr royxat_nomi[:] ko'rinshida yozish kifoya.
# # Bunda [:] operatori ro'yxatdan nusxa olishni anglatadi:
# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar[:])
# print(talabalar)
