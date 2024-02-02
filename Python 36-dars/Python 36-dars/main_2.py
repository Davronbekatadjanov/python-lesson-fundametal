"""
Mavzu:JSON(JavaScript Object Notation)
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:2-qism

"""

# Jsondan pythonga 

# JSON formatidan ma'lumotlarni Python ma'lumot turiga 
# keltirish uchun json.loats() yoki json.loat() funksiyalaridan
# foydalanamiz.Yuqoridagi kabi json.loads() funksiyasi
# to'g'ridan to'g'ri JSON matn bilan ishlasa,json.load() 
# funksiyasi JSON fayllarni o'qish uchun ishlatiladi.

# json.loads()

# Bu funksiya parametr sifatida JSON matn qabul qiladi
# va matnni Python ma'lumot turiga o'tkazadi.
import json
sonlar = [12,45,23,67]
sonlar_json = json.dumps(sonlar)
sonlar = json.loads(sonlar_json)



bemor = {
    "ism":"Alijon Valiyev",
    "yosh":30,
    "oila":True,
    "farzandalar":('Ahmad','Bonu'),
    'allaegiya':None,
    "dorilar":[
        {"Nomi":'Analgin',"miqdor":0.5},
        {"Nomi":"Panadol","miqdor":1.2}
    ]
}


bemor_json = json.dumps(bemor)

bemor = json.loads(bemor_json)
print(bemor)


# E'tibor qiling,oilava allergiya kalitlarining
# qiymati qaytadan Python ma'lumot turlariga qaytdi.

# json.load()
# Bu funksiya JSON fayllarnnig tarkibini Pythonga
# yuklab olish uchun ishlatiladi.
filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
print(type(bemor))


