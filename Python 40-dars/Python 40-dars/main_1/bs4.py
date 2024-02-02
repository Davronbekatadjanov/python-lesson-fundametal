
# BeautgulSoup4
# O'rnatilishi: pip install beutifulsoup4

# BeautfulSoup juda kuchli modullardan biri bo'lib
# bu modul yordamida turli veb-sahifalardan istalgan ma'lumotlarni
# yig'ishtirib(scrapping) olish mumkin.Biror kishining Instagram sahifasidagi
# (scrapping) olish mumkin.Biror kishining Instagram sahifasidagi
# barcha rasmalr deysizmi,Facebook guruhidagi barcha postlar va
# izohlar deysizmi,oldi-sotdi bozoridagi e'lonlar deysizmi,marhamat,bs4
# moduli yordamida buni bemalol avtomatlashtirish mumkin

import requests

from bs4 import BeautifulSoup
sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
soup = BeautifulSoup(r.text,'html.parser')
# yangiliklarning mavzusini ajratib olish uchun quyidagi kodni 
# yozamiz 
news = soup.find_all(class_="news-title")
# eng birinchi yangilikni konsolga chiqaramiz
print(news[6].text)



# Odatda,bs4 moduli request moduli bilan hamkorlikda ishlaydi.Keling
# sodda misol keltiramiz.Avvalgi bo'limda requests yordamida kun.uz
# sahifani tortib olgan edik.Endi esa bs4 yordamida sahifadan oxirgi
# yangiliklarning mavzusini ajratib olamiz.

# wordcloud va matplotlib
# O'rnatilishi:
    # pip install wordcloud
    # pip install matplotlib
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text,'html.parser')
news = soup.find_all(class_="news-title")
matn=""
for n in news:
    matn += n.text
    
# keraksiz so'zlar

stopwords = ["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]
  
# bulutni yaratamiz
wordcloud = WordCloud(width = 1000,height = 1000,
                      background_color = 'white',
                      stopwords = stopwords,
                      min_font_size = 20).generate(matn)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()




# wordcloud moduli yordamida katta matnlarda
# eng ko'p uchraydigan so'zlardan so'zlar bulutli chiqarish
# mumkin. wordcloud moduli grafiklarni chizishga mo'ljallangan
# matplotlib moduli bilan hamkorlikda ishlaydi.

# Quyidagi kun.uz sahifasidan  olingan yangiliklar uchun
# so'zlar bulutini yaratishni ko'zdan kechiramiz.


