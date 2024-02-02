import re

andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

msg = "Yangi raqam kiriting "
msg += "(+ belgilarisiz telefon raqam kiriting,kamida:12 ta raqamdan iborat bo'lsin "
msg += "va 998 bilan boshlansin:>>>"
while True:
    phone_number = input(msg)
    if re.match(andoza,phone_number):
        print("Telefon raqam qabul qilindi")
        break
    else:
        print("Telefon raqam noto'g'ri kiritilgan,qayta kiriting!")
