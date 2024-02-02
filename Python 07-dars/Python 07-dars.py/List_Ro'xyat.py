"""
Mavzu: List(Ro'yxat)
Sana: 08.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # Ro'yxatlar-List
# # Ro'yxat o'z nomi bilan o'zgaruvchi bir nechta qiymatlarni saqlash imkonini beradi.

# mevalar = ['olma', 'anjir', ' shaftoli', "o'rik"]
# narxlar = [12000, 18000, 10900, 22000]
# sonlar = ['bir', 'ikk', 3, 4, 5 ] # aralash ro'yxat
# ism = [] # <- bo'sh ro'yxat 

# # Ro'yxat saqlaydigan o'zgaruvchilar nomlashda -lar (ko'plik) qo'shimchasini qo'shish maqsadga muvofiq bo'ladi (ingliz tilida -s).Misol uchun: mevalar,uylar, cars,toys,books.

# # Ro'yxat elementlari

# # Dasturlash olamida indeks 0 dan boshlanadi!Ya'ni ro'yxatdagi birinchi elementining tartib raqami(indeks) 0 ga, ikkinchi elementining indeksi 1 ga teng va hokazo.

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])
# print("Uchunchi meva: ", mevalar[3])

# # Agar list ichidagi elementlar matn ko'rinishida bo'lsa,ularga string metodlarni qo'llashimiz mumkin:

# mevalar = ['olma', 'anjir','shaftoli', "o'rik"]
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# # List elementlari ustida arifmetik amallar bajarish:

# narxlar = [12000, 18000, 10900, 22000]
# print(narxlar[2] + narxlar[3])

# # Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat etish mumkin.Bu usul Listning uzunligini bilmaganda juda asqatadi.

# sonlar = [10,12,345,-23,445,61,-45,56,-34]
# print(sonlar[-1])

# # Elementlarni qo'shish,o'chirish va o'zgartirish:

# # Elementni o'zgartirish:

# narxlar = [12000, 18000, 10900, 22000]
# narxlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narxlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narxlar[3] = narxlar[3] + 2000 # 4-qiymatga 2000 qo'shamiz 
# print(narxlar)

# # Mavjud bo'lmagan indeksga qiymat yuklab bo'lmaydi:

# # Yangi element qo'shish 
# # Ro'yxatga element qo'shishning ikkita usuli bor.

# # Birinchi usul: .append() metodi yordamida ro'yxatning oxiriga qiymatni qo'shish:
# mevalar = ['olma', 'anjir','shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz.
# print(mevalar)

# # .append() metodi bo'sh ro'yxatni to'ldirishda juda qulay.Odatda,dastur boshida bo'sh ro'yxat yaratilib,dastur davomida ro'yxat foydalanuvchi tomonidan to'ldirib borilishi odatiy hol.

# cars = [] # bo'sh ro'yxat yaratamiz:
# cars.append('Lacetti') # ro'yxatga Laccetti qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 qo'shamiz 
# cars.append('Cobalt') # ro'yxatga Cobalt qo'shamiz
# print(cars)

# # Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz. .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:

# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# print(cars)

# cars.insert(0, 'Malibu')
# print(cars)

# cars.insert(2, 'Damas')
# print(cars)

# # Elementni o'chirish
# # Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini bilishimiz lozim.
# # Elementni indeks yordamida olib tashlash uchun del operatoridan foydalanamiz
# mevalar = ['olma', 'anjir','shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz 
# print(mevalar)

# # Elementning qiymati bo'yicha o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz.Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz.

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli')
# print(mevalar)

# # .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi.Agar ro'yxatning ichidagi 2 va ndan ko'p bir xil qiymatli elementlar bo'lsa,ulardan faqat birinchi o'chadi.

# hayvonlar = ['it', 'mushuk', 'sigir', 'quyon', 'mushuk']
# hayvonlar.remove('mushuk')
# print(hayvonlar)

# # Elementni sug'irib olish

# # Ba'zida biror elementni butunlay olib tashlash emas,balki uni  ro'yxatdan sug'irib olib,foydalanish talab qilinadi.Buning uchun Pythonda .pop() metodidan foydalanamiz.

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # 4-elementni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# # Agar .pop() metodida indeks berilmasa,ro'yxatdan oxirgi qiymat sug'urib olinadi.

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers.pop()
# print(numbers)

