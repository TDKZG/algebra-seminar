"""
MODUL   Osnove programiranja u Pythonu
TEMA    Varijable i tipovi podataka
NASLOV Naredba print()
"""


ime = "Petar"
prezime = "Perić"
godina_rodenja = 1995
drzava_rodenja = "Republika Hrvatska"
zaposlen = True
tezina = 86.7
spol = "M"


# Hardcoded tekst koristimo za tekst i poruke koje nećemo mijenjati tijekom izvršavanja programa
print("Petar")

# Drugi print će ispisivati vrijednost varijable koja god to vrijednost bila pohranjena u varijabli
print(ime)


# Ispišimo na ekran ime Petar i vrijednost varijable "ime" s jednim praznim redom između njih
print("Petar")
print()
print(ime)


# ZADATAK: Ako vrijedi gornji opis, kako onda možemo ispisati ime i prezime hardcoded i pomoću varijabli
print("Petar Peric")
print("Petar" + " Peric")
print("Petar", "Peric")
print(ime, prezime)


# ZADATAK: Dodajte na kraju ispisa imena i prezimena točku.
print("Petar Peric.")
print("Petar", " Peric", ".", sep="")
print(ime, " ", prezime, ".", sep="")


naziv = "Top Gun: Maverick"
godina_objavljivanja = 2022
autor = "Joseph Kosinski"
prosjecna_ocjena = 8.3
dobitnik_oscara = "Saznati ćemo večeras"

print("Naziv filma:", naziv)
print("Godina objavljivanja: ", godina_objavljivanja, ".", " godine", sep="")
print("Autor filma:", autor)
print("Prosječna ocjena: ", prosjecna_ocjena, "/10", sep="")
print("Dobitnik oscara:", dobitnik_oscara)


stranica_a = 10
stranica_b = 5
povrsina = stranica_a * stranica_b

print(
    "Povrsina cetverokuta stranica",
    stranica_a,
    "i",
    stranica_b,
    "iznosi",
    povrsina,
    "cm2",
)


cijena_struje = 0.95
dnevna_potrosnja = 2
snaga_mikrovalne_pecnice = 1.3
broj_dana_u_mjesecu = 30
pdv = 0.25

trosak = (
    snaga_mikrovalne_pecnice * dnevna_potrosnja * broj_dana_u_mjesecu * cijena_struje
)
trosak_pdv = trosak * (1 + pdv)

print("mjesecni trosak (bez pdv-a):", trosak)
print("mjesecni trosak (s pdv-om):", trosak_pdv)

ime = input("Upisite ime: ")
print("Bok", ime)


a = input("Upišite prvi broj: ")
b = input("Upišite drugi broj: ")
zbroj = a + b
razlika = a - b
umnozak = a * b
kolicnik = a / b
potencija = a**b
modulo = a % b

print(a, "+", b, "=", zbroj)
print(a, "-", b, "=", razlika)
print(a, "*", b, "=", umnozak)
print(a, "/", b, "=", kolicnik)
print(a, "**", b, "=", potencija)
print(a, "%", b, "=", modulo)


naziv_filma = "Top Gun"
godina = 1987
autor = "Netko"
ocjena = 8.5
dobitnik_Oskara = True


print(
    f"Movie title: {naziv} \nYear of release: {godina} \nDirector: {autor} \nAverage rating:"
    + ocjena
    + "\nOscar winner:"
    + dobitnik_Oskara
)


naziv = "Titanic"
godina_obj = "1997"
autor = "James Cameron"
prosjecna_ocjena = "7,9"
dobitnik_oscara = True

print(
    f"Naziv: {naziv} \n Godina objavljivanja: {godina_obj} \n Autor: {autor}",
    "\n",
    f"Prosječna ocjena: {prosjecna_ocjena}",
    "\n",
    sep="",
)
