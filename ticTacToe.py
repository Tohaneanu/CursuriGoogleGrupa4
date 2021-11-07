import random

import numpy as np

table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def to_string(game):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(game[i][j], end="|")
        print()


def my_move(x, y):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == x:
                table[i][j] = y


def pc_move():
    if str(table[1][1]).isnumeric():
        table[1][1] = "O"
        return
    if table[0][0] == "O" and str(table[2][2]).isnumeric() and table[1][1] == "O":
        table[2][2] = "O"
    elif table[2][2] == "O" and str(table[0][0]).isnumeric() and table[1][1] == "O":
        table[0][0] = "O"
    elif table[0][2] == "O" and str(table[2][0]).isnumeric() and table[1][1] == "O":
        table[2][0] = "O"
    elif table[2][0] == "O" and str(table[0][2]).isnumeric() and table[1][1] == "O":
        table[0][2] = "O"
    list = [[0, 0], [2, 2], [0, 2], [2, 0]]
    for item in list:
        if str(table[item[0]][item[1]]).isnumeric():
            continue
        else:
            list.remove(item)
    if pc_random_move(list) == 1:
        return
    list = [[0, 1], [1, 0], [1, 2], [2, 1]]
    for item in list:
        if str(table[item[0]][item[1]]).isnumeric():
            continue
        else:
            list.remove(item)
    if pc_random_move(list) == 1:
        return


def pc_random_move(list):
    a = random.choice(list)

    if set_random_poz(list, a) == 1:
        return 1
    return


def set_random_poz(elem, a):
    if str(table[a[0]][a[1]]).isnumeric():
        table[a[0]][a[1]] = "O"
        elem.remove(a)
        return 1


def win():
    for item in table:
        if item[0] == item[1] == item[2]:
            if item[0] == "x":
                return 1
            else:
                return 0
    for item in np.transpose(table):
        if item[0] == item[1] == item[2]:
            if item[0] == "x":
                return 1
            else:
                return 0
    if table[0][0] == table[1][1] == table[2][2]:
        if table[0][0] == "x":
            return 1
        else:
            return 0
    if table[0][2] == table[1][1] == table[2][0]:
        if table[0][0] == "x":
            return 1
        else:
            return 0
    return

def game():
    while True:
        to_string(table)
        val = int(input(f"ALEGE UN NUMAR DIN CELE AFISATE :"))
        my_move(val, "x")
        pc_move()
        a=win()
        if a == 1:
            print("AI CASTIGAT!")
            break
        elif a==0:
            print("AI PIERDUT!")
            break


game()
