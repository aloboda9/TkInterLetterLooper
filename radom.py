import string
import random
import time
from tkinter import *
from tkinter import messagebox

glowne_okno = Tk()
pasekMenu = Menu(glowne_okno)
glowne_okno.geometry("300x250")

for i in range(10):
    random_letter = Label(glowne_okno, text = random.choice(string.ascii_letters), font = 'arial 30')
    random_letter.place(relx=.5, rely=.5,anchor= CENTER)
    time.sleep(2)
    glowne_okno.update()

glowne_okno.mainloop()
