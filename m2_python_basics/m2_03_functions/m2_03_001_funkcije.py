"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                FUNKCIJE
"""


import datetime

# def pozdrav(ime):
#     """
#     Funkcija koja na konzolu ispisuje pozdravnu poruku osobi
#     cije ime je proslijedeno u funkciju kao parametar
#     """
#     print(f"Dobar dan, {ime}. Kako ste danas?")


def pozdrav(ime):
    """
    Funkcija koja ovisno o dobu dana vrati pozivatelju pozdravnu poruku
    za osobu cije ime smo poslali
    """
    if datetime.datetime.now().hour < 12:
        return f"Dobro jutro, {ime}. Danas je novi dan"
    elif datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 19:
        return f"Dobro dan, {ime}. Dobro vam ide, nastavite tako"
    else:
        return f"Dobra vece, {ime}. Danasnji dan je bio uspjesan"


pozdrav_imenu = pozdrav("Petar")
print(pozdrav_imenu)


unos_korisnika = input("Upisi nesto: ")
print(unos_korisnika)


def pozdrav(ime):
    print("Bok", ime)


pozdrav("Petar")
