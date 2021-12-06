import string
import random
import time
from tkinter import *
from tkinter import messagebox

glowne_okno = Tk()
pasekMenu = Menu(glowne_okno)
glowne_okno.geometry("300x250")


glowne_okno.bind('<space>', lambda x: glowne_okno.destroy())

f= open("wyniki.txt","w+")

while True:
    letter =  random.choice(string.ascii_letters)
    random_letter = Label(glowne_okno, text = letter, font = 'arial 30')
    random_letter.place(relx=.5, rely=.5,anchor= CENTER)
    with open("moje_dane.txt", "a") as myfile:
        myfile.write("start\n")
    end = time.perf_counter()
    rezultat = [letter, end]
    f.write(str(rezultat)+'\n')
    time.sleep(1)

    glowne_okno.update()

glowne_okno.mainloop()
