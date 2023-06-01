"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Korisnicki definirani tipovi podataka
NASLOV              Klase - nasljedivanje
"""


# class Osoba:
#     def __init__(self):
#         self.ime = "Pero"
#         self.oib = "46456"
#         self.adresa = "Ilica"


# class Tvrtka:
#     def __init__(self):
#         self.ime = ""
#         self.oib = ""
#         self.adresa = ""
#         self.broj_djelatnika = 0
#         self.pravni_oblik = ""


# class Djelatnik:
#     def __init__(self):
#         self.ime = ""
#         self.oib = ""
#         self.adresa = ""
#         self.radno_mjesto = ""


# class Tvrtka(Osoba):
#     def __init__(self):
#         super().__init__()
#         self.broj_djelatnika = 0
#         self.pravni_oblik = ""


# class Djelatnik(Osoba):
#     def __init__(self):
#         super().__init__()
#         self.radno_mjesto = ""


class Osoba:
    def __init__(self, ime, oib, adresa):
        self.ime = ime
        self.oib = oib
        self.adresa = adresa


# class Tvrtka:
#     def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
#         self.ime = ime
#         self.oib = oib
#         self.adresa = adresa
#         self.broj_djelatnika = broj_djelatnika
#         self.pravni_oblik = pravni_oblik


# class Djelatnik:
#     def __init__(self, ime, oib, adresa, radno_mjesto):
#         self.ime = ime
#         self.oib = oib
#         self.adresa = adresa
#         self.radno_mjesto = radno_mjesto


class Tvrtka(Osoba):
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        super().__init__(ime, oib, adresa)
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik


class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, radno_mjesto):
        super().__init__(ime, oib, adresa)
        self.radno_mjesto = radno_mjesto


ime = input("unesi ime")
oib = input("")
adresa = "Ilica 50"
djelatnost = "programer"

djelatnik = Djelatnik(ime, oib, adresa, djelatnost)
# print(djelatnik.ime)
