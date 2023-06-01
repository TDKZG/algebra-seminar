"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    DICTIONARY - rjecnik
"""

stanovnistvo_lista = [
    "Petar Peric",
    "Marko Maric",
    "Ivan Ivic",
    "Josip Josipovic",
    "Marko Maric",
]

stanovnistvo = {
    "1345028745": "Petar Peric",
    "7826548763": "Marko Maric",
    "2984376248": "Ivan Ivic",
    "243654356": "Josip Josipovic",
    "2345435": "Marko Maric",
}


# dohvacanje vrijednosti iz rijecnika pomocu kljuca
vrijednost_elementa = stanovnistvo["2345435"]
print(vrijednost_elementa)


# dodavanje novog para vrijednost-kljuc u rijecnik
stanovnistvo["134059783"] = "Hrvoje Horvat"
print(stanovnistvo)


# pregaziti vrijednost pod odredenim kljucem
stanovnistvo["1345028745"] = "Petar Pericic"
print(stanovnistvo)


# FOR PETLJA ZA DICT

# ispisati sve kljuceve iz rijecnika

for key in stanovnistvo.keys():
    print(key)


for key in stanovnistvo.keys():
    print(stanovnistvo[key])

for value in stanovnistvo.values():
    print(value)


for key, value in stanovnistvo.items():
    print(key)
    print(value)
    print()


stanovnistvo = {
    0: ["Petar", "Peric", 30, "zaposlen"],
    1: ["Marko", "Maric", 32, "zaposlen"],
    2: ["Ivan", "Ivic", 350, "zaposlen"],
    3: ["Josip", "Josipovic", 3, "nezaposlen"],
    4: ["Marko", "Maric", 43, "zaposlen"],
    5: ["Hrvoje", "Horvat", 32, "nezaposlen"],
}


# zelimo ispisati prezime osobe pod identifikatorom 123443265

lista = stanovnistvo["123443265"]
print(lista[1])

print(stanovnistvo["123443265"][1])
