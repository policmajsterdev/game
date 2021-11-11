import os.path


filepath = os.path.dirname(__file__)


def delete_db_0_save():

    """ Kasuje pre_save db gdy gracz wychodzi przed zapisem """

    try:
        lista_plikow = list(os.listdir(filepath + "\\data\\save"))
        if lista_plikow[0] == "db_account.db":
            nowa_sciezka = filepath + "\\data\\save\\" + lista_plikow[0]
            os.remove(nowa_sciezka)
        else:
            pass
    except:
        pass


def delete_db_continue():

    """ Kasuje save gdy gracz posiada zapis a wybierze nową grę """

    try:
        lista_plikow = list(os.listdir(filepath + "\\data\\glsav"))
        if lista_plikow[0] == "db_account.db":
            nowa_sciezka = filepath + "\\data\\glsav\\" + lista_plikow[0]
            os.remove(nowa_sciezka)
        else:
            pass
    except:
        pass
