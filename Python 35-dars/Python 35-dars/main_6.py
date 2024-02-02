"""
Mavzu:Fayllar bilan ishlash
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:6-qism

"""
# Faylga ma'lumot qo'shish

# Agar mavjud faylga ma'lumot qo'shish talab qilinsa, 
# open() funksiyasiga murojat qilishda 'a' (append) 
# argumentidan foydalanamiz. Bunda yangi qo'shilgan 
# ma'lumotlar faylning oxiriga qo'shiladi.

faylnomi = 'new_file.txt' 
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')  
with open(faylnomi,'a') as fayl:
    fayl.write('Alijon Valiyevin\n')
    fayl.write('2000')

# Agar biz ochayotgan fayl mavjud bo'lmasa.
# Python yangi fayl yaratadi.

# O'zgaruvchilarni faylda saqlash

# Yuqorida biz ma'lumotlarni matn ko'rinishida 
# saqlashni ko'rdik. Agar dastur davomida turli 
# o'zgaruvchilarni faylda saqlash talab qilinsa 
# pickle modulidan foydalanamiz. Pickle ma'lumotlarni 
# biz qanday ko'rinishda bersak, shunday ko'rinishda 
# faylga yozadi. Yuqoridagi usuldan farqli ravishda, 
# pickle yordamida yozilgan fayllarning tarkibini 
# Pythondan tashqarida ko'rib bo'lmaydi.

# Picke faylga yozish

# Pickle dan foydalanish uchun biz avval bu modilni 
# import qilamiz. Faylni ochishda esa, open() 
# funksiyasiga ikkinchi argument sifatida 'wb' 
# (write binary) beramiz, ya'ni ikkilik sanoq 
# tizimida yozishni ko'rsatamiz. Faylga yozish 
# uchun esa pickle.dump() metodidan foydalanamiz

import pickle
talaba1 = {
    'ism':'hasan',
    'familiya':'husanov',
    'tyil':2003,
    'kurs':2}
talaba2 = {
    'ism':'alijon',
    'familiya':'valijev',
    'tyil':2004,
    'kurs':1}

with open('info','wb') as file :
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

# E'tibor bering, yuqorida fayl nomini yozishda 
# uning turini ko'rsatmadik, sababi, avval 
# aytganimizdek bu fayllar Pythondan tashqarida 
# ochilmaydi va biz buning oldini olishimiz kerak. 
# Aslida fayl nomiga .txt qo'shimchasini ham 
# qo'shishimiz mumkin, bu bilan dastur xato ishlamaydi, 
# lekin bu bizni kelajakda chalg'itishi mumkin. 

# Istasangiz faylga .dat (data so'zidan olingan) 
# qo'shimchasini qo'shib qo'yishingiz mumkin (info.dat).

# Pickle fayldan o'qish

# Pickle fayldan o'qish uchun open() funksiyasini 
# 'rb' (read binary) argumenti bilan chaqiramiz. 
# O'zgaruvchilarni bitta faylga yozganimizda, har bir 
# o'zgaruvchi alohida qatordan yoziladi. Fayldan 
# o'qishda ham har bir qatorni alohida o'qishimiz kerak bo'ladi:

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
 
# O'zgaruvchi tarkibini ko'ramiz:
    
print(talaba1)
print(talaba2)


# Adashib ketmaslik uchun alohida o'zgaruvchilarni 
# alohida fayllarga saqlash tavsiya qilinadi.

     