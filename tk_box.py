import os
from tkinter import *


filepath = os.path.dirname(__file__)
icon_eq = os.path.join(filepath, "data\\pics\\pleczak.ico")


def informacja(tresc, zrodlo_pliku, wymiary):

    eq = "☆ Otrzymujesz " + tresc + " ☆"
    tytul_okna = "Ekwipunek/Statystyki"
    root = Tk()
    root.iconbitmap(icon_eq)
    root.geometry(wymiary)
    root.title(tytul_okna)
    text3_lbl = Label(root, text=eq)
    text3_lbl.pack()
    przedmiot = PhotoImage(file=zrodlo_pliku)
    graph_lbl = Label(root, image=przedmiot)
    graph_lbl.pack()
    root.mainloop()
