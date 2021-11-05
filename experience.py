import db_save


def check_exp():

    """ Sprawdza poziom doświadczenia """

    stan_konta = db_save.pobierz_dane("dane_konta")
    dane_gracza = db_save.pobierz_dane("dane_gracza")
    exp = stan_konta[0][0]
    stopien_sluzb = dane_gracza[0][1]
    dodatek_sluzbowy = stan_konta[0][2]
    kwota_bazowa = stan_konta[0][3]
    mnoznik_grupa = stan_konta[0][4]
    dodatek_stopien = stan_konta[0][5]
    wysluga_lat = stan_konta[0][6]
    dni_sluzby = stan_konta[0][7]
    grupa_zaszeregowania = dane_gracza[0][2]
    if exp >= 299 and stopien_sluzb == "posterunkowy":
        db_save.aktualizuj_dane_gracza("dane_konta", "exp", 1)
        db_save.aktualizuj_dane_gracza("dane_gracza", "stopien_sluzbowy", "starszy posterunkowy")
        db_save.aktualizuj_dane_gracza("dane_konta", "dodatek_stopien", 300)
    ang = stan_konta[0][1]
    if ang >= 299 and grupa_zaszeregowania == "kursant":
        db_save.aktualizuj_dane_gracza("dane_konta", "ang", 1)
        db_save.aktualizuj_dane_gracza("dane_gracza", "grupa_zaszeregowania", "aplikant")
        db_save.aktualizuj_dane_gracza("dane_konta", "dodatek_sluzbowy", 50)
    wyplata_netto = uposazenie_netto(kwota_bazowa, mnoznik_grupa, dodatek_sluzbowy, dodatek_stopien, wysluga_lat)
    if dni_sluzby >= 31:
        db_save.aktualizuj_dane_gracza("dane_konta", "dni_sluzby", 1)
        db_save.update_exp_ang_dni("stan_konta", "dane_konta", wyplata_netto)


def uposazenie_netto(kwota_bazowa, mnoznik_grupa, dodatek_sluzbowy, dodatek_stopien, wysluga_lat):

    """ Liczy uposażenie """

    wysluga_procenty = wysluga_lat / 100
    kwota_mnoznik = (kwota_bazowa * mnoznik_grupa) + dodatek_sluzbowy + dodatek_stopien
    wysluga_netto = kwota_mnoznik * wysluga_procenty
    wyplata_netto = kwota_mnoznik + wysluga_netto
    wyplata_netto = round(wyplata_netto, 2)

    return wyplata_netto


def aktualny_stan_konta():

    """" Tworzy dane do wyświetlenia """
    check_exp()
    stan_konta = db_save.pobierz_dane("dane_konta")
    exp = stan_konta[0][0]
    ang = stan_konta[0][1]
    dodatek_sluzbowy = stan_konta[0][2]
    kwota_bazowa = stan_konta[0][3]
    mnoznik_grupa = stan_konta[0][4]
    dodatek_stopien = stan_konta[0][5]
    wysluga_lat = stan_konta[0][6]
    wysluga_procent = str(wysluga_lat) + "%"
    dni_sluzby = stan_konta[0][7]
    kiedy_wyplata = 31 - dni_sluzby
    stan_konta_fsza = stan_konta[0][8]
    wyplata_netto = uposazenie_netto(kwota_bazowa, mnoznik_grupa, dodatek_sluzbowy, dodatek_stopien, wysluga_lat)

    return exp, ang, dodatek_sluzbowy, kwota_bazowa, mnoznik_grupa, dodatek_stopien, wysluga_procent, stan_konta_fsza, wyplata_netto, kiedy_wyplata
