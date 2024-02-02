# random moduli
# # Random moduli tasodifiy sonlar bilan ishlash uchun qulay funksiyalarga boy.Keling ulardan ayrimlar bilan tanishamiz.
# # randint(a,b)
# # Bu funksiya a va b oralig'ida tasodifiy butun son qaytaradi.

import random as r # random modulini r deb chaqirayapmiz

# son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
# print(son)

# # choice()
# # x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya.Bunda  x bir nechta elementdan ibo(at o'zgaruvchi(matn,ro'yxat)bo'lishi kerak

# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism  tanlaymiz
# print(ism)
# print(r.choice(ism))

x = list(range(0,51,5))
print(x)
print(r.choice(x))

# shuffle(x)
# x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya.Bunda x bir necha elementdan iborat o'zgaruvchi (matn,ro'yxat) bo'lishi kerak.

x = list(range(11))
print(x)
r.shuffle(x)
print(x)