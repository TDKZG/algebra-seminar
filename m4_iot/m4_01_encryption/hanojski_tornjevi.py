"""
MODUL               Modul 4 - Python u području Internet stvari (IoT)
TEMA                Vjezba pisanja koda na Raspberry Pi OS
NASLOV              Rekurzivne funkcije - funkcije koje pozivaju same sebe
"""


def hanojski_tornjevi(broj_diskova, stap_pocetni, stap_odredisni, stap_pomocni):
    if broj_diskova == 1:
        print(
            f"Prebaci disk {broj_diskova} sa stapa {stap_pocetni} na {stap_odredisni} stap"
        )
        return

    hanojski_tornjevi(broj_diskova - 1, stap_pocetni, stap_pomocni, stap_odredisni)

    print(
        f"Prebaci disk {broj_diskova} sa stapa {stap_pocetni} na {stap_odredisni} stap"
    )

    hanojski_tornjevi(broj_diskova - 1, stap_pomocni, stap_odredisni, stap_pocetni)


broj_diskova = 5
hanojski_tornjevi(broj_diskova, "A", "C", "B")
