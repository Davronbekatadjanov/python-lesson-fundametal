"""
Mavzu:Lug'at va to'plam 
Sana:17.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # Lug'at va to'plam 
# # Ushbu bobda yangi ma'lumot turlari,lug'at (dictionary) va to'plam (set) bilan tanishamiz.Dars davomida lug'at yaratish,unga ma'lumot qo'shish,lug'atning ichida ro'yxat yoki,aksincha,ro'yxatning ichida lug'at saqlash kabi mavzular bilan tanishamiz.Darsimiz so'nggida esa to'plamlar haqida qisqacha to'xtali o'tamiz.

# # Lug'at nima?
# # Lug'at bir obyektga bog'liq ma'lumotlarni kalit so'z va qiymat juftligi ko'rinishida saqlash imkoniyatini beradi.Bu esa,o'z navbatida,lug'at ichidagi ma'lumotlarni tushunishni osonlashtiradi.Misol uchun,biz biror avtomabilfa oid lug'at yaratishimiz va lug'atda shu avtomabilga tegishli barcha ma'lumotlarni saqlashimiz mumkin (avtomobilning nomi,rangi,yili,motori,narxi va hokazo.)
# # Nima uchun bu ma'lumot turi lug'at deyilishini tushunish uchun oddiy lug'atga qaraylik.Odatda,lug'atdagi ma'lumotlar ikki qismdan iborat bo'ladi:kalit so'z va izoh (yoki tarjima).Xuddi oddiy lug'atlardagi kabi Python lug'atidagi ma'lumotlar ham ikki qismdan iborat bo'ladi:kalit so'z va qiymat (ingliz tilida bu "key-value pair",ya'ni "kalit-qiymat juftligi deyiladi").
# # Dasturlashda ko'p ishlatiladigan atamalarni ingliz tilida yodlab qolish juda muhim! Bu sizga kelajakda yangi ma'lumotlaar izlashda,xatolar ustida ishlashda,umuman,ish faoliyatingizda ko'p asqatadi.Shuning uchun variable,integer,float,string,list,tuple,dictionary,function,loop,key,value va boshqa atamalarning ma'nosini yaxshilab o'zlashtirib oling.
# # Pythonda lug'at yaratish uchun katta (jingalak) qavsdan foydalanamiz.Qavs ichida har bir element uchun kalit so'z va qiymat beramiz.Ularning orasi ikki nuqta (:) bilan,har bir element (juftlik) esa vergul(,) bilan ajratiladi:

# car = {'model':'ferrari','rang':'qizil'}

# # Yuqoridagi car degan lug'at yaratdik.Lug'atda 2ta element bor:mashinaning modeli(ferrari) va rangi(qizil).Bu yerda 'model' va 'rang' kalit so'zlar,'ferrari' va 'qizil' esa mos keluvchi kalit so'zlarning qiymatlaridir.
# # Lug'at ichidagi kalitlar takrorlanmasligi kerak.Agar lug'at yaratishda kalit so'zlar takrorlansa,ulardan faqat oxirgisining qiymati saqlanib qoladi.
# # Lug'at bilan ishlash 
# # Demak,Pythonda lug'at kalit-qiymat juftliklarining yig'indisi ekan.Lug'atdagi biror elementning qiymatini ko'rish uchun unga kalit so'z va orqali murojaat etamiz:

# car = {'model':'ferrari','rang':'qizil'}
# print(car['model'])
# print(car['rang'])

# # Lug'atdagi qiymatlar son (int,float),matn(string),ro'yxat (list,tuple),hatto boshqa lug'at ham bo'lishi mumkin.
# talaba = {'ism':'murod olimov','t_yil':2000,'yosh':20}
# print(f"{talaba['ism'].title()},\
#   {talaba['t_yil']}-yilda tu'gilgan,\
#   {talaba['yosh']}-yoshda ")
# # Uzun lug'atlarni bir necha qatorga bo'lib yozishimiz ham mumkin.Bunda har bir element alohida qatordan yoziladi va qator oxirida vergul qo'yilib,yangi qatorga o'tiladi.
# car = {
#   'make':'GM',
#   'model':'Malibu',
#   'color':'Black',
#   'gear':'Automatic',
#   'year':2023,
#   'price':40000
# }

# # get() metodi
# # Yuqorida biz lug'at elementiga kalit so'z orqali murojaat etishni o'rgandik.
# print(car['model'])
# # Bu usulning kamchiligi shundaki,agar lug'atda siz so'ragan kallit topilmasa,dastur KeyError xatoligi bilan to'xtab qoladi.
# # print(car['narx'])
# # Lug'atda 'narx' kalit so'zi bo'lmagani uchun yuqoridagi kod KeyError degan xatoni qaytaradi.
# # Biz kegusi darslarimizda Pythondagi xatolarni dastur bajarilishi jarayonida 'tutib olish'ni o'rgaanamiz.Hozircha esa get() metodi yordamida lug'atga murojaat etish va mavjud bo'lmaga kalitning o'rniga biror xabar qaytarishni ko'rib chiqaylik.
# # narx = car.get('narx','Bunday kalit mavjud emas')
# # Yuqorida lug'at nomidam so'ng.get() metodini yozdik,argumentlar sifatida ('narx') va kalit mavjud bo'lmaganda chiqadigan xabarni yozdik ('Bunday kalit mavjud emas').
# print(narx)

# # Agar .get() metodida ikkinchi argumentni tashlab ketsangiz va siz so'ragan kalit mavjud bo'lmasa, .get() metodi None qiymatini qaytaradi.
# car = {
#   'make':'GM',
#   'model':'Malibu',
#   'color':'Black',
#   'gear':'Automatic',
#   'year':2023,
#   'price':40000
  
# }
# narx = car.get('narx')
# print(narx)

# # None qiymat mavjud emas degan ma'noni beradi.
# # Yangi juftlik qo'shish
# # Lug'atga yangi element(kalit so'z va qiymatlar) qo'shishimiz ham mumkin.Keling,yuqoridagi talaba nomli lug'atga yana 2 ta - kurs va fakultet nomli kalit so'zlar va qiymatlar qo'shamiz:
# talaba = {'ism':'murod olimov','t_yil':2000,'yosh':20}
# talaba['kurs'] = 4
# talaba['fakultet'] = 'informatika'
# # Lug'atni konsolga chiqarib ko'ramiz:
# print(talaba)

# # Bo'sh lug'at
# # Ba'zida dastur boshida bo'sh lug'at yaratib,dastur davomida lug'atga yangi ma'lumotlar kiritib borish talab qilinishi mumkin.Bunday holatda bo'sh lug'at quyidagicha yaratiladi:
# car = {}
# # Dastur davomida esa lug'atga qiymatlar kiritib borilishi mumkin:
# car['model'] = 'Mazda 65'
# car['color'] = 'Red'
# car['price'] = 40000
# print(f"{car['color']} {car['model']} {car['price']}")

# # Lug'atga kalit so'zlar qanday ketma-ketlikda kiritilsa,shu tartib saqlanib qoladi.

# # Qiymatni o'zgartirish
# # Biror kalit so'zga tegishli qiymatni o'zgaritish esa quyidagicha amalga oshiriladi:
# car['price'] = 40000
# print(f"{car['color']} {car['model']} {car['price']}$")

# # Kalit so'z-qiymat juftligini o'chirish
# # Lug'atdagi elementlarni del operatori yordamida o'chiramiz:
# car = {'model':'Malibu', 'color':'Black', 'price':40000}
# print(car)
# del car['color']
# print(car)
