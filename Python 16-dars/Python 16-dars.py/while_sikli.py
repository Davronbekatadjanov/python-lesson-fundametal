"""
Mavzu:while sikli
Sana:23.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # While sikli
# # Biz 3-bob for sikl yordamida kodning ma'lumot bir qismini bir necha bor takrorlashni o'rgangan edik.Ushbu bobda esa while sikli bilan tanishamiz.Bu ikkisining o'rtasidagi farq shundaki,for siklining takrorlanishi biror ro'yxat (lug'at,to'plam) elementlari soniga bog'langan bo'lsa,while tsiklining takrorlanishi biror shartning qanoatlanishiga bog'langan bo'ladi.

# # "while" so'zi ingliz tilidan "toki" deb tarjima qilinadi.

# # While qanday ishlaydi?
# # while sikli badanidagi kodning nechta marta takrorlanishi biror shartga bog'langan bo'ladi.Tushunarli bo'lishi uchun quyidagi misoni ko'zdan kechiramiz:
# son = 1
# while son<=5: # toki son 5 dan kichik yoki teng ekan . . .
#   print(son, end=' ') # sonni konsolga chiqaramiz va 
#   son = son+1 # songa 1 ni qo'shamiz.
# # Yuqoridagi dasturni tahlil qilamiz:
# # avval son degan o'zgaruvchi yaratdik va unga 1 qiymatini berdik.
# # 2-qatorda "toki son 5 dan kichik yoki teng ekan" keyingi qatorlarni bajar dedik.
# # 3-qatorda sonni konsolga chiqardik.
# # 4-qatorda son 1 qo'shdik.
# # 4-qatordan so'ng kod yana 2-qatorga qaytadi va son<=5 shartini tekshiradi,agar shart bajarilsa (True),3 - 4-qatorlar takrorlanadi.
# # 5-qatordan so'ng son=5 bo'lganida while sikli to'xtaydi.

# # Pythonda += operatori bor.Bu operator o'ng tarafdagi qiymati chap tarafdagi qiymatga qo'shadi.Misol uchun,yuqorida son = son + 1 ifodasin son += 1 deb yodik.

# # while va input()
# # while sikli yordamida dasturni to'xtatish imkoniyatini fodalanuvchiga berashimiz mumkin:
# print("Kiritilgan sonning kvadratin qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit': # toki qiymat exitga teng emas ekan 
#   qiymat = input(savol) 
#   if qiymat != 'exit':
#     print(float(qiymat)**2)


# # Ishora-Flag
# # Yuqoridagi misolda dasturni to'xtatish uchun yagona shartni tekshirdik (qiymat!='exit').Katta dasturlarda biz emas,bir nechta shartlarni tekshirish va ulardan biri bajarilgan taqdirda dasturni to'xtatish talab qilinishi mumkin.
# # Bunday holatlarda biror o'zgaruvchidan ishora (flag) sifatida foydalanishimiz mumkin.Agar dastur bajarilishi davomida dasturni to'xtatish shartlaridan biri bajarilganda ishora o'zgaruvchining qiymatini o'zgartiramiz va dastur o'z-o'zidan to'xtaydi.

# print("Kiritilgan sonning kvadratin qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(to'xtatish uchun 'exit' deb yozing): "
# ishora = True 
# while ishora: # toki ishora=True ekan 
#   qiymat = input(savol)
#   if qiymat == 'exit':
#     ishora = False
#   else:
#     print(float(qiymat)**2)
    
# # break operatori 
# # break operatori yordamida sikl bajarilishini sikl badanidan to'xtatishimiz mumkin.Ya'ni sikl to'xtashi while dan so'ng yozilgan shartga emas,sikl ichidagi boshqa shartga bog'lanishi mumkin:
# print("Kiritilgan sonning kvadratin qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(to'xtatish uchun 'exit' deb yozing): "
# while True: # abadiy sikl
#   qiymat = input(savol)
#   if qiymat == 'exit':
#     break  # sikl to'xtatish
#   else:
#     print(float(qiymat)**2)

# # break operatori for siklini to'xtatish uchun ham ishlatiladi.
# sonlar = list(range(1,11))
# for son in sonlar:
#   if son == 5: # son 5 ga teng bo'lsa,sikl to'xtaydi
#     break
#   print(f"{son} ning kvadrati {son**2} ga teng")

# # Sikl ichida bir nechta break operatorlari bo'lishi mumkin.

# # Continue operatori
# # continue operatori esa, aksincha,ma'lum bir shart bajarilganda qadam tashlab o'tish uchun mo'ljanllangan.
# sonlar = list(range(1,11))
# for son in sonlar:
#   if son == 5: # son 5 ga teng bo'lsa,sikl boshiga qaytadi
#     continue
#   print(f"{son} ning kvadrati {son**2} ga teng")

# # while sikliga ham misol ko'ramiz.Quyidagi kod 0 dan 10 gacha bo'gan juft sonlarni konsolga chiqaradi:
# son = 0 
# while son<10:
#   son += 1
#   if son%2!= 0: # agar son toq bo'lsa 
#     continue
#   else: # aks holda (juft bo'lsa)
#     print(son, end= ' ')

# # Sikl ichida bir nechta continue operatorlari bo'lishi mumkin.

# # Abadiy sikl tuzog'i 
# # Sikllar bilan ishlashda abadiy sikl yaratib qo'yishdan ehtiyot bo'lishimiz kerak.Abadiy siklga turli mantiqiy xatolar sabab bo'lishi mumkin: noto'g'ri shart,o'zgarmas qiymat,kodlar ketma-ketligida xatolik va hokazo.
# # Dasturingiz abadiy siklga tushib qolganda dasturni to'xtatish uchun konolda (terminalda) Ctrl+C tugmaslarini bosing.

# son = 0 
# while son<10:
#   if son%2!= 0: # agar son toq bo'lsa
#     continue
#   else:
#     print(son)

# # Yuqoridagi kod abadiy davom etadi,sababi,biz sonning qiymatini o'zgartirishni esdan chiqardik:
# # Yana bir misol ko'ramiz:
# son = 0 
# while son<10:
#   if son%2!= 0: # agar son toq bo'lsa
#     continue
#   else:
#     print(son)
#   son += 1

# # Bu kod ham abadiy davom etadi,sababini topa olasizmi?
# son = 1
# while son<0:
#   son += 1
#   if son%2!= 0: 
#      continue
#   else:
#     print(son)

# Yuqoridagi kodda xato shart tufayli (son>0) sikl abadiy aylanadi.
