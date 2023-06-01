"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Korisnicki definirani tipovi podataka
NASLOV              Moduli - datetime, dateutil i time moduli
"""

import datetime as dt
import locale

# Danasnji datum
danasnji_dan = dt.date.today()
print(f"\nDanasnji dan je {danasnji_dan}")
# YYYY-MM-DD

# Sadasnji trenutak
sadasnji_trenutak = dt.datetime.now()
print(f"\nSadasnji trenutak je {sadasnji_trenutak}")
# YYYY-MM-DD HH:MM:SS.MS


### Dan u tjednu
dan_u_tjednu = dt.date.weekday(danasnji_dan)
print(f"Danas je {dan_u_tjednu}. dan u tjednu")  # pocinje od 0
print(f"ISPRAVNO: Danas je {dan_u_tjednu+1}. dan u tjednu")

if dan_u_tjednu == 0:
    print(f"Danas je PONEDJELJAK, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 1:
    print(f"Danas je UTORAK, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 2:
    print(f"Danas je SRIJEDA, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 3:
    print(f"Danas je CETVRTAK, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 4:
    print(f"Danas je PETAK, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 5:
    print(f"Danas je SUBOTA, {dan_u_tjednu+1}. dan u tjednu")
elif dan_u_tjednu == 6:
    print(f"Danas je NEDJELJA, {dan_u_tjednu+1}. dan u tjednu")


print("\nDan u tjednu '%A' - puni naziv, a '%a' - skraceni naziv")

print(f"Puni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%A')}.")
print(f"Kraci naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%a')}.")


locale.setlocale(locale.LC_TIME, "hr_HR")
print(f"HRV Puni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%A')}.")
print(f"HRV Kraci naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%a')}.")
print(f"HRV Kraci naziv danasnjeg dana u tjednu je {danasnji_dan.strftime('%A')[:3]}.")

locale.setlocale(locale.LC_ALL, "")

# ISPIS GODINE
print("\nTEKUCA GODINA '%Y' - puni naziv, a '%y' - skraceni naziv\n")
print(f"4 znamenke - Tekuca godina je {danasnji_dan.strftime('%Y')}. godina")
print(f"2 znamenke - Tekuca godina je {danasnji_dan.strftime('%y')}. godina")

print("\nBroj danasnjeg dana u godini: '%j")
print(
    f"Danas je {danasnji_dan.strftime('%j')}. dan u {danasnji_dan.strftime('%Y')}. godini"
)

print("\nBroj tjedna u godini: '%W'")
print(
    f"Danas je {danasnji_dan.strftime('%W')}. tjedan u {danasnji_dan.strftime('%Y')}. godini"
)


# ISPIS MJESECA
print("\nTEKUCI MJESEC '%B' - puni naziv, '%b' - kraci naziv, '%m' - broj")

print(f"Puni naziv mjeseca je {danasnji_dan.strftime('%B')}")
print(f"Kraci naziv mjeseca je {danasnji_dan.strftime('%b')}")
print(f"Danasnji mjesec je {danasnji_dan.strftime('%m')}")


# KOMBINIRANI PRIKAZ
print("\n\nKOMBINIRANJE prikaza pomocu strftime()\n")
print(
    f"Sadasnji trenutak: {sadasnji_trenutak.strftime('%A')}, {sadasnji_trenutak.strftime('%d.%m.%Y %H:%M:%S')}"
)
