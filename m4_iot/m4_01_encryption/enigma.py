"""
MODUL               Modul 4 - Python u području Internet stvari (IoT)
TEMA                Vjezba pisanja koda na Raspberry Pi OS
NASLOV              Izrada simulatora uredaja Enigma
"""


# --------------------- Enigma Settings --------------------------------
rotori = ("I", "II", "III")
reflektor = "B"
# Definira koliki je offset kod enkodiranja na rotoru
rotori_pomak = "CBS"
rotori_pocetne_pozicije = "NBA"
ploca_s_utikacima_postavke = "AT BS DE FM IR KN LZ OW PV XY"
# ----------------------------------------------------------------------


# Funkcija koja dobiveni tekst izmijeni tako da svako slovo u tekstu zamjeni s drugim
# slovom abecede, ovisno o definiranom pomaku
def ceaser_crypt(tekst, pomak):
    rezultat = ""

    for i in range(len(tekst)):
        slovo = tekst[i]
        ascii_code = ord(slovo)
        if (ascii_code >= 65) and (ascii_code <= 90):
            slovo = chr(((ascii_code - 65 + pomak) % 26) + 65)
        rezultat += slovo
    return rezultat


def enigma(poruka):
    global rotori, reflektor, rotori_pomak, rotori_pocetne_pozicije, ploca_s_utikacima_postavke

    kriptirana_poruka = ""
    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    rotor_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor_I_zarez = "Q"
    rotor_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor_II_zarez = "E"
    rotor_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotor_III_zarez = "V"
    rotor_IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    rotor_IV_zarez = "J"
    rotor_V = "VZBRGITYUPSDNHLXAWMJQOFECK"
    rotor_V_zarez = "Z"

    rotor_dict = {
        "I": rotor_I,
        "II": rotor_II,
        "III": rotor_III,
        "IV": rotor_IV,
        "V": rotor_V,
    }
    rotor_zarezi_dict = {
        "I": rotor_I_zarez,
        "II": rotor_II_zarez,
        "III": rotor_III_zarez,
        "IV": rotor_IV_zarez,
        "V": rotor_V_zarez,
    }

    reflektor_tip_B = {
        "A": "Y",
        "Y": "A",
        "B": "R",
        "R": "B",
        "C": "U",
        "U": "C",
        "D": "H",
        "H": "D",
        "E": "Q",
        "Q": "E",
        "F": "S",
        "S": "F",
        "G": "L",
        "L": "G",
        "I": "P",
        "P": "I",
        "J": "X",
        "X": "J",
        "K": "N",
        "N": "K",
        "M": "O",
        "O": "M",
        "T": "Z",
        "Z": "T",
        "V": "W",
        "W": "V",
    }
    reflektor_tip_C = {
        "A": "F",
        "F": "A",
        "B": "V",
        "V": "B",
        "C": "P",
        "P": "C",
        "D": "J",
        "J": "D",
        "E": "I",
        "I": "E",
        "G": "O",
        "O": "G",
        "H": "Y",
        "Y": "H",
        "K": "R",
        "R": "K",
        "L": "Z",
        "Z": "L",
        "M": "X",
        "X": "M",
        "N": "W",
        "W": "N",
        "Q": "T",
        "T": "Q",
        "S": "U",
        "U": "S",
    }

    if reflektor == "B":
        reflektor_dict = reflektor_tip_B
    else:
        reflektor_dict = reflektor_tip_C

    # A - lijevi rotor, B - srednji rotor, C - desni rotor
    rotor_A = rotor_dict[rotori[0]]
    rotor_B = rotor_dict[rotori[1]]
    rotor_C = rotor_dict[rotori[2]]

    rotor_A_zarez = rotor_zarezi_dict[rotori[0]]
    rotor_B_zarez = rotor_zarezi_dict[rotori[1]]
    rotor_C_zarez = rotor_zarezi_dict[rotori[2]]

    rotor_A_pocetno_slovo = rotori_pocetne_pozicije[0]
    rotor_B_pocetno_slovo = rotori_pocetne_pozicije[1]
    rotor_C_pocetno_slovo = rotori_pocetne_pozicije[2]

    rotor_A_pomak_postavke = abeceda.index(rotori_pomak[0])
    rotor_B_pomak_postavke = abeceda.index(rotori_pomak[1])
    rotor_C_pomak_postavke = abeceda.index(rotori_pomak[2])

    rotor_A = ceaser_crypt(rotor_A, rotor_A_pomak_postavke)
    rotor_B = ceaser_crypt(rotor_B, rotor_B_pomak_postavke)
    rotor_C = ceaser_crypt(rotor_C, rotor_C_pomak_postavke)

    if rotor_A_pomak_postavke > 0:
        rotor_A = (
            rotor_A[26 - rotor_A_pomak_postavke :]
            + rotor_A[0 : 26 - rotor_A_pomak_postavke]
        )
    if rotor_B_pomak_postavke > 0:
        rotor_B = (
            rotor_B[26 - rotor_B_pomak_postavke :]
            + rotor_B[0 : 26 - rotor_B_pomak_postavke]
        )
    if rotor_C_pomak_postavke > 0:
        rotor_C = (
            rotor_C[26 - rotor_C_pomak_postavke :]
            + rotor_C[0 : 26 - rotor_C_pomak_postavke]
        )

    ploca_s_utikacima = ploca_s_utikacima_postavke.upper().split(" ")
    ploca_s_utikacima_dict = {}
    for kombinacije_slova in ploca_s_utikacima:
        if len(kombinacije_slova) == 2:
            ploca_s_utikacima_dict[kombinacije_slova[0]] = kombinacije_slova[1]
            ploca_s_utikacima_dict[kombinacije_slova[1]] = kombinacije_slova[0]

    poruka = poruka.upper()

    for slovo in poruka:
        kriptirano_slovo = slovo

        if slovo in abeceda:
            # odmah zaokreni rotore - to se dogada prije enkripcije
            rotor_zakreni_okidac = False
            # prvo se desni rotor zaokrene za jedno slovo svaki put
            if rotor_C_pocetno_slovo == rotor_C_zarez:
                rotor_zakreni_okidac = True
            rotor_C_pocetno_slovo = abeceda[(abeceda.index(rotor_C_pocetno_slovo)) % 26]

            # provjeriti treba li zakrenuti srednji rotor
            if rotor_zakreni_okidac:
                rotor_zakreni_okidac = False
                if rotor_B_pocetno_slovo == rotor_B_zarez:
                    rotor_zakreni_okidac = True
                rotor_B_pocetno_slovo = abeceda[
                    (abeceda.index(rotor_B_pocetno_slovo)) % 26
                ]

                # ovisno na kojoj je poziciji srednji rotor, to moze uzrokovati zaokretanje lijevog
                # provjeri treba li zaokrenuti lijevi

                if rotor_zakreni_okidac:
                    rotor_zakreni_okidac = False
                rotor_A_pocetno_slovo = abeceda[
                    (abeceda.index(rotor_A_pocetno_slovo)) % 26
                ]

        else:
            # provjeri je li se dogodila situacija da se zbog okretanja srednjeg
            # rotora istovremeno treba okrenuti i lijevi i ako je, zaokreni srednji i lijevi rotor
            if rotor_B_pocetno_slovo == rotor_B_zarez:
                rotor_B_pocetno_slovo = abeceda[
                    (abeceda.index(rotor_B_pocetno_slovo) + 1) % 26
                ]
                rotor_A_pocetno_slovo = abeceda[
                    (abeceda.index(rotor_A_pocetno_slovo) + 1) % 26
                ]

        # primijeni enkripciju definiranu pomocu ploce s utikacima
        if slovo in ploca_s_utikacima_dict.keys():
            if ploca_s_utikacima_dict[slovo] != "":
                kriptirano_slovo = ploca_s_utikacima_dict[slovo]

        # primijeni enkripciju na rotorima i reflektoru
        pomak_A = abeceda.index(rotor_A_pocetno_slovo)
        pomak_B = abeceda.index(rotor_B_pocetno_slovo)
        pomak_C = abeceda.index(rotor_C_pocetno_slovo)

        # prvo enkripcija na desnom rotoru
        pozicija = abeceda.index(kriptirano_slovo)
        slovo_na_rotoru = rotor_C[(pozicija + pomak_C) % 26]
        pozicija = abeceda.index(slovo_na_rotoru)
        kriptirano_slovo = abeceda[(pozicija - pomak_C + 26) % 26]

        # zatim enkripcija na srednjem rotoru
        pozicija = abeceda.index(kriptirano_slovo)
        slovo_na_rotoru = rotor_B[(pozicija + pomak_B) % 26]
        pozicija = abeceda.index(slovo_na_rotoru)
        kriptirano_slovo = abeceda[(pozicija - pomak_B + 26) % 26]

        # pa enkripcija na lijevom rotoru
        pozicija = abeceda.index(kriptirano_slovo)
        slovo_na_rotoru = rotor_A[(pozicija + pomak_A) % 26]
        pozicija = abeceda.index(slovo_na_rotoru)
        kriptirano_slovo = abeceda[(pozicija - pomak_A + 26) % 26]

        # enkripcija na reflektoru
        if kriptirano_slovo in reflektor_dict.keys():
            if reflektor_dict[kriptirano_slovo] != "":
                kriptirano_slovo = reflektor_dict[kriptirano_slovo]

        # pa ponovno enkripcija na lijevom rotoru
        pozicija = abeceda.index(kriptirano_slovo)
        slovo_na_rotoru = abeceda[(pozicija + pomak_A) % 26]
        pozicija = rotor_A.index(slovo_na_rotoru)
        kriptirano_slovo = abeceda[(pozicija - pomak_A + 26) % 26]

        # pa ponovno enkripcija na srednjem rotoru
        pozicija = abeceda.index(kriptirano_slovo)
        slovo_na_rotoru = abeceda[(pozicija + pomak_B) % 26]
        pozicija = rotor_B.index(slovo_na_rotoru)
        kriptirano_slovo = abeceda[(pozicija - pomak_B + 26) % 26]

        # pa ponovno enkripcija na desnom rotoru
        pozicija = abeceda.index(kriptirano_slovo)
        slovo_na_rotoru = abeceda[(pozicija + pomak_C) % 26]
        pozicija = rotor_C.index(slovo_na_rotoru)
        kriptirano_slovo = abeceda[(pozicija - pomak_C + 26) % 26]

        # i na kraju jos jednom enkripcija na ploci s utikacima
        if kriptirano_slovo in ploca_s_utikacima_dict.keys():
            if ploca_s_utikacima_dict[kriptirano_slovo] != "":
                kriptirano_slovo = ploca_s_utikacima_dict[kriptirano_slovo]

        kriptirana_poruka += kriptirano_slovo

    return kriptirana_poruka


tekst_za_kriptiranje = input("Upisite poruku koju zelite kriptirati:\n")
kriptirani_tekst = enigma(tekst_za_kriptiranje)

print("\nKriptirana poruka:\n", kriptirani_tekst)

dekriptirani_tekst = enigma(kriptirani_tekst)
print("\nDekriptirana poruka:\n", dekriptirani_tekst)
