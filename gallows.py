# cuvant="a__a__t"
# alfabet
import random
from random_word import list_of_random_word
word = random.choice(list_of_random_word)
word_list = []
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())

# print(word_list)
print(" ".join(word_list))

count_nr = 1
already_list_checked = []
while count_nr <= 7:
    user_letter = input("Alege o litera: ").lower()
    count_nr += 1
    if user_letter == "":
        print("Introdu o litera")
        continue
    if user_letter in word_list:
        print("litera deja afisata pe ecran")
    elif user_letter in already_list_checked:
        print(f"Litera deja incercata, literele deja incercate: {' '.join(already_list_checked)}")
    else:
        if user_letter in word:
            print("Litera exista in cuvant")
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = user_letter
            print(" ".join(word_list))
        else:
            print(f"mai ai doar {7 - count_nr} incercari")
            count_nr += 1
        if '_' not in "".join(word_list):
            print("CASTIGAT")
            break
        elif count_nr > 7:
            print(f"Ai pierdut, cuvantul era {word}")
        already_list_checked.append(user_letter)
