
# googletrans
# O'rantilishi: pip install googletrans

# Ushbu modul yordamida Googlening tarjimonlik xizmatiga
# murojaat etib,istalgan matnni turli tillarga tarjima
# qilishimiz mumkin.Moduldan foydalanish uchun avval
# googletrans modulidan Translator klassini import qilamiz
# va bu klassdan yangi obyekt yaratamiz(tarjimon).Bevosita
# tajimonlik xizmatiga murojaat etish uchun tajimon obyekti
# ichidagi .translate() metodiga murojaat etamiz va parametr
# sifatida tarjimon qilish kerak bo'lgan matnni uzatamiz.
# .translate() metodi tarjimani obyekt ko'rinishida qaytaradi,
# obyekt ichidan tarjima matnini olish .text xususiyatiga
# murojaat etamiz
from googletrans import Translator
tarjimon = Translator() # Translator - bu maxsus klass (trajimon esa obyekt)
matn_uz = "Python - dunyodagi eng mashhur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)
print(tarjima.origin)
print(tarjima.text)


# googletrans modulini ishlatish uchun kompyuterimiz internet
# tarmog'iga ulangan bo'lishi kerak.

# Agar yuqoridagi kod xato berse(TKK token error),googletrans modulini
# o'chirib tashlab,modulning alfa versiyasini o'rnating:

# pip uninstall googtrans  # modulni o'chirish
# pip install googletrans==3.1 0a0 # yangi versiyani o'rnatish

# Agar matnni boshqa tillarga tarjima qilish kerak bo'lsa,
# .translate() metodiga matnga qo'shimcha ravishda dest
# parametrini ham uzatamiz va bu parametrga tajima qilinishi
# kerak bo'lagan tilning qisqartmasini beramiz.Masalan,
# rus tiliga tarjima qilish uchun dest=='ru' dev yozamiz.

# Tarjima uchun mavjud tillarni quyidagi manzilda ko'rishingiz mumkin.
# https://stes.google.com/site/opti365/translate_codes


tarjima_ru = tarjimon.translate(matn_uz,dest='uz')
print(tarjima_ru.text)

# Ingliz tilidan boshqa tillarga tarjima ham shunday:
matn_en = "Tashkent is the capital of Uzbekiston"
tarjima_uz = tarjimon.translate(matn_en,dest ='ru')
print(tarjima_uz.text)

# Odatda,Google asl matnning tilini o'zi aniqlaydi.Lekin
# matn tilini ham alohida ko'rsatmoqchi bo'lsangiz,src parametridan
# foydalaning:

# tarjima_uz = tarjimon.translate(matn_en,src='uz',dest='en')
# print(tarjima_uz)
