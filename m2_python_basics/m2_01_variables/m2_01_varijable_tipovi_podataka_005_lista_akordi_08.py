"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    ZADATAK AKORDI
"""

tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]


print("Lista svih tonova pocevsi od C:")
for ton in tonovi:
    print(ton, end=" ")
print()

tonovi.extend(tonovi)

pocetni_ton = input("Unesite pocetni ton akorda: ")
veliki_pocetni_ton = pocetni_ton.upper()
indeks_pocetnog_tona = tonovi.index(veliki_pocetni_ton)

print(
    f"{veliki_pocetni_ton} dur akord cine tonovi {veliki_pocetni_ton}, {tonovi[indeks_pocetnog_tona + 3]}, {tonovi[indeks_pocetnog_tona+6]}"
)

print(
    f"{veliki_pocetni_ton} mol akord cine tonovi {veliki_pocetni_ton}, {tonovi[indeks_pocetnog_tona + 2]}, {tonovi[indeks_pocetnog_tona+6]}"
)
