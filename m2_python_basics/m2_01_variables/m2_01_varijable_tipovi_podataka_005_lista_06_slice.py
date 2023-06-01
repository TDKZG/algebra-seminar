"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    NAREDBA SLICE izrezivanje liste i kolekcije podataka
"""

brojevi = []
for broj in range(0, 101):
    brojevi.append(broj)

print(brojevi)
print()

# zelimo izdvojiti brojeve od 20 do 40
range(20, 41, 1)
izdvojeni_brojevi = brojevi[:10:2]
print(izdvojeni_brojevi)


# NAZIV_LISTE[START : STOP]


# NAZIV_LISTE[START : ]


# NAZIV_LISTE[ : STOP]


# elementi od PREDZADNJEG ELEMENTA do kraja liste
# izdvojeni_brojevi = brojevi[]


lista_brojeva = []
for broj in range(0, 101):
    lista_brojeva.append(broj)
print(lista_brojeva)


# elementi od prvog elementa do PREDZADNJEG - podrazumijeva se da je STEP = 1
izdvojeni_brojevi = lista_brojeva[:-1]
print(izdvojeni_brojevi)

print()

izdvojeni_brojevi = brojevi[::-1]
print(izdvojeni_brojevi)
