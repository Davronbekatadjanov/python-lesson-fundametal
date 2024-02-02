# # Berilgan sonlar ro'yxatidan juft sonlarni 

def juftSonmi(son):
    sonlar = []
    for n in son:
        if n%2 == 0:
            sonlar.append(n)
    return sonlar
        
# def juft_sonlarni_ajratish(sonlar):
#     juft_sonlar = []
#     for son in sonlar:
#         if son % 2 == 0:
#             juft_sonlar.append(son)
#     return juft_sonlar



# raqamlar = [1,2,3,4,5,6,8]
# juft_sonlar = juft_sonlarni_ajratish(raqamlar)
# print(juft_sonlar)


# sonlar = juftSonmi(raqamlar)
# print(sonlar)
