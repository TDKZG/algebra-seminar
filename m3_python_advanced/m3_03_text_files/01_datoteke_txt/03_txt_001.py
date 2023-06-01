"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s datotekama
NASLOV              Uvod u rad s tekstualnim datotekama

NAPOMENA            Putanja do datoteke je UVIJEK vrsni folder u kojem je otvoren projekt.
"""


# PISANJE U DATOTEKU

# 1. korak - otvaranje datoteke za pisanje
pisac_u_datoteku = open("m3_03_tekstualne_datoteke/01_datoteke_txt/ime.txt", "w")

# 2.1. kreiranje sadrzadaja koji zelimo zapisati u datoteku
ime = input("Upisite ime i prezime: ")

# 2.2. zapisivanje sadrzaja u datoteku
pisac_u_datoteku.write(ime)

# 3. zatvoriti datoteku!
pisac_u_datoteku.close()


# CITANJE IZ DATOTEKE

# 1. korak - otvoriti datoteku za citanje
citac_datoteke = open("m3_03_tekstualne_datoteke/01_datoteke_txt/ime.txt", "r")

# 2. korak - kreiraj varijablu i spremi u nju sadrzaj datoteke
podaci_datoteke = citac_datoteke.read()

# 3. korak - zatvorite datoteku!
citac_datoteke.close()

print(f"Sadrzaj datoteke je\n{podaci_datoteke}")
