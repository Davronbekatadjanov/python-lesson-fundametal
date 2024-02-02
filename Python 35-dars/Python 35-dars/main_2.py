"""
Mavzu:Fayllar bilan ishlash
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

Bo'lim:2-qism

"""

# Faylni to'liqligacha o'qish

# Boshlanishiga bizga fayl kerak.Keling,kompyuterda yangi
# pi.txt faylini yaratamiz va ichiga quyidagi matnni 
# joylaymiz:
    
# 3.1415926535
# 8979323846
# 2643383279

# Uch qatordan iborat faylimiz pi sonining qiymatini 30
# xona aniqlik bilan saqlaydi.
# Faylni to'liq o'qish uchun quyidagi kodni yozamiz:
    
with open('pi.txt') as fayl:
    pi = fayl.read()
    
# Kodni tahlil qilamiz:

# Birinchi qatorda open() funksiyasi yordamida faylni 
# ochayapmiz. Bunda funksiyaga argument sifatida fayl
# nomini berayapmiz. Bu yerda biz ochayotgan fayl va 
# dasturimiz bir papkada bo'lishi muhim.

# open() funksiyasi faylni obyekt sifatida qaytaradi, 
# as operatori yordamida esa biz obyektimizga fayl deb 
# nom berayapmiz.

# Ikkinchi qatorda .read() metodi yordamida fayl 
# obyektining tarkibidan bizga kerakli matnni olib, 
# yangi, PI o'zgaruvchisiga yuklayabmiz.

# with operatorining vazifasi biz fayl bilan ishlab 
# bo'lganimizdan so'ng faylni yopish. Yuqoridagi misolda, 
# 2-qatordan so'ng Python zudlik bilan faylni yopadi.

# Yuqorida ko'rgan usulimiz fayl bilan ishlashning eng 
# xavfsiz usuli. Aslida biz fayllarni to'g'ridan-to'g'ri 
# fayl=open('pi.txt') yordamida ochishimiz, fayl bilan 
# ishlab bo'lgandan so'ng esa fayl.close() komandasi 
# yordamida faylni yopishimiz ham mumkin edi:

# fayl = open('pi.txt')
# pi = fayl.read()
# print(pi)
# fayl.close()


# Lekin, bu usul xavfli hisoblanadi va tavsiya qilinmaydi. 
# Gap shundaki, open() funksiyasi yordamida faylni ochganimizdan 
# keyin, toki close() metodini chaqirgunga qadar faylimiz ochiq 
# holatda turadi. Agar, faylni vaqtida yopmasak, yoki fayl 
# yopilmasidan avval dasturimiz to'xtab qolsa, fayl tarkibiga 
# ziyon yetishi, ma'lumotlar yo'qotilishi mumkin. Misol uchun, 
# boshqa dasturlarda ham (masalan Microsoft Word) faylni 
# yopmasdan oldin kompyuteringiz o'chib qolsa, yoki dastur 
# behosdan yopilib ketsa faylingizga ziyon yetgani kabi.

# Shuning uchun open() funksiyasiga with orqali murojat 
# qilganimizda, faylimiz with blokining oxirigacha ochiq 
# turadi, va with tugashi bilan, fayl ham yopiladi. 
# Demak fayl ustidagi amallarni biz with bloki ichida 
# bajarib olishimiz kerak.

# Keling endi pi ning qiymatini konsilga chiqaramiz:

print(pi)

# Matn faylda qanday saqlangan bo'lsa, huddi shu ko'rinishda 
# konsolga chiqdi. Saqlangan ma'lumot son bo'lsada, fayldan 
# o'qiganimizda qaytgan qiymat matn ko'rinishida bo'ladi. 
# Matnni songa o'tkazish uchun, unga biroz ishlov beramiz:

# 1 qator oxiridagi bo'shliqlarni olib tashlaymiz
pi = pi.rstrip()
# 2 qator belgisini almashtiramiz:
pi = pi.replace('\n','')
# 3 matnni float (o'nlik) songa o'tazamiz
pi = float(pi)
print(pi)

# .replace() metodi matn takribidagi biror harf yoki belgisi boshqa
# harf yoki belgi bilan alamshtirish uchun ishlatiladi

