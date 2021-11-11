import os
import os.path


filepath = os.path.dirname(__file__)


def checking_save():

    """ Sprawdza czy w folderze znajduje się plik save """

    list_file = os.listdir(os.path.join(filepath, "data\\glsav\\"))
    if len(list_file) == 0:
        return 0
    else:
        return 1


def checking_presave():

    """ Sprawdza czy w folderze znajduje się plik pre_save """

    list_file = os.listdir(os.path.join(filepath, "data\\save\\"))
    if len(list_file) == 0:
        return 0
    else:
        return 1
