"""
Mavzu:JSON(JavaScript Object Notation)
Sana:22.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
Bo'lim:1-qism

"""
# JSON bilan ishlash

# Ko'pincha internet orqali JSON fayllarni 
# qabul qilganimizda ma'lumotlar bir necha 
# qavatli lug'at ko'rinishida bo'ladi. 
# JSON matnidan aynan o'zimizga kerakli 
# ma'lumotni ajratib olish uchun lug'atni 
# biroz tahlil qilish, uning kalitlari va 
# qiymatlarini topish talab qilinishi mumkin. 
# Bu ayniqsa juda uzun JSON fayllarga tegishli. 
# Shuning uchun JSON bilan samarali ishlash uchun 
# lug'atlar bilan ishlashni yana bir bor takrorlab 
# oling.

# Quyidagi misolda Google Maps hizmati qaytargan 
# JSON matni lug'at ko'rinishida berilgan. 
# Bu Toshkent shahridagi Olmazor tumanining 
# Geografik manzili.



data = {
    "address_components": [
        {
            "long_name": "Almazar District",
            "short_name": "Almazar District",
            "types": [
                "political",
                "sublocality",
                "sublocality_level_1"
            ]
        },
        {
            "long_name": "Tashkent",
            "short_name": "Tashkent",
            "types": [
                "locality",
                "political"
            ]
        },
        {
            "long_name": "Tashkent Region",
            "short_name": "Tashkent Region",
            "types": [
                "administrative_area_level_1",
                "political"
            ]
        },
        {
            "long_name": "Uzbekistan",
            "short_name": "UZ",
            "types": [
                "country",
                "political"
            ]
        }
    ],
    "formatted_address": "Almazar District, Tashkent, Uzbekistan",
    "geometry": {
        "bounds": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        },
        "location": {
            "lat": 41.3645355,
            "lng": 69.2281531
        },
        "location_type": "APPROXIMATE",
        "viewport": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        }
    },
    "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
    "types": [
        "political",
        "sublocality",
        "sublocality_level_1"
    ]
}

# Keling shu ma'lumotlar orasidan tumanning 
# geografik koordinatalrini topamiz. Avvalo, 
# lug'atga ko'z yugurtirib chiqib, bizga kerak 
# ma'lumotlar quyidagi ko'rinishda berilganini 
# ko'rishimiz mumkin:
    
 # "location": {
 #     "lat": 41.3645355,
 #     "lng": 69.2281531

# Bizga aynan latitude (kenglik) va longitude 
# (uzunlik) qiymatlari kerak. Ular esa "location" 
# kaliti ichidagi lug'atda lat va lng kalitlariga 
# tegishli qiymatlarda joylashgan. location 
# kalitining o'zi ham geometry kaliti ichida 
# joylashganini ko'rishimiz mumkin.

# Demak, lug'at ichidan lat va lng qiymatlarini 
# olish uchun quyidagi kodni yozamiz:
    
kenglik = data['geometry']['location']['lat']
uzunlik = data['geometry']['location']['lng']
print(f"{kenglik},{uzunlik}")

# olingan koordinatalarni Google Maps xizmatiga kirtib
# ko'ramiz va quyidagi natijani olamiz.

