"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    STRING KAO LISTA ZNAKOVA
"""

rijec = "Programiranje"

lista_znakova = ["p", "r", "o", "g", "r", "a"]

for znak in lista_znakova:
    print(znak)


for znak in rijec:
    print(znak)


# koristeci f-string i varijablu rijec
# Broj slova u rijeci programiranje je 13

print(f"Broj slova u rijeci {rijec} je {len(rijec)}")
print()
print(f"Zbroj slova u rijeci {rijec} je {sum(rijec)}")
print()

print(ord("A"))

suma = 0

for slovo in rijec:
    suma += ord(slovo)

print(suma / len(rijec))
