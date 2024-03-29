import os
from tkinter import *
import db_save


filepath = os.path.dirname(__file__)
icon_eq = os.path.join(filepath, "data\\pics\\pleczak.ico")
tlos = os.path.join(filepath, "data\\pics\\hg.png")
tloe = os.path.join(filepath, "data\\pics\\hp.png")


def informacja(tresc, zrodlo_pliku):

    eq = "☆ Otrzymujesz " + tresc + " ☆"
    tytul_okna = "Ekwipunek/Statystyki"
    root = Tk()
    root.iconbitmap(icon_eq)
    root.geometry("350x150")
    root.title(tytul_okna)
    tlo = PhotoImage(file=tloe)
    label_image = Label(root, image=tlo)
    label_image.place(x=0, y=0, relwidth=1, relheight=1)
    text3_lbl = Label(root, text=eq, foreground="#FFFFFF", bg="#000000")
    text3_lbl.pack()
    przedmiot = PhotoImage(file=zrodlo_pliku)
    graph_lbl = Label(root, image=przedmiot, relief="flat", bd=0)
    graph_lbl.pack()
    root.mainloop()


def zapiski(osoba, tabela):

    """ Pobiera informacje o osobie """

    tytul_okna = "Zapiski na temat " + osoba
    dane = db_save.pobierz_dane(tabela)
    root = Tk()
    root.iconbitmap(icon_eq)
    root.geometry("400x400")
    root.title(tytul_okna)
    tlo = PhotoImage(file=tlos)
    label_image = Label(root, image=tlo)
    label_image.place(x=0, y=0, relwidth=1, relheight=1)
    label_head = Label(root, width=0, foreground="#000000", bg="#000000")
    label_head.pack()

    for x in dane:
        tex = x[0] + " : " + x[1]
        label = Label(root, text=tex, foreground="#FFFFFF", bg="#000000")  # set your text
        label.pack()
    root.mainloop()