
# requests

# O'rantishlish: pip install reaquests

# Bu paket yordamida Pythonda veb sahifalarga murojaat
# etishimiz(so'rov yuborishimiz) va ulardan qaytgan ma'lumotlar ustida
# turli amallar bajarishimiz mumkin.Misol uchun,quyida
# requests yordamida
# kun.uz sahifasini to'liqligicha tortib olamiz.Natija
# juda ham uzun bo'lgani uchun bu yerda keltirmadik.
# Kodni o'zingiz bajarib ko'rishingiz mumkin.

import requests
from pprint import pprint


# manzil = "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)


# Ko'pincha requests paketidan API-lar bilan ishlashda foydalaniladi.
# API ma'lum bir veb xizmatga so'rov yuborish orqali undan foydalanish.
# Misol uchun,Yandex tarjimonga yoki Google xaritalari xizmatiga requests
# paketi yordamida API so'rov yuborish va o'zimizga kerakli
# ma'lumotlarni olishimiz mumkin.API haqida internetda ko'proq
# ma'lumot olishingiz mumkin.Biz esa sodda misol bilan cheklanamiz.

# Internetda restcountries.eu sahifasi mavjud.Bu sahifa
# orqali dunyodagi davlatlar haqida turli ma'lumotlarni
# olishingiz mumkin.Sahifadan foydalanish qulay bo'lishi uchun
# esa sahifa yaratuvchilari bir nechta tayyor API-lar e'lon
# qilishgan.Misol uchun,O'zbekiston haqida ma'lumot olish uchun
# quyidagi manzilga so'rov yuborasiz:https://restcountries.eu/rest/v2/name/Uzbekiston

# API dan qaytgan natija JSON (lug'at ) ko'rinishda bo'ladi va biz bu
# lug'atdan o'zimizga kerakli ma'lumotni sug'urib olishimiz mumkin.
# Misol uchun,quyidagi kodimiz APIga yuborilgan davlatning poytaxtini
# ko'rsatadi.

capital = "Uzbekistan"
url = f"https://restcountries.com/v3.1/capital/{capital}"
r = requests.get(url)
r_json = r.json()
print(r_json)


