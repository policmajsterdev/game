import shutil
import os.path
import check_file_save

filepath = os.path.dirname(__file__)


def copy_save():

    """ Tworzy/kopiuje plik save """

    file = check_file_save.checking_presave()
    if file == 1:
        pre_save = filepath + "\\data\\save\\db_account.db"
        save = filepath + "\\data\\glsav\\db_account.db"
        shutil.copy2(pre_save, save)
    else:
        pass
