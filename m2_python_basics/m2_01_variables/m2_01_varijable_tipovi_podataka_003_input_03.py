"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              Naredba input()
                    KONVERZIJA TIPOVA PODATAKA
"""


# Sada kada znamo da pomoću naredbe input() UVIJEK dobijemo tekst,
# idemo vidjeti kako možemo tekst konvertirati u broj.

a = int(input("Upišite prvi broj: "))
b = int(input("Upišite drugi broj: "))

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

a = 192
b = 168
c = 0
d = 184

print(a, ".", b, ".", c, ".", d, sep="")
print(bin(a), ".", bin(b), ".", bin(c), ".", bin(d), sep="")
print(hex(a), ".", hex(b), ".", hex(c), ".", hex(d), sep="")
print(oct(a), ".", oct(b), ".", oct(c), ".", oct(d), sep="")


cijena_goriva = 9.56
potrosnja_automobila = float(input("Kolika je potrošnja automobila na 100 km: "))
potrosnja_1km = potrosnja_automobila / 100
trosak_1km = potrosnja_1km * cijena_goriva  # izračun cijene za 1 km vožnje
udaljenost = float(input("Kolika je udaljenost do vašeg radnog mjesta u kilometrima: "))
mjesecni_trosak = trosak_1km * udaljenost * 2 * 30

print("Potrošnja po 1 km vožnje je: ", round(trosak_1km, 2), "kn")
print(
    "Mjesečni trošak goriva ukoliko je udaljenost do radnog mjesta",
    udaljenost,
    "km: ",
    round(mjesecni_trosak, 2),
    "kn",
)
