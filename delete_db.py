import os.path
import db_save


filepath = os.path.dirname(__file__)


def delete_db_0_save():

    """ Kasuje plik db gdy gracz wychodzi przed 1 zapisem gry """
    try:
        lista_plikow = list(os.listdir(filepath + "\\data\\save"))
        if lista_plikow[0] == "db_account.db":
            hit = db_save.search_data("scena", "dane_save")
            if not hit:
                nowa_sciezka = filepath + "\\data\\save\\" + lista_plikow[0]
                os.remove(nowa_sciezka)
        else:
            pass
    except:
        pass


def delete_db_continue():

    """ Kasuje plik db gdy gracz posiada zapis a wybierze nową grę """

    lista_plikow = list(os.listdir(filepath + "\\data\\save"))
    if lista_plikow[0] == "db_account.db":
        nowa_sciezka = filepath + "\\data\\save\\" + lista_plikow[0]
        os.remove(nowa_sciezka)
    else:
        pass
