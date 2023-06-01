def generiraj_akord(pocetni_ton, tonovi, tip):
    indeks_pocetnog_tona = tonovi.index(pocetni_ton)
    if tip == "dur":
        akord = [pocetni_ton, tonovi[indeks_pocetnog_tona + 3], tonovi[indeks_pocetnog_tona + 6]]
    elif tip == "mol":
        akord = [
            pocetni_ton,
            tonovi[indeks_pocetnog_tona + 2],
            tonovi[indeks_pocetnog_tona + 6],
        ]
    return akord


tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]
tonovi.extend(tonovi)

pocetni_ton = input("Unesite pocetni ton akorda: ").upper()
tip = input("Koji tip akorda zelis: ")
bla = generiraj_akord(pocetni_ton, tonovi, tip)
print(bla)
