# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:33:37 2023

@author: user
"""

import random as r
def sontop(x=20):
    print(f"1 dan {x} gacha son o'yladim .Topa olasizmi?")
    tasodifiy_son = r.randint(1, x)
    taxminlar = 0 
    while True:
        taxminlar += 1 
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato,men o'ylagan son bundam kattaroq,Yana urinib ko'ring")
        elif taxmin>tasodifiy_son:
            print("Xato,men o'ylgan son bundam kichikroq, Yana urinib ko'ring")
        else: 
            break
    print(f"Tabriklaymiz.Siz {taxminlar} ta urinishda topdingiz.")
    return taxminlar
def sontop_pc(x=20):
    input(f"1 dan {x} gacha son o'ylang men topaman, va istagan tugmani topish")
    taxminlar = 0
    quyi = 1 
    yuqori = x
    while True:
        taxminlar += 1 
        if quyi != yuqori:
            taxmin = r.randint(quyi,yuqori)
        else: 
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz : tog'ri(t),"
                      f"men o'ylagan son bundan kattaroq(+),yoki kichikroq (-)".lower())
        if javob =="-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break 
    print(f"Men {taxminlar} ta urinish bilan topdim!")
    return taxminlar
        
def play(x=20):
    yana = True
    while yana:
        taxminlar_user = sontop()
        taxminlar_pc = sontop_pc()
        if taxminlar_user>
        