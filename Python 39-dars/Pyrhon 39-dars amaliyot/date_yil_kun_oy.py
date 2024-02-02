import datetime as dt
hozir = dt.date.today()
tyil = dt.date(2005,12,14)

farq = hozir-tyil 

kunlar = farq.days
oylar = int(kunlar/30)
yillar = int(oylar/12)

print(f"Tug'ilgan kunimdan {yillar} yil, {oylar} oy {kunlar} kun o'tdi ")
