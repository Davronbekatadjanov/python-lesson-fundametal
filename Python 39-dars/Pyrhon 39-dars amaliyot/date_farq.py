import datetime as dt 

bugun = dt.date.today()
 
avval = bugun - dt.timedelta(days=14)
for n in range(1,11):
    sana = avval + dt.timedelta(days=n)
    sana_format = sana.strftime("%d/%m/%Y")
    print(sana_format)

# farq so'zini qanday qilib tushunishni bilmadi 
# shuning uchun ikkita misol yozdim
for n in range(1,11):
    sana = bugun + dt.timedelta(weeks=n)
    sana_format1 = sana.strftime("%d/%m/%Y")
    print(sana_format1)
    