"""
Mavzu:if-else
Sana:11.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # Shartlar va tarmoqlanish

# # Shu vaqtgacha yozgan dasturlarimizga e'tibor bersangiz,dasturimiz yuqoridan pastga qarab qatorma qator bajarilib keldi.Bu chiziqli dastur deyiladi.Voqelikda esa aksar dasturlar ma'lum bir shart bajarilishiga (yoki bajarilmaganiga) ko'ra kodning bir qismidan boshqa qismiga "sakrab" o'tishi tabiiy hol.Dasturlashda bu tarmoqlanish deb ataladi.
# # Misol uchun,ijtimoy tarmoqlar yoshingizdan kelib chiqqan holda sizga mos mavzularni ko'rsatishi tarmoqlanishiga misol bo'ladi.Yoki ba'zi internet sahifalar sizga sahifaning tilini tanlash imkonini beradi(Rus/O'zbek/Ingliz) va tanlovingizga qarab turli yo'nalishlarda davom etadi.
# # Dastur tarmoqlanishi uchun avval ma'lum bir shartlar bajarilishi kerak (yosh-7,til=o'zbek,jins=Ayol va hakozo).Uchbu bobda mana shunday shartlarni yozish,tekshirish va shart bajarilishi (yoki bajarilmaganiga) ko'ra dasturni tarmoqlashni o'rganamiz.
# # Taqqoslash operatorlar 
# # Dastur tarmoqlanishi uchun,avval,bior shart bajarilishi kerak.Shart bajarilishini tekshirish uchun esa maxsus taqqoslash operatorlari mavjzud.Bu opertorlar yordamida biz o'zgaruvchilarning ma'lum qiymatga tengligini yoki,aksincha,teng emasligini yoxud ifodalarning natijasi berilgan qiymatdan katta yoki kichikligini va hokazo shartlarni tekshirib ko'rishimiz mumkin.
# # Taqqoslash opertori: == :Ma'nosi: tenglik :ishlatilishi: a==b
# # Taqqoslash opertori: != :Ma'nosi: tengsizlik :ishlatilishi: a!=b
# # Taqqoslash opertori: > :Ma'nosi: katta   :ishlatilishi: a>b
# # Taqqoslash opertori: < :Ma'nosi: kichik :ishlatilishi: a<b
# # Taqqoslash opertori: >= :Ma'nosi: katta yoki teng  :ishlatilishi: a>=b
# # Taqqoslash opertori: <= :Ma'nosi: kichik yoki teng  :ishlatilishi: a<=b

# # Taqqoslash opertorlari mantiqiy qiymat qaytaradi.Mantiqiy qiymalar True(shart bajarildi)yoki False (shart bajarilmadi) bo'lishi mumkin.
# # True ingliz tilidan "To'g'ri",False esa "Yolg'on" deb tajima qilinadi.
# # Tushunarli bo'lishi uchun quyidagi misolni ko'ramiz:
# a=5 
# b=6 
# print(a==b) # a b ga tengmi?

# # Yuqorida biz a ga 5,b ga 6 qiymatini yukladik.3-qatorda bu ikki o'zgaruvchining bir-biriga tengligini tekshirganimizda  (a==b) taqqoslash operatori False qiymatini qaytardi.(ya'ni tenglik bajarilmadi.)
# a = 5
# b = 6
# print(a==(b-1))

# # Bu safar taqqoslashning o'ng tarafiga b-1 ifodasini yozdik,b-1=5 bo'lgani uchun tenglik bajarildi va taqqoslash operatori True qiymatini qaytardi.Demak,mana shu yo'sinda biz turli ifodalarni taqqoslashimiz mumkin ekan.
# # Taqqoslash,odatda,bir turdagi ma'lumotlar o'rtasida bo'ladi.Misol uchun,matnlarni matn bilan,sonlarni sonlar bilan va hokazo.
# print('anvar'=='Anvar') # matnlarni taqqoslash
# print(10**2<2**18) # sonlarni taqqoslash

# # Taqqoslash qanday ishlashini tushunish uchun quyidagi mashqlarni Pythonda bajarib ko'ring va natijasini tahlil qiling:
# ism = 'ahad'
# print(ism!='ahad')
# # False
# print(ism.title()=='Ahad')
# # True
# nums1=[1,2,3,]
# nums2=[1,2,4]
# print(nums1!=nums2) 
# # True
# print(9**2>=7*9+18)
# # True
# x=10
# # print(x*x<'x**2')
# # # Type error
# print(x*x>=float(f"{x**2}"))
# # True
      
# # if-else operatori
# # Avvalgi bo'limda biz turli ifodalarni taqqoslashni o'rgandik,keling,endi taqqoslashning natijasiga ko'ra tarmoqlanishini ham ko'zdan kechiraylik.Buning uchun dasturlash tillarda maxsus if operatori mavjud."if" so'zi ingliz tilidan "agar" deb tarjima qilinadi va ma'lum bir shart qanoatlantirilishiga qarab shu shartga bog'langan kod ham bajariladi.
# son = int(input("Istalgan son kirting: "))
# if son>0:
#     print(son, "musbat son")

# # Yuqoridagi daturni tahlil qilamiz:
# # 1-qatorda biz foydalanuvchidan istalgan son kiritishini so'raymiz
# # 2-qatorda if operatori yordamida kiritilgan sonning 0 dan katta ekanini teshiramiz.Bu qatorni "agar son 0 dan katta bo'lsa" deb o'qish mumkin.
# # 3-qatorda if operatorining badani hisoblanadi va faqatgina  yuqoridagi shart to'g'ri (True) bo'lsa,bajariladi.
# # Kening,endi dasturni bajaramiz:
# # Istalgan son kiriting:5
# # 5 musbat son
# # Biz 5 sonini kiritdik.5>0 bo'gani uchun kodning 3-qatori bajarildi va "5 musbat son"degan endi manfiy son kiritib ko'ramiz.
# # Ko'rib turganingizdek,son>0 ifodasi False qaytargani uchun 3-qatordag kod bajarilmadi.

# # Keling yana bir misolga e'tibor qaratamiz va yangi else operatori bilan tanishamiz."else" so'zi ingliz tilidan "aks holda" deb tarjima qilinadi va if operatorida berilgan shart qanoatlantirilmasa,else operatoridan keyingi kod bajariladi.
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=7: # agar yosh 7 dan kichik yoki teng bo'lsa 
#   print("Sizga avtobus bepul")
# else:
#   print("Sizga chipta narxi 5000 so'm")

# # Yuqoridagi dasturda foydalanuvchi yoshini so'raymiz.Agar foydalanuvchi 7 yoshdan kichik bo'lsa,"Sizga avtobus bepul" aks holda (else), "Chipta narxi 5000 so'm" degan yozuvni konsolga chiqaramiz.
# # Shart "badani" shartdan biroz o'nnga surib yoziladi (xuddi for sikl kabi).if/else dan keyin va o'nnga surib yozilga har bir qator if/else shartining badani hisoblanadi. 

# # Bir qator if-else
# # Qisqa kodlar uchun shart va uning badanini 1 qatorga jamlab yozishimiz ham mumkin.Agar shartimiz faqat if dan iborat bo'lsa,uning badanini keyingi qatordan emas,ikki nuqtadan keyin yozish kifoya:
# yosh = int(input("Yoshingiz nechida?>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# # Agar kodimizdan if=else birgalikda qatnashsa,if ning badani undan oldin,else ning badani esa keyin yoziladi:
# x,y =25,50 # x=25 va y=50
# print("x>y") if x>y else print("x<y")

# # Matnlarni solishtirish 
# # Aksar tizimlar foydalanuvchi kiritgan matnni ma'lum bir ko'rnishiga keltirib oladi.Sababi,kompyuter uchun 'Ali','ALI' va 'ali'- uchta turli xil ism.Ularni solishtirish uchun esa bir ko'rnishga keltirib olish kerak.
# # Tasavvur qiling,siz yangi elekotron pochta ochmoqchisiz va o'zingizga yangi foydalanuvchi ismini tanlashingiz kerak.Kompyuter siz kiritgan foydalanuvchi ismini tizimdagi mavjud foydalanuvhcilar bilan solishtiradi,agar ism band bo'lsa,sizga boshqa ism tanlashni tavsiya etadi.Solishtirish jarayonida esa siz tanalgan ismni kichik harflarga o'tkazib,boshqa ismlar bilan solishtiradi.
# # Rasmda ko'rsatilgan misolda kimdir anvar@yandex.ru manzilini band qilgan,agarda men 'Anvar','ANvar' yoki 'ANVAR' deb login tanlasam ham, anvar@yandex.ru band bo'lgan sababli men so'ragan loginlar rad etilaveradi.
# # Xo'sh,turli ko'rinishda yozilgan matnlarni qanday qilib solishtiramiz?
# # Juda oddiy.Matnlarni solishtirishdan avval .lower() matodi yordamida kichik harflar ko'rinishiga keltirib olamiz:
# ism = 'Ali'
# ism.lower() == 'ali' 
# # Natijasi: True

