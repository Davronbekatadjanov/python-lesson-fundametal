"""
Mavzu:Ro'yxatlar ustida amallar;amaliyot
Sana:10.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# # O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsulga chiqaring.
# davlat = ['Uzbekiston', 'Qozoqiston', 'Germaniya', 'Angliya', 'Shotlandiya']
# # Ro'yxatning uzunligini konsolga chiqaring.
# print("Elementlar soni: ", len(davlat))
# # sorted() funksiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring.
# print(sorted(davlat))
# # asl ro'yxatni qaytadan konsolga chiqaring.
# print(davlat)
# # reverse() metodi yordamida ro'yxatni ortidan boshilab chiqaring.
# davlat.reverse()
# print(davlat)
# # sort() yordamida ro'yxatni avval alifbo bo'yicha,keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlat.sort()
# print(davlat)
# davlat.sort(reverse=True)
# print(davlat)

# # 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
# sonlar = list(range(120,1200,2))
# print(sonlar)
# # Ro'yxatdagi sonlar yig'indisini hisolang va konsolga chiqaring.
# jami = sum(sonlar)
# print("120 dan 1200 gacha bo'lgan juft sonlar yig'indisi: ", jami)
# # Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmasi hisoblang va konsolga chiqaring.
# eng_max = max(sonlar)
# eng_min = min(sonlar)
# print(max(sonlar)-min(sonlar))
# print(f"Eng katta va eng kichik sonlarni ayirmasi: {eng_max-eng_min}")
# # Ro'yxatdagi elementlar sonini hisoblang.
# print("120 dan 1200 gacha juft bo'lgan sonlar nechta: ", len(sonlar))
# # Ro'yxatning boshidan,o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring.
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[260:280])

# # taomlar degan ro'yxat yarating va ichidagi istalgan 5ta taomni kiriting.
# taomlar = ['manti', 'osh', 'somsa', "lag'mon"]
# nonushta = taomlar[:] # taomlar degan ro'yxatdan nusxa olamiz
# # Yangi ro'yxatdan faqat nonushtaga yeyiladigan taomlarni qoldiring va yana 2 ta taom qo'shing.
# nonushta.remove('manti')
# nonushta.remove("lag'mon")
# nonushta.append('non va qaymoq')
# nonushta.append('issiqa non')
# # Ikkala ro'yxatni ham (taomlar va nonushta) ga konsolga chiqaring.
# print("Nonushtaga yeyiladigan taomlar: ", nonushta)
# print(taomlar)
# # Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta [0] = "qaymoq va non" deb qiymat  berib ko'ring.
# nonushta = tuple(nonushta)
# print(nonushta)
# nonushta[0] = "qaymon va non"
# # Type error

