"""
Mavzu:Ro'yxatlar va List amaliyot
Sana:09.01.2023
Muallif:Atadjanov Daavronbek
telegram:@atadjanovd
"""
# # ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting.
# # Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
# ismlar = ['Ali', 'Hasan va Husan', "G'ani"]
# print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
# print(ismlar[1] + " egizaklar")
# print(ismlar[2] + " g'ildirakni g'iziliatib g'ildratdi")

# # sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat,manfiy,butun,o'nlik).
# # Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring.Ba'zilarini esa amashtiring:

# sonlar = [1,21,-22,203,-10,-25,20.5,36.6]
# sonlar[0] = sonlar[0] + sonlar[-1]
# sonlar[1] = -93
# sonlar[3] = sonlar[3] + 65
# del sonlar[-2]
# print(sonlar)

# # t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zgingiz eng ko'p hurmat qilagan tarixiy shaxslarning,ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# # Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()),quyidagi ko'rinishda chiqaring:

# t_shaxslar = ['Imom Buxoriy', 'al Xorazimiy', ' Alisher Navoiy']
# z_shaxslar = ['Ilon Mask', 'Bill Gets', 'Alisher Usmonov']
# t_shaxs = t_shaxslar.pop(1)
# z_shaxs = z_shaxslar.pop(1)
# print(f"Men tarixiy shaxlardan {t_shaxs} bilan, zamonaviy shaxslardan esa Bill Gets  bilan suhbat qilishni istar edim")

# # friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# friends = []
# friends.append('Ali')
# friends.append('Hasan va Husan')
# friends.append('Amirbek')
# friends.append('Sandibek')
# friends.append('Jahongir')
# friends.append('Dilshod')
# print(friends)

# # Yuqoridagi ro'yxatdan mehonga kela olmaydigan odamlarni .remove() metodi yordamida o'chirib tashlang.
# friends.remove('Hasan va Husan')
# friends.remove('Ali')
# friends.remove('Jahongir')
# print(friends)

# # Ro'yxatning oxiriga,boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.insert(0, 'Ali')
# friends.insert(2, 'Jahongir')
# friends.insert(-1, 'Hasan va Husan')
# print(friends)

# # Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stingizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

# friends = ['Ali', 'Amirbek', 'Jahongir', 'Sandibek', 'Hasan va Husan', 'Dilshod']
# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(2))
# print("Kelgan mehmonlar: ",  mehmonlar)
