import os
import os.path


filepath = os.path.dirname(__file__)


def checking_files():

    """ Check save folder """

    list_file = os.listdir(os.path.join(filepath, "data\\save\\"))
    if len(list_file) != 0:
        return 1
    else:
        return 0


def type_save():

    """ IOTA, BSV, PC """

    iota_save = []
    bsv_save = []
    pc_save = []
    wtf = []

    list_file = os.listdir(os.path.join(filepath, "data\\save\\"))
    for i in list_file:
        if i == "pc_save.txt":
            pc_save.append(i)
        elif i == "iota_save.txt":
            iota_save.append(i)
        elif i == "bsv_save.txt":
            bsv_save.append(i)
        else:
            wtf.append(i)

    return iota_save, bsv_save, pc_save


def delisting_save(list_save):

    """ Delisting save list """

    imieGracza = ""
    legitymowanie = ""
    ruchdrogowy = ""
    pendrive1 = ""
    skrawek1 = ""
    ocenaSTR = ""
    ocena_ruchSTR = ""
    quest_tomek_1 = ""
    wynikp99 = ""

    lis_save = list_save.split("/")

    for i in lis_save:
        if i[:7] == "PLAYER:":
            imieGracza = i[7:]
        if i[:7] == "LEGITY:":
            legitymowanie = i[7:]
        if i[:7] == "RUCHDR:":
            ruchdrogowy = i[7:]
        if i[:7] == "PENDRI:":
            pendrive1 = i[7:]
        if i[:7] == "SKRAWE:":
            skrawek1 = i[7:]
        if i[:7] == "OCENAL:":
            ocenaSTR = i[7:]
        if i[:7] == "OCENAR:":
            ocena_ruchSTR = i[7:]
        if i[:7] == "QUESTT:":
            quest_tomek_1 = i[7:]
        if i[:7] == "WYNIKP:":
            wynikp99 = i[7:]

    return imieGracza, legitymowanie, ruchdrogowy, pendrive1, skrawek1, ocenaSTR, ocena_ruchSTR, quest_tomek_1, wynikp99
