
# PyWebIO
# O'rantish: pip install pyweb.io

# Ushbu modul veb-dasturlashdan mutlaqo xabari yo'q
# odamlarga ham sodda veb-dasturlar yaratish imkoniyatini beradi.
# pyWebIO yordamida dasturlashga yangi kirganlar ham konsol
# dasturlarini brauzerda chiroyli ko'rinishda taqdim etishlarii mumkin.

# Keling,quyidagi sodda misolni ko'ramiz.Bu dastur doiraning
# radiusidan uning yuzi va perimetrini hisoblab qaytaradi.
from pywebio.input import input,FLOAT
from pywebio.output import put_text
from math import pi
# def doira():
#     r = input("Doira radiusini kiriting:", type = FLOAT)
#     yuza = pi*(r**2)
#     per = 2*pi*r
#     put_text(f"Doira yuzi {yuza}ga,\nperimetri {per} ga teng")
# doira()

# Dasturni barajarganda pywebio takribidagi input() funksiyasi
# kompyuteringizda veb-brauzer oynasini ochadi va qiymat kiritshni so'raydi:

# Kerakli qiymatni kiritganimizdan so'zng put_text() funksiyasi natijani
# brauzer oyanidan ko'rsatadi:

# Ko'rib turganingizdek,pywebio moduli yordamida sodda dasturlasimizni ham chiroyli
# taqdim etishimiz mumkin ekan.
# Keyingi qismda yuridaggi modullardan foydalangan holda
# bir nechta loyihalar ustida ishlaymiz

# Vaqt o'tishi bilan kutubxona ichidagi modullar yangilarnib
# turishi,turli funksiya va obyektlarning ishlashda o'zgarishlar yuz berishi
# tabiiy.Agar kitobimizda keltirilgan modullar siz kutgandek ishlamasa,har
# bir modulning sahifasidagi qo'llanmaga murojaat eting.

