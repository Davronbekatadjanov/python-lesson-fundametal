import datetime as dt
hozir = dt.date.today()

qurbon_hayit = dt.date(2024,6,17)

ramazon = dt.date(2024,3,9)
farq_qurbon = qurbon_hayit-hozir

farq_qurbon = farq_qurbon.days
farq_ramazon = ramazon-hozir

farq_ramazon = farq_ramazon.days
print(f"Ramazonga {farq_ramazon} kun qoldi, "
      f"Qurbon hayitiga {farq_qurbon} kun qoldi")



