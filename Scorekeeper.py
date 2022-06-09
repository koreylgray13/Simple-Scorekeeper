import sys
from tkinter import *

root = Tk()
root.geometry('309x200')
root.title('Scorekeeper')
root.iconbitmap('score.ico')

p1 = LabelFrame(root, padx=20, pady=20, text="Player 1")
p1.grid(row=0, column=0, padx=10, pady=10)

p2 = LabelFrame(root, padx=20, pady=20, text="Player 2")
p2.grid(row=0, column=1, padx=10, pady=10)

p1_buttons = LabelFrame(root, padx=25, pady=20, bg='light gray')
p1_buttons.grid(row=1, column=0, padx=10, pady=10)

p2_buttons = LabelFrame(root, padx=25, pady=20, bg='light gray')
p2_buttons.grid(row=1, column=1, padx=10, pady=10)


def read_score1():
    global p1_score
    read = open('p1.txt', 'r')
    p1_score = read.read()
    return p1_score


def add_score1():
    global new_score1
    read = open('p1.txt', 'r')
    score = read.read()
    new_score1 = int(score) + 1
    new_score1 = str(new_score1)
    read.close()
    def write_score1():
        write = open('p1.txt', 'w')
        write.write(str(new_score1))
        write.close()
    write_score1()

    p1_score = Label(p1, text=read_score1(), font=("Arial Bold", 15))
    p1_score.grid(row=0, column=0)


def sub_score1():
    read = open('p1.txt', 'r')
    score = read.read()
    new_score1 = int(score) - 1
    new_score1 = str(new_score1)
    read.close()

    def write_score():
        write = open('p1.txt', 'w')
        write.write(str(new_score1))
        write.close()
    write_score()

    p1_score = Label(p1, text=read_score1(), font=("Arial Bold", 15))
    p1_score.grid(row=0, column=0)


def read_score2():
    read = open('p2.txt', 'r')
    score = read.read()
    return score


def add_score2():
    read = open('p2.txt', 'r')
    score = read.read()
    new_score2 = int(score) + 1
    new_score2 = str(new_score2)
    read.close()
    def write_score():
        write = open('p2.txt', 'w')
        write.write(str(new_score2))
        write.close()
    write_score()

    p2_score = Label(p2, text=read_score2(), font=("Arial Bold", 15))
    p2_score.grid(row=0, column=0)


def sub_score2():
    global new_score2
    read = open('p2.txt', 'r')
    score = read.read()
    new_score2 = int(score) - 1
    new_score2 = str(new_score2)
    read.close()

    def write_score2():
        write = open('p2.txt', 'w')
        write.write(str(new_score2))
        write.close()
    write_score2()

    p2_score = Label(p2, text=read_score2(), font=("Arial Bold", 15))
    p2_score.grid(row=0, column=0)


p1_inc = Button(p1_buttons, text="+", command=add_score1, bg='green', font=("Arial Bold", 12))
p1_dec = Button(p1_buttons, text="-", command=sub_score1, bg='red3', font=("Arial Bold", 12))
p2_inc = Button(p2_buttons, text="+", command=add_score2, bg='green', font=("Arial Bold", 12))
p2_dec = Button(p2_buttons, text="-", command=sub_score2, bg='red3', font=("Arial Bold", 12))

p1_score = Label(p1, text=read_score1(), font=("Arial Bold", 15))
p1_score.grid(row=0, column=0, padx=5)

p2_score = Label(p2, text=read_score2(), font=("Arial Bold", 15))
p2_score.grid(row=0, column=0, padx=5)


p1_inc.grid(row=1, column=1, padx=5, ipadx=3)
p1_dec.grid(row=1, column=0, padx=5, ipadx=5)

p2_inc.grid(row=1, column=1, padx=5, ipadx=3)
p2_dec.grid(row=1, column=0, padx=5, ipadx=5)


root.mainloop()