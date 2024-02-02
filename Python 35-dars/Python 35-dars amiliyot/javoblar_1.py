"""
Mavzu:Fayllar bilan ishlash
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Amaliyot:
Bo'lim:1-qism

# """
# Bugun o'rgangan narsalaringizni matnga 
# yozing va matnni Python yordamida oching

faylnomi = 'hello_world.txt'
with open(faylnomi,'w') as fayl:
    fayl.write('Hello world\n')
    fayl.write("Hello")

with open(faylnomi) as fayl:
    hw = fayl.read()
print(hw)

# Ushbu bog'lanadigan https://xli.xo/DA-pi_million_digits.txt
# faylini yuklab oling (faylda pi son nuqtadan so'ng milion xona 
# aniqlik bilan yozilgan)

with open('pi_million_digits.txt') as file :
    pi=file.read()
print(pi)
pi=pi.rstrip() # qator oxiridagi bo'shliqni olib tashlash
pi = pi.replace('\n','')
pi = pi.replace(' ','')
# print(pi)

# Sizning tug'ilgan kuningiz 
# # π soni tarkibida uchraydimi yoki yo'q 
# ekanligini aniqlovchi funksiya yozing. 
# Misol uchun, tug'ilgan sanangiz 14 dekabr, 
# 2005-yil bo'lsa, 14122005 ketma-ketligi 
# yuqoridagi matnda uchraydimi yo'q toping.

# Fayl ichidagi matnni float ma'lumot turiga 
# o'tkazing va pickle yordamida yangi faylga saqlang.

# Tug'ilgan kunim pi da bormi?
bdate = '14122005'
# print(bdate in pi)

pi = float(pi) # matnni float (o'nlik) songa 
# o'tkazamiz
import pickle
with open('pi_float.dat','wb') as file:
    pickle.dump(pi,file)

# Foydalanuvchidan turli hil ma'lumotlarni so'rab, 
# har bir kiritilgan ma'lumotni yangi qatordan faylga 
# yozib boruvchi dastur tuzing. Dastur qayta chaqirilganida 
# yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas).

while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('books.txt','a') as file:
        file.write(book+'\n')
with open('books.txt') as file:
    bk=file.read()
print(bk)

