"""
Mavzu:While skil amaliyot
Sana:23.01.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
savol = "Sevimli kitobingizni kiriting:"
savol += "(barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): "

while True:
  kitob = input(savol)
  if kitob == 'stop':
      break
print('Raxmat')

# Muzeyga chipta narxi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga 2000 so'm , 7 - 18 gacha 3000 so'm,18-65 gacha 10000 so'm,65 dan kattalarga bepul.Shunday while sikl yozingki,dastur foydalanuvchi yoshini so'rasin va chipta narxini chiqarsin.Foydalanuvchi exit yoki quit deb yoxganda dastur to'xtasin (ikkita shartni ham tekiring).
# Yuqoridagi dasturni turli usullarda yozib ko'rinki (break,ishora yoki tekshirish).
