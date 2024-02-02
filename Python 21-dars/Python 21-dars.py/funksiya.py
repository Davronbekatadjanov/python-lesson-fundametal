"""
Mavzu:Funksiya
Sana:04.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # Funksiya ma'lum bir vazifani bajarishga mo'lgallangan kodlar yig'indisidir.
# # Funksiyalar,odatda,ma'lumotlarni qabul qilib oladi,ularni qayta ishlaydi va biror natija qaytaradi.
# # Biz darslarimiz davomida bir nechta tayyor funksiyalardan foydalanib keldik.Misol uchun,print()
# # funksiyasi matn yoki ifoda qabul qiladi va uni konsolga chiqaradi,range() funksiyasi esa ma'lum
# # oraliqdagi sonlarni yaratish uchun ishlatiladi.
# # Aslida,har qanday funksiyaning ortida ham bir nechta qatordan iborat kod bo'ladi,lekin biz funksiyaga
# # murojaat etganda uning nomini yozamiz,xolos.Funksiya ortidagi kod esa  biz uchun yashirin bo'lib qolaveradi.
# # Funksiyalarning qulaylikgi ham shunda.Dastur davomida ma'lum bir kodlarni qayta-qayta yozmaslik uchun biz ularni jamlab,
# # bitta kunksiya ichiga joylashimiz va dastur davomida bu kodlarga funksiya nomi orqali murojaat etishimiz mumkin.
# # Funksiyalar turlicha bo'ladi,ba'zi funksiyalar sizdan qiymat qabul qilib,konsolga biror ma'lumot chiqaradi,ba'zilari esa sizdan
# # qabul qilgan qiymat ustida turli amallar bajarib yangi qiymat qaytaradi.Foydalanuvchidan mutlaqo qiymat qabul qilmaydigan
# # funksiyalar ham mavjud.
# # Ushbu bobda biz Pythonda yangi funksiya yaratish,unga murojaat etish,tekshirish va to'g'irlashni o'raganamiz.Shuningdek,
# # darsimiz yakunida dasturimizni bir nechta fayllarga ajratishni va funksiyalarni alohida modullarga joylashni ham o'rganamiz.

# # Funksiya yaratamiz
# # Boshlanishiga oddiy,hech qanday qiymat qabul qilmaydigan funksiya yaratishni ko'rib chiqaylik.Bu funksiyaga murojaat etganimzda konsolga "Assalomu alaykum!"
# # degan xabarni chiqarsin.
# def salom_ber():
#     """Salam beruvchi funksiya"""
#     print("Assalomu alaykum!")

# # Kodni tahlil qilamiz:
#     # Avvalo,def operatori yordamida Pythonga funksiya yaratayotganimizni bildirdik.def dan so'ng esa funksiyamizga nom berdik
#     # va qavslarni ochib-yopdik.Bizning funksiyamiz foydalanuvchidan hech qanday qiymat qabul qilmaydi,shuning uchun ham qavs
#     # ichida bo'sh.Keyingi misollarda foydalanuvchidan qiymat qabul qiluvchi funksiyalarni ham ko'ramiz.
#     # def qatoridan keyin o'ngga surib yozilgan har qanday kod funksiyaning badani hisoblanadi.2-qatorda biz uchun ketma-ket
#     # qo'shtirnoq ichida funksiya haqida ma'lumot berdik.Python mana shu ma'lumotni o'qib,dasturchi funksiya haqida bilmoqchi
#     # bo'lganda aynan shu matnni ko'rsatadi.
#     # Oxirgi qatorimizda esa "Assalomu alaykum!" matnini konsolga chiqarishni buyurdik.Sodda funksiyamizning asosiy vazifasi ham shu.

# # Mana,funksiya tayyor.Endi bu funksiyadan foydalanish uchun uni chiqaramiz.Buning uchun funksiya nomini yozamiz va qavslarni ochib-yopamiz.
# # Funksiyamiz hech qanday qiymat qabul qilmaydi,shuning uchun qavslar ichini bo'sh qoldiramiz.
# salom_ber()
# # Funksiyaga nom berishda fe'l,ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning.Bu bilan siz o'zgaruvchi va funsiya
# # o'rtasini farqlashingiz oson bo'ladi.Misol uchun,yuqorida biz funksiyamizni salom emas,salom_ber deb nomladik.

# # Qiymat qabul qiluvchi funksiya
# # Avvalgi sodda funksiyamiz foydalanuvchida hech qanday qiymat olmaydi va barcha birda "Assalomu alaykum!" deb javob qiladi.
# # Keyingi funksiyaga o'zgartirish kiritamiz,funksiya foydalanuvchi ismini qabul qilib,unga ismi bilan murojaat etsin.Buning uchun funksiya
# # nomidan keyin qavs ichida foydalanuvchi berishi kerak bo'lgan qiymatni ko'rsatamiz.

# def salom_ber(ism):
#     """Foydalanuvchiga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum,hurmatli {ism.title()}!")

# # Bunday funksiya murojaat etish uchun qavs ichida so'ralgan qiymatni berish talab qilinadi:
# salom_ber('hasan')
# # Agar funksiyaga murojaat etishda unga qiymat bermasak,xatolik vujudga keladi:
# salom_ber()
# # TypeError: salom_ber() missing 1 required positional argument: 'ism'

# # Funksiya yaratishning asl maqsadlaridan bir-biz unga qayta-qayta,yangi qiymatlar bilan murojaat etishimiz mumkin.
# salom_ber('hasan')
# salom_ber('olim')

# # Docsting
# # Funksiyani yaratishda qanday ishlashi haqida qisqacha ma'lumot berib ketish o'zimiz uchun ham,kelajakda bizning funksiyamizni
# # ishatadigan boshqa dasturchilar uchun ham juda foydali bo'ladi.Bunday ma'lumotlar docstring deb ataladi va funksiya badanining
# # ilk qatorida uchta qo'shtirnoq ichida yoziladi:
# def salom_ber():
#     """Salom beruvchi funksiya""" # <-Docstring
#     print("Assalomu alaykum!")

# # Murakkab funksiyalar uchun docstringni bir nechta qatorga bo'lib yozish mumkin:
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,
#        unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum,hurmatli {ism.title()}!")

# # Docstringni konsolga chiqarish uchun quyidagi buyurqni yozamiz:print(funkisya_nomi._doc_)
# print(salom_ber.__doc__)

# # Odatda,dasturlash muhitlari funksiya nomini yozishnigiz bilan docstring ichidagi matnni ko'rsatadi:

# # Argument va parametr
# # Funksiya yaratihsda qavs ichida berilgan,funksiya to'g'ri ishlashi uchun uzatiladigan parametr deb ataladi.
# # Sodda bir misol keltiramiz:
# def salom_ber(ism):
#         """Foydalanuvchi ismini qabul qilib,
#             unga salom beruvchi funksiya"""
#         print(f"Assalomu alaykum,hurmatli {ism.title()}!")

# # Yuqoridagi misolda ism-salom_ber funksiyasining parametri.
# # Parametrlarga mazmunli nom berishni odat qiling:
#     # qisqa harflardan foydalanmaymiz masalan: def salom_ber(n)
#     # to'g'ri bo'lishi uchun def salom_ber(name)
#     # to'g'ri bo'ishi uchun def salom_ber(ism)
# # Foydalanuvchi funksiyaga murojaat etishda funksiyaga uzatgan qiymat argument deb ataladi.salom_ber('hasan') kodida
# # 'hasan'- argument deb ataladi.
# # Demak,parametr va argument bitta narsaga ikki xil qarash ekan,xolos.
# # Ba'zi manbalarda argument va parametr so'zlari almashtirib ishlatilishi ham kuzatiladi.

# # Funksiyaga bir nechta argument uzatish

# # Ba'zi funksiyalar bir emas,bir nechta parametr talab qilishi mumkin,foydalanuvchi esa,o'z navbatida,bir nechta
# # argumentlar taqdim qilishi kerak.Funksiyaga argument uzatishning bir nechta usuli bor,keling,ular bilan birma-bir tanishamiz.

# # To'g'ri tartibda uzatish
# # Bu usulda funksiya parametrlari qaysi tartibda yozilgan bo'lsa,argumentlar ham aynan shu ketma-ketlikda uzatilishi shart.
# # Bitta misol keltiramiz.Quyidagi funksiya foydalanuvchining ismi va familiyasini parametr sifatida qabul qilib ,ularni jamlab xabar chiqaradi.

# def toliq_ism(ism,familiya):
#     """ism va familiya jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# # Yuqoridagi funksiya to'g'ri natija chiqarishi uchun argumentlarni ism va familiya ketma-ketligida kiritishimiz lozim.
# toliq_ism('olim', 'hakimov')
# # Agar argumentlarni noto'g'ri ketma-ketlikda bersak,natija ham biz kutganday chiqamaydi:
# toliq_ism('hakimov','olim')

# Ko'p holatlarda esa argumentlarni noto'g'ri tartibda uzatish xatalikka olib kelishi mumkin.
def yosh_hisobla(ism,tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan funksiya"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
# Funksiyani chiqaramiz.
yosh_hisobla('olim', 2005)

# # Endi argumentlarni o'rnini almashtirib yozib ko'ramiz:
# yosh_hisobla(2005, 'olim')
# # AttributeError: 'int' object has no attribute 'title'

# # Parametr nomi bilan uzatish
# # Yuqoridagi kabi holatlarning oldini olish uchun argumentlarni parametr nomi bilan qo'shib uzatishimiz mumkin.Bularni parametr nomi bilan
# # qo'shib uzatishimiz mumkin.Buning uchun funksiyaga o'zgarrtirish kiritish talab qilinmaydi.
# yosh_hisobla(tugilgan_yil=2005, ism='olim')

# # Yuqoridagi misolda funksiyani chaqirishda biz parametrlar ketma=ketligiga rioya qilmagan bo'lsak-da,argumentlarni parametr=qiymat
# # ko'rinishida yozganimiz sababli funksiya to'g'ri ishladi.
# # Xuddi shu kabi yuqoridagi toliq_ism funksiyasiga murojaat etishimiz mumkin:
# toliq_ism(familiya='hakimov', ism='olim')
# # Bu usuldan foydalanganda parametr nomi to'g'ri yozilishiga e'tibor bering!

# # Standart qiymat

# # Funksiya yaratishda istalgan parametr uchun standart qiymat ko'rsatib ketishimiz mumkin.Agar foydalanuvchi shu parametr uchun
# # qiymat(argument) kiritmasa,funksiya bajarilishi jarayonida standart qiymat ishlatiladi.Standart qiymat funksiya yaratish vaqtida
# # parametr = qiymat ko'rinishida beriladi.
# # Quyidagi misolda yosh_hiobla funksiyasida  joriy_yil parametriga standart qiymat beramiz:
# def yosh_hisobla(tugilgan_yil,joriy_yil=2021):
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# # Funksiya yaratishda standrat qiymatga ega parametrlar doim oxirida yozilishi kerak.Aks holda,xatolik yuzaga keladi.
# # Keling,avval funksiyani ikkala argument bilan chaqiramiz:
# yosh_hisobla(1995,2020)

# # Endi esa faqat biita argument (tugilgan_yil) bilan chaqiramiz:
# yosh_hisobla(2005)
# # Bu safar foydalanuvchi joriy_yil ni kiritmagani sababli standart qiymat - 2021 ishlatildi.

# Funksiyaga murojaat etishda turli xatoliklarga yo'l qo'yishiimiz tabiiy.Bunday holatlarda Python qaytargan xatoni sinchiklab o'qib,
# xato qayerdaligini topishimiz va uni to'g'rilashimiz zarur.Quyida men turli funksiyalar yaratib,ularga xato usullar bilan murojaat etaman
# Xatolar nimada ekanini topa olasizmi?

# # 1-misol

# def yosh_hisobla(tugilgan_yil,joriy_yil=2020):
#     """Tug'ilgan yildan yoshini hisoblaymiz"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)

# # 2-misol

# def yosh_hisobla(tugilgan_yil,joriy_yil=2021):
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(1993)

# # 3-misol

# def salom_ber(ism):
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu alaykum {ism.title()}!")
# salom_ber('hasan')

# # 4-misol
# def toliq_ism(ism,familiya):
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism(ism='olim',familiya='hakimov')
