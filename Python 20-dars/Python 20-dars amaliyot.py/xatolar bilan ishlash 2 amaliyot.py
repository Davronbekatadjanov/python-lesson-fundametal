"""
Mavzu:Xatolar bilan ishlash 2 amaliyot
Sana:03.02.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
# Quyidagi kod bajarilishida yuzaga kelishi mumkin bo'lgan xatolarni ushlab ,
# xatoga mos matnni konsolga chiqaring:

while True:
    x = int(input("son kiriting: "))
    y = int(input("yana bir son kiriting: "))
    z = x/y
    if z.isdigit():
        break
print(x, '/',y, '=',z)
    
    