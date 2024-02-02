"""
Mavzu:To'plamlar 
Sana:20.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # To'plamlar

# # Pythonda to'plam (set) yana bir ma'lumot turi bo'lib,ro'yxat va lug'at kabi bir nechta elementlarni saqlashda qo'llaniladi.
# # To'plam yaratish uchun ham lug'atlardagi kabi katta (jinigalak) qavsdan foydalanamiz:
# sonlar = {1,2,3}
# print(sonlar)
# ismlar = {'alijon','valijon','boqijon'}
# print(ismlar)

# # To'plam bir xil elementlarni saqlamaydi:
# sonlar = {1,2,3,3,4,4,5,6,5}
# print(sonlar)

# # E'tibor qiling,yuqoridagi kodning 1-qatorida biz 3,4 va 5 qiymatlarini 2 martadan takrorlab yozganimizga qaramay,to'plam ichida bu sonlar bir martadan saqlandi,xolos.
# # Bo'sh to'plam yaratish uchun set() funksiyasidan foydalanamiz:
# a = set() # bo'sh to'plam 
# # Ro'yxatdan farqli ravishda, set ichidagi elementlar biror tartibda saqlanmaydi va ularga indeks orqali murojaat etib bo'lmaydi.
# sonlar = {1,2,3,3,4,4,5,6,5}
# print(sonlar[0])
# # TypeError:

# # Avvalga bo'limda ko'rganimizdek,to'plamlar biror ro'yxatdan qaytarilgan elemnetlarni o'chirib tashlash uchun juda qulay:

# mevalar = ['olma','anjir','olma','uzum','olma','uzum']
# mevalar = set(mevalar)
# print(mevalar)
# # Yuqoridagi misolda mevalar ro'yxatida olma va uzum bir necha bor takrorlangan edi, biz set() funksiyasi yordamida ro'yxatni to'plamga o'zgartirdik va ortiqcha elementlardan xalos bo'ldik.
# # Agar to'plamni yana ro'yxatga o'tkazish talab qilinsa,list() funksiyasiga murojaat etamiz:

# mevalar = list(mevalar)
# print(mevalar)

# # To'plamga element qo'shish
# # To'plamga yagona element qo'shish uchun .add() metodidan,bir nechta element qo'shish uchun esa .update() metodidan foydalanamiz:
# mevalar = {'anjir','olma','uzum'}
# mevalar.add('banan') # bitta element qo'shamiz
# print(mevalar)

# # .update() metodidan foydalanganda parametr sifatida ro'yxat yoki lug'at uzatishimiz mumkin.

# # To'plamdan element o'chirish
# # To'plamdan element o'chirish uchun .discord() va .remove() metodidan mavjud.
# mevalar = {'anjir','olma','uzum','anor','banan'}
# mevalar.discard('anjir') # discord() metodi yordamida anjir elementini o'chiramiz.
# print(mevalar)
# mevalar.remove('banan') # remove() metodi yordamida banan elementini o'chiramiz.
# print(mevalar)

# # Bu ikki metod bir vazifani bajaradi,ularning o'rtasidagi farq shundaki,agar biz o'chirmoqchi bo'lgan element to'plamda mavjud bo'lmasa, .remove() metodi xato qaytaradi, .discard() esa xato qaytarmaydi.
# sonlar = {1,2,3,4,5,6}
# sonlar.discard(7) # to'plamda 7 yo'q
# print(sonlar)
# sonlar.remove(7) # to'plamda 7 yo'q

# # To'plamdan element o'chirishning (sug'urib olishning) yana bir usuli .pop() metodidir.Lekin to'plam elementlari indeksi mavjud bo'lmagani sababi .pop() metodi to'plamdan tasodifiy elementni sug'urib oladi.

# sonlar = {1,2,3,4,5,6}
# son = sonlar.pop() # sonlardagi 1-elementni sug'urib olishdan .pop() metodi yordamidan foydalanmiz.
# print(son)
# print(sonlar)

# # To'plamlar ustida amallar 
# # To'plamlar matematikada ham keng qo'llanilgani uchun ularning ustida o'ziga xos matemetik amallar bajarilish mumkin.
# # Misol uchun,ikki to'plamni birlashtirish uchun | operatori yoki .union() metodidan foydalanamiz.
# A = {1,2,3,4}
# B = {3,4,5,6}
# C = A|B
# print(C)
# D = A.union(B)
# print(D)

# # Ikki to'plamning kesishmasini (bir xil elementlarini) topish uchun esa & operatori yoki .intersection() metodidan foydalanamiz:
# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A&B)
# # {3,4} A va B uchun umumiy elementlar 
# print(A.intersection(B))

# # Ikki to'plam o'rtasidagi farqni topish uchun esa ayirish (-) operatori yoki .difference() metodidan foydalanamiz.B to'plamning A to'plamdan farq degan (A-B)  A to'plamga kiruvchi,lekin B to'plamda yo'q elementlar tushuniladi.

# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A-B)
# # {1,2} 1 va 2 A da bir B da yo'q
# print(B.difference(A))
# # {5,6} 5 va 6 da bor A da yo'q

# # To'plamlar o'rtasidagi simmetrik farqni to'pish uchun operatori yoki .symmetric_difference() metodidan foydalanamiz.Simmetrik farq deb A va B to'plamfa kiradigan,lekin bir vaqtda ikkalasiga kirmaydigan elementlar tushuniladi.Quyidagi misolda {3,4} elementlari ikkala to'plamda bo'lgani uchun simmetrik farqqa kirmaydi.
# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A^B)
# print(A.symmetric_difference(B))
