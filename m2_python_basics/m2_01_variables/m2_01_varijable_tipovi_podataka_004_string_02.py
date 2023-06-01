"""
MODUL       Modul 2 - Osnove programiranja u Pythonu
TEMA        Varijable i tipovi podataka
NASLOV      STRING - Tekstualni tip podataka
"""


ime = "Petar"
prezime = "Perić"
godina_rodenja = 1995

print(f"Godine {godina_rodenja}. je rodena osoba: {ime} {prezime}")

print(f"\tGodine {godina_rodenja}. je rodena osoba: {ime} {prezime}")

print(f"\tGodine {godina_rodenja}. \n\tje rodena osoba: {ime} {prezime}")


print(
    f"Godine {godina_rodenja}. je rodena osoba: {ime} {prezime}. To je tocno 1\\4 stoljeca"
)


# Ime i prezime osobe dodano u dvostruke navodnike pomoću Escape Charactera
print(f'Godine {godina_rodenja}. je rodena osoba: "{ime} {prezime}".')
