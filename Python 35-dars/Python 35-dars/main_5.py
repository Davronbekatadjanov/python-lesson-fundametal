"""
Mavzu:Fayllar bilan ishlash
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:5-qism

"""

# Faylga ma'lumot yozish

# # FAYLGA YOZISH

# Ma'lumotlarni saqlashning eng qulay usuli bu faylga yozish. 
# Dasturimiz bajarilishdan to'xtaganidan so'ng, xotiradagi 
# ma'lumotlar o'chib ketishi mumkin, lekin faylga yozilgan 
# ma'lumotlar saqlanib turaveradi. Fayllarni kelajakda 
# qaytdan xotiraga yuklab, dasturimizni to'xtagan joyidan 
# davom etishimiz mumkin. 

# Yuqorida biz faylni ochishda 'open()' funksiyasidan 
# foydalandik, va yagona argument sifatida fayl nomini 
# berdik. Bunda fayl faqatgina o'qish uchun ochiladi, 
# unga yozib bo'lmaydi. Faylga ma'lumot yozish uchun 
# `open()` funksiyasiga murojat qilishda fayl nomidan 
# tashqari yana bir argument beramiz. Ikkinchi argument 
# faylni aynan nima maqsadda ochishimizni bildiradi. 
# Argumentlar quyidagilardan iborat bo'lishi mumkin:

# Yangi faylga yozish

# Yangi faylga ma'lumot yozish uchun open() funksiyasini 
# chaqirishda 'w' (write) argumentidan foydalanamiz. 
# Ochilgan faylga ma'lumot qo'shish uchun esa .write() 
# metodini chaqiramiz.

filename = 'ustozlar.txt' # ochilgan fayl nomi
with open(filename,'w') as file:
    file.write('Hello word') # filega yozilayotgan matn

# Diqqat!!! open() funksiyasini 'w' argumenti bilan 
# chaqirganimizda ehtiyot bo'lishimiz kerak, sababi 
# agar bunday fayl mavjud bo'lsa, uning ichidagi 
# barcha ma'lumotlar o'chib ketadi.

# Filega yozayotgan ma'lumotlarimiz
# matn ko'rinishida bo'lishi kerak.
# Aks holda,dasturimiz xato beradi.

# faylnomi = 'new_file.txt'
# ism = 'olimjon Hasanov'
# tyil = 2004
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism)
#     fayl.write(tyil) #TypeError: write() argument must be str, not int

# Xatoning oldini olish uchun sonlarni avval 
# str() funksiyasi yordamida matnga keltirib olamiz: 
faylnomi = 'new_file.txt'
ism = 'olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism)
    fayl.write(str(tyil)) 

# Fayllar matn formatida yoziladi, va biz ularni 
# istalgan matn muharriri yordamida ochib ko'rishimiz mumkin.

# Afsuski, faylga bir nechta ma'lumot yozganimizda, 
# ma'lumotlar alohida qatordan emas, bir qatorda 
# bir-biriga qo'shib qo'shib yoziladi.

# Buning oldini olishimiz uchun matn so'ngida \n 
# belgisini qo'shib ketishimiz kerak bo'ladi:
    
faylnomi = 'new_file.txt' 
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')

    

    