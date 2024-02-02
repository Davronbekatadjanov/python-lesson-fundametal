# fuzzywuzzy

# pip install fuzzywuzzy

# Bu modul yordamida so'zlarni bir-biriga 
# solishtirish yoki matnlar tarkibida kerakli 
# so'zni topishda foydalanamiz.

# Quyidagi misolda "salom" so'zini "assalom" va 
# "salim" so'zlari bilan naqadar o'xshashligini 
# tekshrib ko'ramiz:

from fuzzywuzzy import fuzz
print(fuzz.ratio("salom",'assalom'))

print(fuzz.ratio('salom','salim'))

# Keling endi so'zlar orasidan o'xshash
# so'zlarni topishni ko'ramiz.
# Buning uchun avvaligi dasrlarimidagi
# uzwords modulidan foydalanamiz.Ro'yxatdan
# bir nechta so'zlarni ajratib olish
# uchun .process.extract() funksiyasiga murojat qilamiz.

from fuzzywuzzy import process
from uzwords import words

# Matnlar orasidan 3 ta eng o'xshlashlarini ajratib olish
text = "салом"
matches = process.extract(text,words,limit=3)
print(matches)

# Agar yagona so'zni 
# tanlab olish talab qilinsa extractOne() metodini chaqiramiz.

text = "талба"
match = process.extractOne(text,words)
print(match)

