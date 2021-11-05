import sqlite3
import os.path

filepath = os.path.dirname(__file__)


def create_db_account():

    """ Tworzy plik małej bazy danych dla txt """

    connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
    curs = connector.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS dane_gracza (imie_gracza TEXT, stopien_sluzbowy TEXT, grupa_zaszeregowania)''')
    curs.execute('''INSERT INTO dane_gracza VALUES (1, 1, 0)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS dane_baretki (baretki TEXT)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS dane_notatki (notatki TEXT)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS dane_quest_tomek (quest_tomek TEXT)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS dane_indeks (ocena INT)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS dane_strzelnica (punkty INT)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS dane_ekwipunek (ekwipunek TEXT)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS dane_save (scena TEXT)''')
    curs.execute(
        '''CREATE TABLE IF NOT EXISTS dane_konta (exp INT, ang INT, dodatek_sluzbowy INT, kwota_bazowa REAL, mnoznik_grupa REAL, dodatek_stopien INT, wysluga_lat INT, dni_sluzby INT, stan_konta REAL)''')
    curs.execute('''INSERT INTO dane_konta VALUES (1, 1, 0, 1614.69, 1.36, 280, 1, 1, 2500.74)''')
    connector.commit()
    connector.close()


def add_1_value(tabela, wartosc):

    """ Dodaje wartość do wybranej tabeli """

    zapytanie = "INSERT INTO " + tabela + " VALUES (?)"
    connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
    curs = connector.cursor()
    curs.execute(zapytanie, (wartosc,))
    connector.commit()
    connector.close()


def delete_1_value(tabela, wartosc):

    """ Kasuje wartość w wybranej tabeli """

    zapytanie = "DELETE from " + tabela + " where ekwipunek = " + wartosc
    connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
    curs = connector.cursor()
    curs.execute(zapytanie)
    connector.commit()
    connector.close()


def add_2_value(tabela, value_1, value_2):

    """ Dodaje wartość do małej bazy danych"""

    zapytanie = "INSERT INTO " + tabela + " VALUES (?, ?)"
    connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
    curs = connector.cursor()
    curs.execute(zapytanie, (value_1, value_2))
    connector.commit()
    connector.close()


def update_exp_ang_dni(kolumna, tabela, wartosc):

    """ Aktualizuje wpis ang w db konto """

    poprzedni = 0
    zapytanie_1 = "SELECT " + kolumna + " FROM " + tabela
    zapytanie_2 = "UPDATE " + tabela + " SET " + kolumna + " = ?"
    connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
    curs = connector.cursor()
    for row in curs.execute(zapytanie_1):
        poprzedni = row[0]
    nowy = poprzedni + wartosc
    curs.execute(zapytanie_2, (nowy,))
    connector.commit()
    connector.close()


def aktualizuj_dane_gracza(tabela, kolumna, wartosc):

    """ Aktualizuje wpis d_sluzbowy w db konto """

    zapytanie = "UPDATE " + tabela + " SET " + kolumna + " = ?"
    connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
    curs = connector.cursor()
    curs.execute(zapytanie, (wartosc,))
    connector.commit()
    connector.close()


def search_dane_gracza(value):

    """ Wybiera szukaną wartość """

    hit = None

    connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
    curs = connector.cursor()
    curs.execute("SELECT id, nazwa FROM dane_gracza")
    for i in curs:
        if i[0] == value:
            hit = i[1]
    connector.close()
    return hit


def search_dane_save():

    """ Wybiera szukaną wartość """

    hit = None
    try:
        connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
        curs = connector.cursor()
        for i in curs.execute("SELECT * FROM dane_save"):
            hit = i[0]
        connector.close()
    except:
        pass
    return hit


def search_data(kolumna, tabela):

    """ Pobiera ekwipunek """

    zapytanie = "SELECT " + kolumna + " FROM " + tabela
    eq_x = []
    eq = []
    try:
        connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
        curs = connector.cursor()
        curs.execute(zapytanie)
        for i in curs:
            i = i[0]
            eq_x.append(i)
        connector.close()
        for e in eq_x:
            eq.append(e)
    except:
        pass
    return eq


def pobierz_dane(tabela):

    """ Pobiera stan konta gracza """

    stan_konta = []
    zapytanie = "SELECT * FROM " + tabela
    connector = sqlite3.connect(os.path.join(filepath, "data\\save\\db_account.db"))
    curs = connector.execute(zapytanie)
    for i in curs:
        stan_konta.append(i)
    connector.close()
    return stan_konta
