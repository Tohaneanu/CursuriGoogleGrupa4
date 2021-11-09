import random

import numpy as np

import tkinter
from tkinter import *
from tkinter import messagebox

table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def to_string(game):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(game[i][j], end="|")
        print()


def my_move(x, y="X"):
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
            if item[0] == "X":
                return 1
            else:
                return 0
    for item in np.transpose(table):
        if item[0] == item[1] == item[2]:
            if item[0] == "X":
                return 1
            else:
                return 0
    if table[0][0] == table[1][1] == table[2][2]:
        if table[0][0] == "X":
            return 1
        else:
            return 0
    if table[0][2] == table[1][1] == table[2][0]:
        if table[0][2] == "X":
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
        a = win()
        if a == 1:
            print("AI CASTIGAT!")
            break
        elif a == 0:
            print("AI PIERDUT!")
            break


# game()

root = tkinter.Tk()
# root.geometry('500x600+300+300')
root.resizable(0, 0)
root.title("Tic Tac Toe")
b = []
pc_m = set()
index = set()
count = 0


def logica_grafic(a1, a2):
    global count
    count += 1
    my_move(a1)
    b[a2]["text"] = "X"
    b[a2].config(state=DISABLED)
    if count >= 3:
        a = win()
        print(a)
        if a == 1:
            messagebox.showinfo("TicTacToe", "AI CASTIGAT!!")
            disable_all_buttons()
            return
    pc_move()
    print(table)
    global index
    global pc_m
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 'O':
                if i == 0 and j == 0:
                    index.add(0)
                    break
                elif i == 0 and j == 1:
                    index.add(1)
                    break
                elif i == 0 and j == 2:
                    index.add(2)
                    break
                if i == 1 and j == 0:
                    index.add(3)
                    break
                elif i == 1 and j == 1:
                    index.add(4)
                    break
                elif i == 1 and j == 2:
                    index.add(5)
                    break
                if i == 2 and j == 0:
                    index.add(6)
                    break
                elif i == 2 and j == 1:
                    index.add(7)
                    break
                elif i == 2 and j == 2:
                    index.add(8)
                    break
    print(index)
    for i in index:
        if i in pc_m:
            continue
        else:
            pc_m.add(i)
            print(pc_m)
            b[i]["text"] = "O"
            b[i].config(state=DISABLED)

    if count >= 3:
        a = win()
        print(a)
        if a == 0:
            messagebox.showinfo("TicTacToe", "AI PIERDUT!!!")
            disable_all_buttons()
            return


def b_click0():
    logica_grafic(1, 0)


def b_click1():
    logica_grafic(2, 1)


def b_click2():
    logica_grafic(3, 2)


def b_click3():
    logica_grafic(4, 3)


def b_click4():
    logica_grafic(5, 4)


def b_click5():
    logica_grafic(6, 5)


def b_click6():
    logica_grafic(7, 6)


def b_click7():
    logica_grafic(8, 7)


def b_click8():
    logica_grafic(9, 8)


def disable_all_buttons():
    for i in range(9):
        b[i].config(state=DISABLED)


b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click0))
b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click1))
b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click2))
b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click3))
b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click4))
b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click5))
b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click6))
b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click7))
b.append(Button(root, text=" ", font=("Helvetica", 20), height=4, width=8, bg="SystemButtonFace",
                command=b_click8))

b[0].grid(row=0, column=0)
b[1].grid(row=0, column=1)
b[2].grid(row=0, column=2)

b[3].grid(row=1, column=0)
b[4].grid(row=1, column=1)
b[5].grid(row=1, column=2)

b[6].grid(row=2, column=0)
b[7].grid(row=2, column=1)
b[8].grid(row=2, column=2)

root.mainloop()
