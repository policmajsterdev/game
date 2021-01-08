

def check_exp(exp, stopien_sluzbowy):

    """ Sprawdza poziom doświadczenia """

    if exp >= 299 and stopien_sluzbowy == "POSTERUNKOWY":
        exp = 1
        stopien_sluzbowy = "STARSZY POSTERUNKOWY"

    return exp, stopien_sluzbowy


def check_gr(ang, grupa_zaszeregowania, dodatek_sluzbowy):

    """ Sprawdza poziom zaangażowania """

    if ang >= 299 and grupa_zaszeregowania == "kursant":
        ang = 1
        grupa_zaszeregowania = "referent"
        dodatek_sluzbowy = "150 zł"

    return ang, grupa_zaszeregowania, dodatek_sluzbowy
