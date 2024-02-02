"""
Mavzu:Bir necha shartlarni tekshirish
Sana:12.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# # Bir necha shartlarni tekshirish
# # if yordamida biz faqatgina bitta shartni tekshira olamiz va uning natijasiga ko'ra (True/Faldse) dasturlarimiz ma'lum bir amallarni bajaradi.Agar dastur davomida bir nechta shartlarni teshirish talab qilinsa,if-elif-else ketma-ketligidan foydalanamiz.
# # elif-else va if so'zlarining jamlanmasi bo'lib "aks holda,agar"deb tarjima qilinadi.
# # if bilan boshlangan ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin:
# son = int(input("Son kiriting:"))
# if son>0: # agar son 0 dan katta bo'lsa
#   print("Son musbat")
# elif son<0: # agar son 0 dan kichik bo'lsa
#   print("Son manfiy")
# else: # aks holda 
#   print('Son 0 ga teng')

# # if-elif-else ketma-ketligida Python  avva if shartini tekshiradi,shart bajarilmasa,elif ga o'tadi,birinchi elif sharti bajarilmasa,keyingi elif ga o'tadi va hokazo davom etaveradi.
# # if-elif-else ketma-ketlikda biror shart bajarilishi bilan Python qolgan shartlarni tekshirmaydi.
# # Keling,bir misol ko'rib chiqamiz.Deylik,hayvonot bog'iga kirish narxlari quyidagicha begilangan:
# # 4 yoshdan kichik bolalarga kirish bepul.
# # 4 yoshdan 12 yoshgacha kirish 5000 so'm.
# # 12 yoshdan kattalarga 10000 so'm.
# # Foydalanuvchining yoshini so'rab,hayvonot bog'iga kirish chiptasi narxini chiqaruvchi dastur yozamiz.
# yosh = int(input("Yoshingiz nechida?:"))
# if yosh<4:
#   print("Sizga kirish bepul")
# elif yosh<=12:
#   print("Sizga kirish 5000 so'm")
# else:
#   print("Sizga kirish 10000 so'm")

# Dasturimiz avval foysalanuvchining yoshini so'raydi.Birinchi shart yosh 4 dan kichik ekanligini tekshiradi.Agar bu shart bajarilsa,shartlarni tekshirish shu yerdayoq to'xtaydi va keyingi shartlar tekshirilmaydi:
# Yoshingiz nechida? 3
# Sizga kirish bepul
# Agar yosh<4 shati bajarilmasa,keyingi elif yosh<=12 sharti tekshiriladi,agar shart bajarilsa,quyidagi natija chiqadi:
# Yoshingiz nechida? 8
# Sizga kirish 5000 so'm
# Agar yuqoridagi ikki shart ham bajarilmasa,navbat o'z-o'zidan else ichidagi kodga keladi:
# Yoshingiz nechida? 40
# Sizga kirish 10000 so'm

# # if-elif-else ketma-ketligida  shartlarning tartibi juda muhim.Agar yuqoridagi kodimizda biz dastavval foydalanuvchi 12 dan kichikligini tekshiradigan bo'sak,dasturimiz biz kutgan natijani bermaydi:
# yosh = int(input("Yoshingiz nechida?:"))
# if yosh<12:
#   print("Sizga kirish 5000")
# elif yosh<4:
#   print("Sizga kirish bepul")
# else:
#   print("Sizga kirish 10000")

# # Kod yozishda yaxshi amaliyotlardan biri kodlarni qisqa yozish va buyruqlarni qayta-qayta takrorlamaslikdir.Bu keljakda kodni o'zgartirishda ham juda qo'l keladi.
# # Avvalgi dasturda ham print() funksiyasini bir necha bor takrorlamaslik uchun kodimizni quyidagicha o'zgartiramiz:
# yosh = int(input("Yoshingiz nechida?:"))
# if yosh<=4:
#   price = 0
# elif yosh<=12:
#   price = 5000
# else:
#   price = 10000
# print("Sizga kirish ", price, " so'm")

# # Bu kelajakda kodimizga o'zgartirish kirtishni ham oson qiladi.Misol uchun,hayvonot bog'i 65 dan katta bo'lgan qariyalar uchun chegirma e'lon qilsa,kodimizni quyidagicha yagilab qo'yamiz:
# yosh = int(input("Yoshingiz nechida?:"))
# if yosh<=4:
#   price = 0
# elif yosh<=12:
#   price = 5000
# elif yosh<65:
#   price = 10000
# else:
#   price = 8000
# print(f"Sizga kirish {price} so'm")

# # if-elif-else zanjirida ham else qismi mahburiy emas:
# yosh = int(input("Yoshingiz nechida?:"))
# if yosh<=4:
#   price = 0
# elif yosh<=12:
#   price = 5000
# elif yosh<65:
#   price = 10000
# elif yosh>=65:
#   price = 8000
# print(f"Sizga kirish {price} so'm")

# # And va or opertorlari
# # Yuqoridagi misollarda if yoki elif dan so'ng biz faqatgina bitta shartni tekshiradik.Agar bir vaqtning o'zida bir nechta shartlarni tekshirish talab qilinsa,buning uchun maxsus AND va OR operatorlari mavjud.
# # OR operatori 
# # OR ingliz tilidan "yoki" deb tarjima qilinadi va ikki va undan ko'p shartlardan biri bajarilishini tekshirishda ishlatiladi.Demak,dasturning biror qismi bajarilishi uchun bir nechta shartlardan birining to'g'ri (True) bo'lishi kifoya bo'lsa OR operatoridan foydalanamiz.
# # Quyidagi misoga qaraylik,foydalanuvchidan hafta kunini so'raymiz,agar kun shanba yoki yakshanba bo'sa,bugun dam olish kuni degan xabarni chiqaramiz,aks holda,bugun ish kuni degan xabarni chiqaramiz.
# kun = input("Bugun nima kuni?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#   print("Dam olish kuni.")
# else:
#   print("Bugun ish kuni.")
  
# # 2-qatordagi or operatoriga e'tibor qiling,bu operator kun.lower()=='shanba' yoki kun.lower()=='yakshanba': shartlaridan biri bajarilsa,TRUE qiymatin qaytaradi.
# # Bugun nima kun?>>>shanba
# # Bugun dam olish kuni.
# # Yana ham tushunarli bo'lishi uchun quyidagi kodlarni bajarib ko'ramiz:
# print(True or False)
# print(True or True)
# print(False or False)

# # AND operatori
# # AND inliz tilidan "va" deb tarjima qilinadi va ikki va undan ko'p shartlarning barchasi bajarilishini tekshirishda ishlatiladi.AND operatori bilan yozilgan shartlarning barchasi bajarilgandagina TRUE qiymati qaytaradi,shartlardan biri bajarilmay qolsa ham,FALSE qiymati qaytaradi:
# # Quyidagi misolni ko'ramiz:
# kun = input("Bugun nima kuni?>>>")
# harorat = float(input("Havo harorati qanday?>>>"))
# if kun.lower()=='yakshanba' and harorat>=35:
#   print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#   print("Uyda dam olamiz!")

# 3-qatordagi and operatori kun.lower()--=='yakshanba': va harorat>=30: shartlarining ikkisi ham bajarilgandagina TRUE qiymatini qaytaradi,aks holda,qiymat FALSE bo'ladi.

# # Bir necha shartlarni ketma-ket yozish
# # Shartlarni yozishda bir nechta and va or operatorini aralashtirib ham yozish mumkin:
# kun = input("Bugun nima kuni?>>>")
# yosh = int(input("Yoshingiz nechida?>>>"))
# if (yosh<7 or yosh>65) and kun=='chorshanba':
#    print("Bugun siz uchun Muzeyga kirish bepul")

# # Boolean ma'lumotlar turi.

# # Yuqorida taqqoslash operatorlari yordamida turli ifodalarni solishtirishda TRUE yoki FALSE qiymatlari qaytishini ko'rdik.Bu qiymatlar boolean (mantiqiy) qiymatlar deb ataladi va dasturlashda juda keng qo'llaniladi.
# # Boolean ma'lumot turini ham xuddi son yoki matn kabi o'zgaruvchilarda saqlash mumkin.
# a = True
# b = False

# # Quyidagi dasturga e'tibor bering.Returanimizga kelgan mijoz 15000 so'mlik taom oldi,biz mijoz qo'shimcha choy va salat ham olganiga (olmaganiga) qarab ularning narxini ham yakuniy narxga qo'shishimiz kerak.Mijozning choy bilan belgilaymiz:
# narx = 15000 # mijoz 15000 so'mga taom oladi.
# choy = True # mijoz choy ham oladi.
# salat = False # mijoz salat olmadi.

# if choy and salat: # agar mijoz choy va salat olgan bo'lsa.
#   narxlar = narx + 10000 # narxga 10000 so'm qo'shamiz.
# elif choy or salat: # agar choy yoki salat olgan bo'lsa.
#   narx = narx + 5000 # narxga 5000 so'm qo'shamiz.
# print(f"Jami {narx} so'm") # yakuniy narxni chiqaramiz.

# # E'tibor bering,choy va salat boolean (mantiqiy) qiymatlar bo'lgan uchun if va elif shartlarida biz choy==True yoki salat==True deb yozib o'tirishimiz shart emas.
# # Yuqoridagi misolda choy = True(choy) va salat = False(salat olmadi) bo'lgani uchun yakuniy narx narx+5000=20000 chiqdi.
# # Pythonda True va False qiymatlari o'rniga 1 va 0 sonlarini ham ishlatish mumkin.

# # Shartlarni krtma-ket tekshirish
# # if-elif-else zanjirning kamchiliklaridan biri-shartlardan biri bajarilishi bilan qolgan shartlar tekshirilmaydi.Shuning uchun shartlarni ketma-ket tekshirish uchun har bir shartni alohida if bilan ajratish talab qilinadi.
# # Avvalgi bo'limda ko'rgan misolni kengaytiraylik.
# narx = 15000 # mijoz 15000 so'mga ovqat oladi.
# choy = True # mijoz choy ham oladi.
# salat = False # mijoz salat olmadi.
# non = True # mijoz non ham oladi.
# kompot = True # mijoz komput ham oladi.
# assorti = False # mijoz assorti ham olmadi.

# if choy: # agar choy olsa,
#   print("Mijoz choy oldi.")
#   narx = narx + 3000 # narxga 3000 so'mga qo'shamiz.
# if salat: # agar salat olsa,
#   print("Mijoz salat oldi.")
#   narx = narx + 5000 # narxga 5000 so'mga qo'shamiz.
# if non: # agar non olsa,
#   print("Mijoz non oldi.")  
#   narx = narx + 2000 # narxga 2000 so'mga qo'shamiz.
# if kompot: # agar komput olsa,
#   print("Mijoz kompot oldi.")
#   narx = narx + 5000 # narxga 5000 so'mga qo'shamiz.
# if assorti: # agar assorti olsa,
#   print("Mijoz assorti oldi.")
#   narx = narx + 15000 # narxga 15000 so'mga qo'shamiz.
# print(f"Jami {narx} so'm") # yakuniy narxni chiqaramiz.

# # Yuqoridagi dasturda har bir if alohida tekshiriladi,avvalgi yoki keyingi if ga bog'liq emas.

# # Ro'yxat tarkibini tekshirish
# # in operatori 
# # in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini teshirishimiz mumkin.

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# 'manti' in menyu #  munyu da manti bormi?
# # False
# menyu = ['osh', 'qozonkabob','shashlik', 'norin','somsa']
# 'osh' in menyu # menyu da osh bormi?
# # True
# menyu = ['osh', 'qozonkabob','shashlik', 'norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menyu:
#   print('Buyutma qabul qilinadi.')
# else:
#   print('Afsuski,bizda bunday ovqat yo\'q')

# # not in operatori 
# # not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.
# menyu = ['osh', 'qozonkabob','shashlik', 'norin','somsa']
# 'manti' not in menyu # menyu da manti yoqmi?
# # True 
# menyu = ['osh', 'qozonkabob','shashlik', 'norin','somsa']
# 'osh' not in menyu # menyu da osh yoqmi?
# # False 
# menyu = ['osh', 'qozonkabob','shashlik', 'norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menyu:
#    print('Afsuski,bizda bunday ovqat yo\'q.')
# else:
#   print('Buyutma qabul qilinadi.')

# not operatorini boshqa shartlarning oldidan ham qo'yishimiz mumkin.Misol uchun,not a==5 ifodasi a!=5 ifodasi bilan bir xil natija qaytaradi.

a = 6
a!=5 
# True
not a==5
# True
not False
# True
not True
# False

# # Ikki ro'yxatni solishtirish
# # Ikki ro'yxatning tarkibini tekshirish uchun for sikli va yuqoridagi in operatoridan foydalanamiz:
# meny = ['osh', 'qozonkabob','shashlik', 'norin','somsa']
# buyurtmalar = ['osh','shashlik', 'manti','somsa']
# for taom in buyurtmalar:
#   if taom in meny:
#     print("Menyuda ",taom, " bor")
#   else:
#     print(f"Kechirasiz,menyuda {taom} yo'q")

# # Ro'yxat bo'sh emasligini tekshirish 
# # Yuqoridagi dasturimizda biz foydalanuvchi buyurtma berdi deb tasavvur qilyabmiz.Lekin foydalanuvchidan bo'sh ro'yxat kesa-chi?Demak,for siklini bajarishdan avval ro'yxat bo'sh emasligiga amin bo'lishimiz kerak.Buning uchun ro'yxat uzunligini tekshirib ko'ramiz.Agar ro'yxat uzunligi 0 ga teng bo'lsa,bu bo'sh ro'yxatdir. 
# list1 = [1,2,3]
# len(list1)>0
# # True
# list2 = [] # bo'sh ro'yxat.
# len(list2)>0
# # False
# # Lekin Pythonda ro'yxat bo'sh yoki bo'sh emasligini tekshirishning bundan ham oson yo'li bor.Buning uchun if operatoridan so'ng ro'yxat nomini yozish kifoya.Agar ro'yxatda bir dona element bo'lsa ham,bu ifoda True qiymatini,aks holda,False qiymatini qaytaradi.
# list1 = [1,2,3]
# if list1: # bu ifoda True qaytaradi,sabab,list1 bo'sh emas.
#   print("Ro'yxatda elementlar bor")
  
# # Yuqorida usuldan foydalanib avvalgi bo'limda ko'rgan dasturga o'zgartirish kiritamiz:
# meny = ['osh', 'qozonkabob','shashlik', 'norin','somsa']
# buyurtmalar = ['osh','shashlik','manti','somsa']
# if buyurtmalar:
#   for taom in buyurtmalar:
#     if taom in meny:
#       print("Menyuda ",taom, " bor")
#     else:
#       print(f"Kechirasiz,menyuda {taom} yo'q")
      