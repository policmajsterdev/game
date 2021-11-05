import os
import os.path


filepath = os.path.dirname(__file__)


def checking_files():

    """ Sprawdza czy w folderze znajdują się pliki db """

    list_file = os.listdir(os.path.join(filepath, "data\\save\\"))
    if len(list_file) == 0:
        return 0
    else:
        return 1
