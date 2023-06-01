"""
MODUL               Modul 4 - Python u području Internet stvari (IoT)
TEMA                Vjezba pisanja koda na Raspberry Pi OS
NASLOV              Uvod u izradu simulatora uredaja Enigma - Cezar enkripcija
"""


def ceaser_crypt(poruka, pomak, dekriptiraj=False):

    if dekriptiraj:
        kljuc = 26 - pomak
    else:
        kljuc = pomak

    rezultat = ""
    poruka_velika_slova = poruka.upper()

    for i in range(len(poruka)):
        slovo = poruka_velika_slova[i]
        ascii_code = ord(slovo)
        if (ascii_code >= 65) and (ascii_code <= 90):
            slovo = chr(((ascii_code - 65 + kljuc) % 26) + 65)
        rezultat += slovo

    return rezultat


# while True:
#     poruka = input("Upisi poruku: ")
#     kriptirana_poruka = ceaser_crypt(poruka, 5)
#     dekriptirana_poruka = ceaser_crypt(kriptirana_poruka, 5, True)
#     print(kriptirana_poruka)
#     print(dekriptirana_poruka)


poruka = "Ovo je poruka"
kriptirana_poruka = ceaser_crypt(poruka, 10)
# dekriptirana_poruka = ceaser_crypt(kriptirana_poruka, 5, True)


ABECEDA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for pomak in range(len(ABECEDA)):
    hakirana_poruka = ""
    for slovo in kriptirana_poruka:
        if slovo in ABECEDA:
            broj = ABECEDA.find(slovo)
            broj -= pomak
            if broj < 0:
                broj += len(ABECEDA)
            hakirana_poruka += ABECEDA[broj]
        else:
            hakirana_poruka += slovo

    print(f"Za pomak {pomak}, izvorna poruka glasi: {hakirana_poruka}")
