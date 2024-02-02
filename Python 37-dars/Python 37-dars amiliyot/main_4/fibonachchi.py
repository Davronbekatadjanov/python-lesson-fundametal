# Berilgan son  Fiobanachchi ketma_ketligida uchradimi
# (True) yoki yoq(False) qaytaruvchi funksiya

def fibonachchi_ket_ketligida(son):
    a,  b = 0, 1
    while b < son:
        a, b = b, a + b
    return b == son
# def fibonachchi_ketma_ketligida(son):
#     a, b = 0, 1
#     while b < son:
#         a, b = b, a + b
#     return b == son
