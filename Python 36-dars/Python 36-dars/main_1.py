"""
Mavzu:JSON(JavaScript Object Notation)
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:1-qism

"""

# JSON (JavaScript Object Notation) 
# bugungi kunda ma'lumotlarni saqlash va internet 
# orqali uzatish uchun qo'llaniladigan eng mashxur 
# format hisoblanadi. Dastavval JavaScript tili uchun 
# yaratilgan bu format, bugungi kunda deyarli barcha 
# dasturlash tillari tomonidan ishlatiladi. Qolaversa, 
# JSON formatidagi fayllarining tarkibini oddiy matn 
# muharriri yordamida koʻrish va tahrirlash mumkin.

# Yuqoridagi misolda maʻlumotlar Pythondagi 
# lug'atlar kabi kalit soʻz va qiymat koʻrinishida 
# saqlangan. Lekin, JSON yordamida biz nafaqat lug'at, 
# balki boshqa turdagi ma'lumotlarni ham saqlashimiz 
# mumkin. Bunda Pythondagi ma'lumot turlari, quyidagi 
# jadval asosida, JavaScript ma'lumot turlariga 
# konvertasiya qilinadi:
    
# Demak,dasturimiz davomida ma'lmotlarni JSON ko'rnishida
# saqlashimiz,internet orqali boshqa foydlanuvchilar
# ga,dasturlarg yoki serverga yuborishimiz,JSON fayllarni 
# Pythonda ochib,unga ishlov berishimiz va turli amallar
# bajarishimiz mumkin.


# JSON ko'rinishidagi o'zgaruvchilar,tarkibidan qati'narzar
# matn ko'rinishida saqlnadi.

# Pythondan JSONGA

# JSON ma'lumotlar turi va fayllar bilan ishlash
# uchun Pythonda maxsus json moduli bor.Dasturimiz boshida
# bir bu modulini yuklab olishimiz kerak:import json
# Ma'lumotlarni JSON ko'rinishidagi matnga o'tkazish
# uchun ikki fuksiyaning foydalanamiz:
    # json.dumps(x) - berilgan x o'zgaruvchini JSON matniga
    # o'zgatirish
    # json.demp(x,fayl)-berilgan x o'zgaruvchini JSON
    # ko'rinishiga o'zgartirish,ko'rsatilgan faylga yozadi.
    
# json_dumps()

# Ma'lumotlarni JSON formatiga o'tkazish uchun json.dumps()
# funksiyasidan foydalanamiz:

import json

x = 10
x_json = json.dumps(x)
 
ism = 'Anvar'
ism_json = json.dumps(ism)
sonlar = [12,45,23,67]
sonlar_json = json.dumps(sonlar)

# JSON ma'lumotlar matn ko'rinishida saqlanadi.

# print(type(sonlar_json))
# Yuqoridagi ayganimizdek,ko'p holatlarda JSON 
# ma'lumotlar lug'at ko'rinishida uztiladi.

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

# print() funksiyasi yordamida JSON tarkibida ko'rishimiz
# mumkin:

# print(bemor_json)    

# Yuqoridagi natija o'qish uchu noqulay ko'rinishida chiqdi.
# Buni to'g'rilash uchun dumps() funksiyasiga 
# qo'shimcha indent=4 parametrini beramiz. 
# Bu parametr ma'umotlarni saqlashda chapdan 
# qancha joy tashlashni ko'rsatadi:
    
bemor_json = json.dumps(bemor,indent=4)
print(bemor_json)

# Natija o'qishga qulay ko'rinishda chiqdi

# Mavzu boshida, JSON ichidagi ma'lumotlar 
# JavaScript ma'lumot turlariga konvertasiya 
# qilinadi dedik. Buni yuqoridagi misolda ham
# ko'rishimiz mumkin (farzandlar, oila, allergiya 
# kalitlari qiymatini asl lug'at bilan solishtiring).

# json.dumps()

# Ma'lumotarni JSON formatiga o'tkazish va faylga yozish
# uchun json.dumps() funksiyasini chaqiramiz.Fuksiya
# parametr sifatida o'zgaruvchi va fayl nomlarini 
# ko'rsatamiz.Albatta,buning uchun avval faylni 
# yozish uchun ochgan bo'lishimiz kerak.


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

with open('bemor.json','w') as f:
    json.dump(bemor,f)
