"""
Mavzu:Xatolar bilan ishlash 2 
Sana:03.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # Exceptions 
# # Avvalgi bo'limda "Run time error" xatoliklari bilan tanishdik.Bunday xatolar dastur bajarish jarayonida
# # kelib chiqadi va dasturning ishlashini to'xtatadi.Sintaksis xatolikdan farqli ravishda,Python bunday xatoliklarni
# # jilovlashni o'rganamiz.Maqsadimiz-xatolik yuz berganda dastur to'xtab qolishining oldini olish.Gap shundaki,dastur 
# # davomida xato yuz berganda Python maxsus exception(istisno) obyektini yaratadi.Agar bu obyekt "tutib" olinmasa,
# # dastur bajarilishdan to'xtaydi.

# # try-except

# # Istisno obyektlarni tutib olish uchun Pythonda maxsus try-except operatorlari bor.Bu operatorlar quyidagicha ishlaydi,
# # try operatori badanida bajarish kerak bo'lgan kod yoziladi,except operatori badanida esa xatolik yuz berganda bajatilishi
# # kerak bo'lgan kod yoziladi.Ya'ni dasturimiz to'xtab qolmasdan bajarilaveradi.
# # Tushunarli bo'lishi uchun quyidagi misolni ko'ramiz.

# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# # Yuqoridagi dasturning 1-qatorida biz foydalanuvchidan yoshini kiritishni so'radik.Navbatdagi qatorda esa foydalanuvchi 
# # kiritgan qiymatni int() funksiyasi yordamida butun songa o'tkazyapmiz.Agar foydalanuvchi yoshini kiritganida butun emas,
# # o'nlik son kiritsa bu ValueError xatoligiga olib keladi va dastur bajarilishdan to'xtaydi:
    
# # Yoshingizni kiriting:32.2
# # ValueError: invalid literal for int() with base 10: '32.2'

# # Mana shunday xatolarning oldini olish uchun xato yuz bershi mumkin bo'lgan qatorlarni try-except bloki yordamida yozamiz.
# # Bunday try bloki ichida bevosita xato keltirib chiqarishi mumkin kodni,except bloki ichida esa xatolik yuz berganda bajarilishi 
# # kerak bo'lgan buyruqlarni yozamiz.
# # Tushunarli bo'lishi uchun yuqoridagi dasturni yangidan yozamiz.

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)  # xato qaytargan qator
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")
# except: # xato yuz bergan bajariluvchi kod
#     print("Butun son kiritmadingiz")
# print("Dastur tugadi")
    
# # Bu yerda ham dastavval foydalanuvchi yoshini so'radik.int() funksiyasini esa try badani ichida yoshdik,agar foydalanuvchi
# # to'g'ri qiymat kiritgan bo'lsa,kodimiz foydalanuvchining tug'ilgan yilini hisoblab ko'rsatadi,exception(istisno) yuz berganda 
# # esa "Butun son kiritmadingiz" xabarini konsolga chiqaradi.Lekin dastur bajarilishdan to'xtamaydi va try-except blokidan keyingi
# # qatorlar ham barilaveradi(print("Dastur tugandi"!)).

# # Yana bir bor,lekin bu safar o'nlik so kiritamiz:
    
# # try-except operatorining afzalliklaridan biri-foydalanuvchiga Python ko'rsatadigan tushunarsiz xatolar o'rniga o'zimizga istagan,
# # tushunarliroq matnni ko'rsatish imkonini beradi.Shuningdek,kompleks tizimlarda arzimagan xatoni deb dasturimiz to'xtab qolishining oldini oladi.

# # try-except-else

# # Yuqoridagi kodimizda biz try moduli ichida xato qaytarishi mumkin bo'lgan ifodani ham (tyil = int(tyil)),xato qaytmaganda bajarilishi kerak bo'lgan 
# # ifodani ham (print(f"Siz {2021-tyil} yoshdasiz")) birdan yoib ketyapmiz.Aslida,bunday qilishimiz to'g'ri emas.
# # To'g'ri usuli=avval xatoga tekshirish va xato yuz bermaganda bajariladigan ifodani alohida,else blokida yozish:
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh =   int(yosh)
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgan siz")
    
# # Albatta,yuridagi usul har doim ham qo'l kelavermaydi.

# # Ma'lum turdagi xatolarni ushlash

# # Xatolarning turlari ko'p,except operatori yordamida biz aynan qaysi xatolarni ushlamoqchi ekanimizni ham ko'rsatishimiz mumkin.Misol uchun,yuqoridagi 
# # yuqoridagi misolda int() funksiyasi ValueError xatosini qaytardi.Agar biz faqatgina shu turdagi xatolarni ushlamoqchi bo'lsa,except operatoridan so'ng 
# # xatolik nomini hom ko'rsatamiz:

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yoshda tug'ilgansiz")
    
# # Shu yo'sinda boshqa turdagi xatolarni ham tutib olish mumkin.

# # ZeroDivisionError
# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
    
# # IndexError 
# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} bor ")
    
# # KeyError

# #  Bu xatolik lug'atda mavjud bo'lmagan kalitga murojaat etishda kelib chiqadi:
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}
# key='tel'
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")
    
# # FileNotFoundError 
# # Bu xatolik Pythonda fayllar bilan ishlashda mavjud bo'lmagan faylga murogaat etish
# # ortidan kelib chiqadi.Biz fayllar bilan ishlash haqida kelgusi boblarda to'xtalamiz,
# # bu bo'limda esa shunday xatolikni ushlashni ko'ramiz,xolos:
# fayl = "data.text" # bunday fayl mavjud emas
# try: # faylni ochishga harakat qilamiz
#     f = open(fayl)
# except FileNotFoundError:
#     print(f"{fayl} fayli mavjud emas.")
    
# # Bir nechta xatolarni ushlash
# # try-except ketma-ketligida bir nechta except operatorlari ham bo'lishi mumkin.Ularning 
# # har biri ma'lum turdagi xatolik uchun javobgar bo'ladi:

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError:  # agar foydalanvuchi butun son kiritmasa,
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa,
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")
    
# # Xatolarni ko'rsatmay o'tish

# # Yuqoridagi misollarda kodimiz xato qaytarganida dasturimiz foydalanuvchiga xatolik haqida 
# # ma'lumot ko'rsatyapti.Agar dastur hech qanday ma'lumot ko'rsatmay,dasturni davom etishi talab qilinsa,
# # except badanida pass opertorida yozamiz.
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}
# key = 'tel'
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     pass

# # Umuman olganda,pass hech narsa bajarmasa-da,juda foydali opertor.Bu operator yordamida biz funksiyalar,
# # sikllar yoki if-else shartlarining badanini vaqtincha to'ldirib turishimiz mumkin.Misol uchun,siz dasturning 
# # skeletini o'ylab qo'ydingiz,qanday sikllar yoki shartlar bo'lishini raga qildingiz,lekin bevosita sikl yoki funksiya 
# # badanini yozishga yetib kelmagan bo'lsangiz,IndentationError xatoligining oldini olish uchun pass opertoridan foydalansiz.

# if yosh<20:
#     pass
# else:
#     pass

# # Yuqoridagi kodni pass operatorisiz yozib ko'ring:
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError:  # agar foydalanvuchi butun son kiritmasa,
#     pass
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa,
#     pass
# else:
#     pass 
    
# # Xatolarning oldini olish 
# # Yuqorida biz xatolar ro'y berganda ularni ushlash va dastur to'xtashining oldini olishni ko'rib chiqdik.
# # Lekin try-except ketma-ketligi xatolarning oldini olishga yordam bera olmaydi.Xatolarning oldini olish uchun 
# # if-else va while sikllaridan foydalanganimiz afzal.
# # Avvalgi bo'limdagi misolimizga qaytsak:
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh) # xato qaytargan qator
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")
# except:# xato yuz bergan bajariluvchi kod
#     print("Butun son kiritmadingiz")
   
# # Biz foydalanuvchi yoshini so'radik va foydalnuvchi butun son kiritmagani sababli dasturni to'xtatdik.
# # Aslida,bunday holatda while sikli yordamida foydalanuvchi to'g'ri qiymat kiritgunga qadar uning yoshini 
# # qayta so'rash to'g'riroq yechim bo'ladi.
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# E'tibor bering,foydalanuvchi kiritgan matn faqatgina sonlardan iborat ekanligini tekshirish uchun 
# .isdigit() metodidan foydalandik.

# Dasturni bajaramiz va boshlanishiga turli "noto'g'ri" qiymatlar berib ko'ramiz:

# Ko'rib turganingizdek,biz dastavval 12.5 qiymatini kiritdik va matn tarkibida nuqta belgisi bo'lgan uchun 
# .isdigit(12.5) metodi False qatardi va siklimiz boshiga qaytdi.Biz yana 2 marta xato qiymat kiritdik va 
# har gal sikl boshidan takrorlandi.4-urinishda 24 qiymatini kiritganimiz sababli .isdigit("24")  metodi 
# True qaytardi,siklimiz to'xtadi va "Siz 1997-yilda tug'ilgansiz" degan natija konsolga chiqdi.
# Albatta, yuqoridagi usul barcha xatolar uchun ishlamaydi.Shunday xatolar bo'lishi mumkinki,biz ularni 
# oldindan ko'ra olmasligimiz,oldindan to'g'irlay olmasligimiz mumkin yoki xato foydalanuvchiga bog'liq 
# bo'lmasligi mumkin.Shunday holatlarda try-except opertorlari bizning xaloskorimizga aylanadi.
