"""
Mavzu:JSON(JavaScript Object Notation)
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Amaliyot
Bo'lim:1-qism

"""
# 1
# Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON
# matnini konsolga chaqiring: data = {"Model" : "Malibu",
# "Rang" : "Qora", "Yil":2020, "Narh":40000}
import json
data = {
        "Model" : "Malibu",
        "Rang" : "Qora", 
        "Yil":2020, 
        "Narh":40000
}

data_json = json.dumps(data,indent=4)

# print(data_json)

# 2
# Ushbu JSON matnni ko'chirib oling,talabaning
# ismi va familiyasini konsolga chiqaring: 
# talaba_json  = """{"ism":"Hasan","familiya":"Husanov","tyil":200}"""
talaba = {"ism":"Hasan",
          "familiya":"Husanov",
          "tyil":2000}

talaba_json = json.dumps(talaba,indent=4)
talaba1 = json.loads(talaba_json)
# print(f"{talaba['ism']} {talaba['familiya']}")

# 3  
with open('data.json','w') as file:
        json.dump(data,file)
with open('talaba.json','w') as file :
    json.dump(talaba,file)
    

# 4 
# Ushbu JSON faylni yuklab oling. Faylda 3 ta 
# talabaning ism va familiyasi saqlangan. 
# Ularning har birini alohida qatordan "Ism Familiya, 
# n-kurs, Fakultet talabasi" ko'rinishida konsolga 
# chiqaring.
with open('students.json') as file:
    data = json.load(file)
for item in data['student']:
    print(f"{item['name']} {item['lastname']}."
          f"Faculty of {item['faculty']},")
# 5

# Quyidagi bog'lamaga kirsangiz, Wikipediadagi 
# Python dasturlash tili haqidagi maqolani JSON 
# ko'rinishida ko'rishingiz mumkin. Brauzerda 
# chiqqan ma'lumotni JSON ko'rinishida saqlang 
# (brauzerda Ctrl+S tugmasini bosib). Faylni 
# Pythonda oching va konsolga maqolaning sarlavhasi 
# (title) va qisqa matnini (extract) chiqaring: https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python

with open('wikipedia.json') as file :
    wiki = json.load(file)
print(wiki['query']['pages']['13801']['title'])
print(wiki['query']['pages']['13801']['extract'])

