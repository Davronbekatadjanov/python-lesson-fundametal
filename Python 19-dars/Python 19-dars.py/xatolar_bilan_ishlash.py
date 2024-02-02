"""
Manvzu:Xatolar bilan ishlash
Sana:02.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# Xatolar bilan ishlash 

# # Har qanday dasturchi kod yoshida xatoga yo'l qo'yadi.Ko'p yozgan
# # odam ko'p xato qiladi va bu tabiiy.Ba'zi xatolarimiz Python tomonidan dastur bajarilishda
# # avval aniqlanadi.Ba'zilari esa dastur bajarish jarayonida aniqlanib,dasturimiz to'xtab qoladi.
# # Ushbu bobda dastavval dasturchilar ko'p yo'l qo'yadigan xatolik yuz berganda dastur to'xtab qolishining oldini olish
# # olishni o'rganamiz.

# # SyntaxError-Sintaksis xatolik 
# # Biz bu xatolik turi 2-bobda tanishgan edik.Syntax Error eng ko'p uchraydigan xato bo'lib,odatda,dasturlash tili
# # qoidalariga amal qilmaslik natijasida kelib chiqadi.Aksar dasturlash muhitlari bunday xatolikni 
# # dastur bajarilishidan avval aniqlab,dasturchiga ishora beradi.Sintaksis xatolik bor dasturni Python bajarmaydi.

# print "Hello world"
# # SyntaxError: Missing parentheses in call to 'print'. 
# # Did you mean print("Hello world")?

# # Odatda,dasturlash muhiti,xatoning turi bilan birga (Syntax Error) xato haqida qo'shimcha ma'lumot ham beradi:
# # Missing prentheses in call to 'print'. Did you mean print("Hello World")?

# # Xatolar bilan ishlashda xatolik matnini sinchkovlik bilan o'qish va tahlil qilish juda muhim.Agar ingliz tilini bilmasangiz, 
# # Google Translate yoki Yandex Tarjimon kabi onlayn xizmatlar yordamida xatolik matnini o'zingizga tushunarli (O'zbek yoki Rus 
# # tiliga tajima qilib xatoni to'g'irlashingiz mumkin.

# # EOL va EOG xatolik

# # EOL (End of Line - qator yakuni) xatoligi sintaksis xatolikning bir turi bo'lib,odatda,qatorda oxirida qo'shtirnoqni (birtirnoq) 
# # yopish esdan chiqqanda yuzaga keladi.
# print("Hello World!
# # SyntaxError: EOL while scanning string literal   
      
# # EOF (End of function - funksiya yakuni) xatoligi esa funksiya oxirida qavsni yopish esdan chiqqanda yuzaga keladi.
# print("Hello World!"   
# # SyntaxError: unexpected EOF while parsing 

# # EOF xatoligining muammoli tarfi - Python aynan qaysi funksiya yopilmay qolganini ko'rsata olmaydi va dastur yakuniga ishora qiladi.
# # Dasturingiz uzun bo'lsa, kodingizni sinchiklab ko'zdan kechirib chiqish talab etiladi.

# # Indentation - Joy tashlashda xatolik

# # Python tilida vaziyatga qarab kodni qator boshidan joy tashlab yoki tashlamasdan yozish muhim ahamiyatga eg.Qator boshidan asossiz 
# # joy qoldirish IndentationError ga olib keladi.
# # Quyidagi kodga e'tibor bering,qator boshida 1 dona bo'sh joy qolgani uchun dasturlash muhiti xatolikni aniqlab,
# # x bilan belgilab qo'ydi.
# # agar rasmdagi kodni bajaradigan bo'lsak,quyidagi natijani olamiz:
# # IndentationError: unexpected indent

# # Ba'zi joylarida esa, aksincha,bo'sh joy tashlab yozish talab qilinadi.Masalan,for siklida yoki if-elif-else shartlarining ichida va hokazo.
# print("O'ngacha sanaymiz")
# for n in range(10):
# print(n+1) # bu qator joy tashlab yozilishi kerak edi.
# # IndentationError: expected an indented block

# # Yana bir miso ko'ramiz:
# son = 50 
# if son>=0:
#     print("Musbat son")
# else:
# print("Manfiy son")
# # IndentationError: expected an indented block

# Qancha joy tashlaymiz?
# Yuqoridagi misollarda IndentationError oldini olish uchun joy tashlash talab qilindi.Xo'sh,qancha joy tashlash kerak va qanday qilib?

# Aslida,hech bo'lmaganda 1 harflik bo'sh joy qoldirish ham bizni IndentationError dan xalos etadi.LEKIN biz dastur davomida bir xil 
# joy tashlashga odatlanishimiz kerak.
# Qoida sifatida kamida 4 harflik joy yoki 1 ta TAB (klaviaturadagi tab tugmasi) joy tashlashga odatlanishimiz zarur.
# Eng muhimi,bir dastur (loyiha) davomida ikkalasini aralashtirmaslik lozim.Ya'ni agar joy tashlash uchun Space (probel)
# tugmasini ishlatsangiz,oxirigacha shunday qiling,agar Tab ishlatsangiz,oxirigacha tab ishlating.Ikkalasini aralashtirmang!

# Run time error -  dasturni bajarishda xatolik
# Run time error dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini to'xtatadi.Sintaksis xatolikdan farqli ravishda,
# Python  bunday xatolarni dasturni bajarishdan avval aniqlay olmaydi.Bu xatolikning bir necha turi bor.
# Ulardan ba'zilari bilan tanishamiz.

# # TypeError

# # Biror funksiya yoki metodga noto'g'ri ma'lumot turini yuborish:
# son = input("Istalgan  son kiriting: ")
# print(f"{son} ning kvadrati {son**2} ga teng")
# # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

# # Yuqoridagi kodda biz foydalanuvchi kiritgan qiymatni matndan songa o'tkazi olishni unutdik,natijada sonning kvadratini 
# # hisoblashda Python xato berdi.

# # NameError
# # O'zgaruvchi,funksiya,obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik.
# prit("Hello World")
# # NameError: name 'prit' is not defined

# # Yuqorida print() funksiyasini prit() deb xato yozganimiz sababli Python bunday funksiya yo'q deb xato qaytardi.
# # Yana bir misol ko'ramiz:
# misol = ['olma','uzum','nok','anor','anjir']
# for meva in mvealar:
#     print(meva)
# # NameError: name 'mvealar' is not defined
# # Xatoni topdingizmi?

# # ValueError 
# # Funksiyaga noto'g'ri qiymatni yuborish natijasidagi xatolik 

# son = int("Istalgan son kiriting: ")
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
#     # Kodni bajaramiz:
# # ValueError: invalid literal for int() with base 10: 'Istalgan son kiriting: '

# # Yuqoridagi dasturning 1-qatorida foydalanuvchidan istalgan son kiritishni so'radik va foydalanuvchi kiritgan qiymatni int,
# # ya'ni butun songa o'tkazdik.Kodning o'zida xato yo'q,lekin dastur bajarish jarayonida foydalanuvchi butun son emas,
# # o'nglik son kiritgani uchun ValueError xato chiqadi.Sababi,int() funksiyasi faqatgina butun sonlar ko'rinishdagi matn bilan ishlaydi.
# # Dastur xato bermasligi uchun yoki int() funksiyasini float() funksiyasiga alamashtirish yoki foydalanuvchidan 
# # butun son kiritishni talab qilishimiz kerak.

# # IndexError 
# # Yangi dasturchilar yo'l qo'yadigan yana bir xato indeks xatolikdir.Ya'ni ro'yxat elementlariga murojaat eltishda indeksni noto'g'ri kiritish
# # (ro'yxatda mavjud bo'lmagan elementga murojaat etish):
    
# mevalar = ['olma','anor','uzum']
# print(mevalar[3])
# # IndexError: list index out of range
# # Natijani tahlil qilamiz.Bizda uchta elementdan iborat mevalar ro'xyat mavjud.Biz 3-elementni konsolga chiqarmoqchimiz va print(mevalar[3]) 
# # deb yozdik va IndexError natijasini oldik.Sababi,dasturlashda indeks 0 dan boshlanadi va 3-elementga 
# # murojaat etish uchun 2-indeksni tanlaymiz.Demak,to'g'ri kod:
    
# print(mevalar[2])
# # Yuqoridagi kodning javobi:uzum

# # ZeroDivisionError 
# # Dastur jarayonida 0 ga bo'lish natijasida yuzaga keladigan xatolik
# x ,y = 50,50 
# z = 250/(x-y) # x-y=0
# # ZeroDivisionError: division by zero

# # Mantiqiy xatolar
# # Mantiqiy xatolar-dasturchi tomonidan dastur algoritmini yozishda yo'l qo'yilgan xatolar.Bunday xatolar dastur bajarilishiga to'sqinlik qilmasa-da,
# # dastur to'g'ri ishlashiga xalaqit qiladi va kutilgan natijani bermaydi.
# # Mantiqiy xatolar eng ko'p uchraydigan va aniqlash qiyin bo'lgan xatolar hisoblanadi.Aksar holatlarda Python mantiqiy xatolarni aniqlamaydi va 
# # dastur bajailaveradi (lekin kutilgan natija chiqmaydi).Bunday xatolarning oldini olish uchun dasturimizning har bir  qadamida  chiqayotgan natijalarni
# # tekshirib borish kerak.Katta dasturlar o'nlab,balki yuzlab funksiyalardan iborat bo'ladi,agar mantiqiy xatolar vaqtida topilmasa,minglab qator kodlarni 
# # ko'zdan kechirib chiqish talab etilishi mumkin.
# # Mantiqiy xatolar turli ko'rinishda bo'lishi mumkin,masalan,sonlar bilan ishlashda:
# radius = 5 
# pi = 4.14 
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)

# # kod bajarildi,natija ham chiqdi.Lekin natija xato.Nima uchun?Sababi,biz pi=4.14 deb xato yozib ketdik (tog'ri qiymat: pi=3.14).
# # Avval aytganimizdek,mantiqiy xatolarning oldini olish uchun dasturimizning har bir qadimida chiqayotgan natijalarni tahlil qilib borish muhim.
# # Sodda dasturlar qo'lda bajariladi,murakkabroq funksiyalar uchun esa maxsus test dasturlar yoziladi.Test dasturlar yozish haqida kelgusi boblarda alohida gaplashamiz.
# # Hozir esa qo'lda tekshirishni ko'raylik:
# son = float(input("Istalan son kiriting: "))
# ildiz = son**1/2 
# print(f"{son} ning ildizi {ildiz} ga teng")

# # Dasturimiz biz kutgan natijani berdi.Lekin yaxshi dastuchi bitta test bilan chegaralanmaydi.Dasturni qayta bajaramiz:
# # Istagan son kiriting: 9
# # 9.0 ning ildizi 4.5 ga teng
# # Mana endi natija xato,9 sonining ildizi 4.5 bo'lib chiqdi.Kodni tahlil qilamiz: 2-qatorda ildizni hisoblashda  1/2 qavs ichida yozilmagani xatolikka olib kelyapti.
# # Natijada foydalanuvchi kiritgan son avval 1-darajaga oshiriladi va undan keyin 2 ga bo'lindi.Kodni to'g'rilaymiz va dasturni 3-4 marta turli qiymatlar berib barib ko'ramiz:

# son = float(input("Istalgan son kiriting: "))
# ildiz = son**(1/2)
# print(f"{son} ning ildizi {ildiz} ga teng")

# Ba'zida noo'rin bo'sh joy qoldirish (yoki qoldirmaslik) ham mantiqiy xatoga olib kelishi mumkin:
mevalar = ['olma','uzum','nok','anor','anjir']
for meva in mevalar:
    print(meva)
    print("Dastur tugadi")

# Yuqorida "Dastur tugadi" matni bir marta,dastur tugaganidan so'ng chiqishi kerak edi.Lekin o'nnga surilib qolgani uchun bir necha bor qaytarildi.
# Bundan boshqa ham mantiqiy xatoliklar juda ko'p uchraydi.Mantiqiy xatoliklar mutlaqo topilmasdan ham qolib ketishi va dastur bozorga chiqqanidan so'ng aniqlanishi
# tabiiy hol.Shuning uchun ham aksar dasturlar  tez-tez yangilanib turadi.Dasturlash jarayonida bundan boshqa xatoliklar,xalos.Keyingi bo'limda Runtime xatoliklarni dastur davomida
# aniqlash va dastur to'xtab qolishining oldini olishni o'rganamiz.

