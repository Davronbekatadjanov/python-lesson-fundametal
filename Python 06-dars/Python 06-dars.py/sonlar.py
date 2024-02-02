"""
Mazvu:Sonlar 
Sana:07.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Integer-Butun sonlar 
# a = 20 # Sonlar musbat 
# b = -30 # manfiy yoki
# c = 0 # 0 ga teng bo'lishi mumkin
# d = a + b 
# print(d)

# # Kvadratning yuzini hisoblaymiz.
# kvadrat_t = 20 # Kvadrat tomoni 20 ga teng 
# kvadrat_yuzi = kvadrat_t**2 # Kvadratni yuzini hisoblaymiz
# print(kvadrat_yuzi)

# # Floats-O'nlik sonlar
# # floats:floating point numbers 

# pi = 3.14159 # O'nlik son(float)
# radius = 10 # butun son (integer)
# diametr = radius*2 
# print("Aylananing uzunligi ", pi*diametr, " ga teng")
# print(f"Aylananing uzunligi {pi*diametr} ga teng")

# # Butun sondan o'nlik songa 
# a = -20
# b = 40
# c = b/a
# print(c) # nyatijada o'nlik son hosil bo'ladi.

# # Shuningdek,butun va o'nlik sonlar o'rtasida har qanday arifmetik amallarning natijasida ham o'nlik son bo'ladi.

# a = 2 # Butun son
# b = 3.0 # o'nlik son
# print(a+b)
# print(a*b)
# print(2*(a+b))

# # Uzun sonlarni kiritish  
# # Uzun sonlarni kiritishda qulaylik uchun raqamlarni pastki chiziq(_) yordamida guruhlash mumkin.Python son tarkibidagi pastki chiziqlarni (_) inobatga olmasdan, uzun sonligicha qabul qiladi.

# aholi = 33_580_000 # aholi soni
# print(f"O'zbekiston aholisi {aholi} dan ortiq")

# # Konstanta 
# # Pythonda konstanta tushunchasi yo'q shuning uchun dasturchilar bunday o'zgaruvchilarning nomini bosh harflar bilan yozishni kelishib olishgan.
# PI = 3.14159 # konstanta 
# radius = 21.2
# diametr = radius*2
# print(f"Aylananing uzunligi {PI*diametr} ga teng")

# # Bir necha o'zgaruvchiga qiymat berish 

# x,y,z = 10,-7.25,-30
# print(f"{x} ga teng, {y} ga teng, {z} ga teng")
# # Yuqoridagi kod x ga 10, y ga -7.25, va z ga -30 qiymatini yuklaydi.
#  # Bu usulda istalgan turdagi o'zgaruvchiga qo'llash mumkin

# yosh,ism = 36,'olimjon'
# print(f"{ism.title()} {yosh} yoshda ")

# # O'zgaruvchilarning turini almashtirish.

# ism = 'Jobir'
# yosh = 36
# xabar = ism() + ' ' + yosh + ' yoshda'
# print(xabar)
# # xatolik berdi chunki
# # Agar xatoni ingliz tilidan tajima qilsak, matn (str) va son(int) ni jamlab bolmaydi degan ma'no
# # Demak bir turdagi matn (string) va son(int,float) turidagi o'zgaruvchilarni qo'shib bo'lmas ekan.
# # Pythonda bir turdagi o'zgaruvchini boshqa turga o'tkazish mumkin,bu ingliz tilida "typecasting" deyiladi.Buning uchun Python maxsus funksiyalar bor,ular bilan tanishamiz. 

# # str() -- int yoki float turidagi sonlarni matn ko'rinishida qaytaradi.
# # in() -- string yoki float ko'rinishidagi qiymatlarni butun son ko'rinishida qaytaradi.Bunda matn butun son ko'rinishida berilishi kerak.
# # float() -- string yoki int ko'rinishdagi qiymatlarni o'nlik son ko'rinishida qaytaradi.

# ism = 'Jobir'
# yosh = 36
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)

# # str(),int() va float() funksiyalari berilgan qiymatni boshqa ko'rinishda qaytaradi,xolos.Bunda asl o'zgaruvchining turi o'zgarmaydi qoladi.

# # O'zgaruvchi turini tekshirish

# ism = 'Jobir'
# yosh = 36
# print(type(ism))
# print(type(yosh))
# # Ko'rib turganingizdek, ism nomli o'zgaruvchi str, ya'ni matn,yosh esa int, son turida ekan.

# # Input() va sonlar

# # 1 fodalanuvchining tug'ilgan yilini so'raymiz 
# t_yil = input("Tug'ilgan yilingizni kiriting:>>")
# # 2 foydalanuvchi yoshini hisoblaymiz
# yosh = 2023 - t_yil 
# # 3 foydalanuvchi yoshini konsulga chiqaramiz 
# print("Siz " + (yosh) + ' yoshda ekansiz') 

# # Kutilgan natijani o'rniga xatolik.Lekin xato qayerd? Dastur tug'ilgan yilimni so'radi.men 2005 deb kiritdim, shu zahoti xato ro'y berdi va dastur to'xtadi.Xabar tarjima qilasak,son (int) va matn (str) o'rtasida ayitish (-) amalini bajarib bo'lmaydi degan ma'no chiqadi.abs
# # Gap shundaki, input() fuksiyasi har qanday kiritilgan qiymatni matn ko'rinishida qabul qiladi ( garchi biz son kiritgan bo'sak ham).Keling, konsulga t_yil degan o'zgaruvchining turini tekshirib ko'ramiz.
# # t_yil str chiqdi konsulda 
# # ko'rib turganingizdek,t_yil o'zgaruvchi saqalayotgan qiymat str, ya'ni matn ekan.Kodimizning 2-va 6-qatorlani o'zgartiramiz.

# # 1 foydalanuvchining tug'ilgan yilini so'raymiz
# t_yil = int(input("Tug'ilgan yilingizni kiriting:>>"))
# # 2 foydalanuvchini yoshini hisoblaymiz 
# yosh = 2023 - t_yil 
# # 3 foydalanuvchi yoshini konsulga chiqaramiz
# print("Siz " + str(yosh) + " yoshda ekansiz")
# print(f"Siz {str(yosh)}yoshda ekansiz")

# # Yuqoridagi kodning 2 qatoriga e'tibor bersangiz,biz ikki funksiyani bir-biriga joylab yozdik:int(input()).Aslida,ularni ajratib ham yozishimiz mumkin edi:

# # 1 foydalanuvchi tug'ilgan yilini so'raymiz
# t_yil = input("Tug'ilgan yilingizni kiriting:>>")
# # 2 t_yil o'zgaruvchini int() ga aylatiramiz: 
# t_yil = int(t_yil)
# # 3 foydanaluvchini yoshini hisoblaymiz
# yosh = 2023 - t_yil
# # 4 foydalanuvchi yoshini konsulga chiqaramiz
# print(f"Siz {str(yosh)} yoshda ekansiz")
# print("Siz " + str(yosh) + " yoshda ekansiz")
