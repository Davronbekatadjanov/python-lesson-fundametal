"""
Mavzu: Ro'yxatlar bilan ishlash
Sana:09.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd

"""

# # Ro'yxatlar bilan ishlash 

# # Ro'yxatni tartiblash
# # Aksar holatlarda ro'yxat ichidagi elementlarni alifbo kema-ketligida tartiblash talab qilinishi mumkin. Buning uchun maxsus .sort() metodidan foydalanamiz.

# cars = ['bmw', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)
# # Tartiblashda bosh harflar kichik harflardan avval kelishini hisobga oling.Agar ro'yxatdagi so'zlarning harfi katta-kichik aralash yozilgan bo'lsa,ular bir ko'rinishiga keltirib olish maqsadga muvofiq bo'ladi.

# cars = ['bmw', 'Gm', 'tesla','volvo', 'audi', 'mercedes']
# cars.sort()
# print(cars)

# # Yuqoridagi misolda GM element bosh harf bilan boshlangani uchun ro'yxatning boshidan joy oldi.
# # Ro'yxatni teskari tartiblash uchun .sort() metodi ichida reverse-True argumentini ham yozamiz.
# cars = ['bmw', 'gm', 'tesla','volvo', 'audi','mercedes']
# cars.sort(reverse=True)
# print(cars)

# # .sort() metodi bevosita berilgan ro'yxatni tartiblaydi(ya'ni ichki elementlarining joylashuvini o'zgartiradi.)
# # Ba'zi holatlarda asl ro'yxat ichidagi elementlarning kema-ketligini buzmagan holda, ro'yxat tarkibini tartiblangan ko'rinishida chiqarish talab qilinish mumkin.Buning uchun sorted() funkisiyasidan foydalanamiz.

# mehmonlar = ['Amirbek', 'Dilshodbek', 'Sandibek', 'Rasul', 'Avazbek']
# print(f"sorted() qaytargan ro'yxat: {sorted(mehmonlar)}")
# print(f"Asl ro'yxat o'zgarmas qoladi: {mehmonlar}")
# # ikkinchi ko'rinishi
# print("sorted() qaytargan ro'yxat: ", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoladi: ", mehmonlar)

# # sorted() funkisiyasi yordamida teskari tartiblash uchun bazi reverse=True argumentini ishlatishimiz:
# print(sorted(mehmonlar, reverse=True))

# # Yuqoridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin:

# ages = [12,98,34,65,34,76,11,]
# ages.sort()
# print(ages)

# # Ro'yxatni aylantirish

# # Ba'zida ro'yxatni (boshini oxiriga,oxirini boshiga qilib) aylantirish talab qilinishi mumkin.Buning uchun .reverse() metodidan foydalanamiz.
# fruits = ['pear', 'banan', 'apple', 'watermelon', 'lemon']
# fruits.reverse()
# print(fruits)

# # Ro'yxatning uzunligi topish

# # Ro'yxatning uzunligi,ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funkisiyasidan foydalanmiz.
# fruits = ['pear', 'banan', 'apple', 'watermelon', 'lemon']
# print(f"Elementlar soni: {len(fruits)}")

# # range() funkisiyasi 
# # Bu funksiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list() funksiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz.

# sonlar  = list(range(0,10))
# print(sonlar)

# # Yuqoridagi misolda range(0,10) funksiyasi 0 dan 9 gacha sonlar ketma-ketligini shakllantirdi. list() funksiyasi esa bu ketma-ketlikni ro'yxatga aylatiradi.

# # E'tibor qiling,range() fuksiyasi ikkinchi indeksdan bitta avval to'xtaydi.
# # ranfe() yordamida qadamni ham berishmiz mumkin.

# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam bilan 
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# # Agar sonlar ketma-ketligi 0 dan boshlansa,range() funksiyasida ikkinchi argumentni ko'rsatish kifoya.Misol uchun,range(0,10) emas, range(10) deb yozsak ham bo'laveradi.

# # Sonli Ro'yxat ustida sodda ammalar

# # Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin.Masalan,ro'yxatdagi eng kichik sonni topish uchun min() funkisyasidan,eng katta sonni topish uchun max() funkisyasidan,sonlarning yig'indisini topish uchun esa sum() funksiyasidan foydalanamiz.

# narxlar = [12000,22500,23456,9800,5600,9934,32874]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon narx ", arzon, \
#       ".Eng qimmat narx ", qimmat, \
#       ". Jami: ", jami)

# print(f"Eng arzon narx: {arzon}. Eng qimmat narx: {qimmat}. Jami: {jami}")
# # Agar bir qatorga yozilayotgan kodingiz juda uzun bo'lib ketsa , \ belgisi yordamida kodni yangi qatordan davom ettirishingiz mumkin.

# # Ro'yxatni kesish

# # Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin.Deylik,biz quyidagi cars degan ro'yxatdan birinchi 3 ta elementni ajratib olmoqchimiz,buning uchun boshlang'ich va oxirgi indekslarni beramiz:

# cars = ['bmw', 'honda', 'ford', 'audi', 'toyota', 'gm']
# my_cars = cars[0:3] # 0 dan boshlab 3 ta element ajratib olamiz 
# print(my_cars)

# # Python ro'yxatni kesishda 2-ko'rsatilgan indeksdan bitta avval to'xtaydi.Yuqoridagi misolda ham 0,1,2-elementlar ajratib olinadi.
# # Bu usul bilan ro'yxatnimg istaljoyidan bolishimiz mumkin.
# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz

# # Agar boshlang'ich indeksni bermasangiz,Python avtomat ravishda 0-indeksdan boshlab kesadi.Agar 2-indeksni kiritmasangiz,ro'yxat oxirigacha kesadi.
# print(cars[:4]) # Ro'yxat boshidan 4 ta element ajratish 
# print(cars[2:]) # 2-elementdan ro'yxat oxirigacha kesish

# # Ro'yxatni nusxalash

# # Dastur davomida biror ro'yxatdan nusxa olish talab qilinishi mumkin.Buning uchun tenglik (=) belgisidan foydalansak bo'ladimi?Quyidagi misolga e'tibor bering:

# sonlar = [1,2,3,4,5] # sonlar degan ro'yxat yaratamiz
# sonlar2 = sonlar  # sonlar2 degan ro'yxatni sonlarga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati: ", sonlar,\
#       ".\n Bu sonlar2 ro'yxati: ", sonlar2)

# # Natija biz kutgandek chiqdimi? Yo'q.Biz 6 va 7 sonlarini sonlar2 degan ro'yxatga qo'shgan edik,lekin bu ikki son sonlar degan asl ro'yxatga ham qo'shilib qoldi.Nima uchun?
# # Gap shundaki,sonlar2=sonlar deb yozgan komandamiz yangi ro'yxat yaratish o'rniga ikkala o'zgaruvchini ham xotiradagi biita ro'yxatga bo'g'lab (yo'naltirib) qo'ydi.Ya'ni bitta ro'yxat ikki nomga ega bo'lib qoldi.Endi sonlar yoki sonlar2 ustida bajargan amallarimiz xotiradagi bitta ro'yxat ustida bajarilaveradi.

# # Unda qanday qilib ro'yxatdan nusxa olamiz?Buning uchun yuqoridagi kabi ro'yxatni kesish usulidan foydalanmiz.Ya'ni ro'yxatning boshidan oxirigacha "kesish" yangi ro'yxatga yuklaymiz.Bunda kvadrat qavs ichida boshlang'ich va yakuniy indeksni ko'rsatish shart emas.

# sonlar = [1,2,3,4,5] # sonlar degan ro'yxat yaratamiz 
# sonlar2 = sonlar[:] # ro'yxatni to'liq ko'chirib oladi.
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz 
# print("Bu sonlar ro'yxat: ", sonlar,\
#      ".\n Bu sonlar2 ro'yxati: ", sonlar2)
# # ikkinchi ko'rinishi
# print(f"Bu sonlar ro'yxati:  {sonlar}, \nBu sonlar2 ro'yxati: {sonlar2}")

# # Tuples -- o'zgarmas ro'yxatlar 
# # Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin.Tuple ichidagi qiymatlar bir marta,dastur boshida beriladi,so'ngra o'zgartirib bo'lmaydi.Listdan farqli ravishda,Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:

# tomonlar  = (20,30,55.2)
# print(tomonlar)

# # Tuple ichidagi elementlarga xuddi ro'yxat elementlariga murojaat etilgan kabi indeks bilan murojaat etilaveradi:
# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# # Keling,Tuple ichidagi biror elementning qiymatini o'zgartirib ko'ramiz:
# toys = ('bus','car', 'bear', 'dino','snake', 'lizard')
# toys[3] = 'dragon'
# # TypeError berdi 
# # Ko'rib turganingizdek,bu operatsiya xatolikka olib keldi.Shu kabi o'zgarmas ro'yxatdan biror elementni o'chirish yoki yangi element qo'shish ham mumkin emas. 
# # Agar tuple ga o'zgartirish talab qilinsa,yagona yo'li o'zgarmas ro'yxatni list() funkisyasi yordamida oddiy ro'yxat ko'rinishiga keltirib olish,o'zgarishlarni bajarish va ro'yxatni qaytarib tuple() funkisyasi yordamida o'zgarmas ro'yxatga konvertatsiya qilishdir:

# # o'zgarmas ro'yxat yaratamiz
# toys = ('bus', 'car', 'bear', 'dino','snake', 'lizard')
# # o'zgarmas ro'yxatni oddiy ro'yxatga aylatiramiz
# toys = list(toys) # (List)
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen' 
# # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz 
# toys = tuple(toys) 
# print(toys)

