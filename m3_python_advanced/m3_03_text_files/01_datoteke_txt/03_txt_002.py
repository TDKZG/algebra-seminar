"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s datotekama
NASLOV              Uvod u rad s tekstualnim datotekama
                    Pisanje liniju po liniju
"""


# ADRESAR - Pokusaj 1
# brojac = 1
# while True:
#     ime = input("Upisite ime kontakta: ")
#     prezime = input("Upisite prezime kontakta: ")
#     telefon = input("Upisite telefon kontakta: ")

#     pisac_datoteke = open("m3_03_tekstualne_datoteke/01_datoteke_txt/adresar.txt", "w")

#     pisac_datoteke.write(f"{brojac};{ime};{prezime};{telefon}")
#     brojac += 1

#     pisac_datoteke.close()

#     if input("Zelite li unijet novi kontakt? (da/ne) ") != "da":
#         break


# ADRESAR - Pokusaj 2
# brojac = 1
# pisac_datoteke = open("m3_03_tekstualne_datoteke/01_datoteke_txt/adresar.txt", "w")

# while True:
#     ime = input("Upisite ime kontakta: ")
#     prezime = input("Upisite prezime kontakta: ")
#     telefon = input("Upisite telefon kontakta: ")

#     pisac_datoteke.write(f"{brojac};{ime};{prezime};{telefon}\n")
#     brojac += 1

#     if input("Zelite li unijet novi kontakt? (da/ne) ") != "da":
#         break

# pisac_datoteke.close()


# ADRESAR - Pokusaj 3
# brojac = 1

# while True:
#     ime = input("Upisite ime kontakta: ")
#     prezime = input("Upisite prezime kontakta: ")
#     telefon = input("Upisite telefon kontakta: ")

#     pisac_datoteke = open("m3_03_tekstualne_datoteke/01_datoteke_txt/adresar.txt", "a")

#     pisac_datoteke.write(f"{brojac};{ime};{prezime};{telefon}\n")
#     brojac += 1

#     pisac_datoteke.close()

#     if input("Zelite li unijet novi kontakt? (da/ne) ") != "da":
#         break


# ADRESAR - Pokusaj 4
# brojac = 1

# while True:
#     ime = input("Upisite ime kontakta: ")
#     prezime = input("Upisite prezime kontakta: ")
#     telefon = input("Upisite telefon kontakta: ")

#     try:
#         pisac_datoteke = open(
#             "m3_03_tekstualne_datoteke/01_datoteke_txt/adresar.txt", "a"
#         )
#         pisac_datoteke.write(f"{brojac};{ime};{prezime};{telefon}\n")
#         brojac += 1

#     except Exception as e:
#         print(f"Dogodila se pogreska {e}")

#     finally:
#         # bez obzira je li se dogodila greska ili nije
#         # UVIJEK cemo zatvoriti komunikaciju prema datoteci
#         pisac_datoteke.close()

#     if input("Zelite li unijet novi kontakt? (da/ne) ") != "da":
#         break


# ADRESAR - Pokusaj 5
brojac = 1

while True:
    ime = input("Upisite ime kontakta: ")
    prezime = input("Upisite prezime kontakta: ")
    telefon = input("Upisite telefon kontakta: ")

    try:
        with open(
            "m3_03_tekstualne_datoteke/01_datoteke_txt/adresar2.txt", "a"
        ) as pisac_datoteke:
            pisac_datoteke.write(f"{brojac};{ime};{prezime};{telefon}\n")
            brojac += 1

    except Exception as e:
        print(f"Dogodila se pogreska {e}")

    if input("Zelite li unijet novi kontakt? (da/ne) ") != "da":
        break
