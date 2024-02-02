"""
Mavzu: "So'z topish" O'YINI
Sana:08.03.2023
Muallif:Atadjanov Davronbek
telegram:@atadjanovd
"""
import random 
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()
  
def display(user_letters,word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ""
    print(f"Men {len(word)} xonali so'z o'yladim.Topa olsizmi?")
    #print(word)
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters):
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz,Boshqa harf kiriting.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfni to'g'ri.")
        else: 
            print("Bunday harf yo'q.")
        user_letters += letter
    print(f"Tabriklarman! {word} so'zini {len(user_letters)} ta urinishda topdingiz")