"""
MODUL       Modul 2 - Osnove programiranja u Pythonu
TEMA        Varijable i tipovi podataka
NASLOV      STRING - Tekstualni tip podataka
"""


ime = "Petar"
prezime = "Peric"
puno_ime = ime + " " + prezime
# print(puno_ime + ".")

# Nacin slican pisanju recenice
# 1. korak - napisemo recenicu koju zelimo imati tekst
"Puno ime i prezime je: Petar Peric"
# 2. korak - nakon zadnjeg navodnika bez razmaka dodajemo tocku i iza toga pisemo format()
"Puno ime i prezime je: Petar Peric".format()
# 3. korak - iz teksta izbrisemo vrijednosti koje zelimo zamijenit s varijablom i umjesto toga stavimo vitice
#            i zatim dodamo te varijable po redu u format
"Puno ime i prezime je: {} {}".format(ime, prezime)

puno_ime = "Puno ime i prezime je: {} {}".format(ime, prezime)
print(puno_ime)

# postoji i kraci nacin
# F-strings
puno_ime = f"Puno ime i prezime je: {ime} {prezime}"
print(puno_ime)


print(f"Puno ime i prezime je: {ime} {prezime}")

input(f"{ime} upisi svoje prezime: ")


tekst = "Puno ime i prezime \\tea"
print(tekst)
