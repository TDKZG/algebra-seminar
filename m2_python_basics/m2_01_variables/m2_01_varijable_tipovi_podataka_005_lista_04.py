"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    OSNOVNE naredbe za manipulaciju listama i kolekcijama podataka
"""


brojevi = [70, 72, 75]

# for petlju
# range funkciju
# append za dodati u listu

for element in range(1, 100):
    brojevi.append(element)


# zelimo dodati broj 80 u listu brojevi
brojevi.append(80)
brojevi += [80, 81, 82, 53]

print(brojevi)


lista = [3.14, 6, "bok", True]

element_liste = lista[2]
print(lista[2])
print(lista[-1])


brojevi = [1, 2, 3, 4, 5, 6, 7]

zbroj = 0
for broj in brojevi:
    zbroj += int(broj)

zbroj = sum(brojevi)

print(zbroj)


# prosjek = zbroj / broj elemenata

zbroj = sum(brojevi)
broj_elemenata = len(brojevi)
prosjek = zbroj / broj_elemenata
print(prosjek)
