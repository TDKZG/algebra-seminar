"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Korisnicki definirani tipovi podataka
NASLOV              Moduli - datetime, dateutil i time moduli
                    Ucitavanje od korisnika ili iz nekog drugog izvora
                    Racunanje s datumima
"""

import datetime as dt

# pip3 install python-dateutil
from dateutil import tz

# datum_korisnik = input(
#     "Upisite danasnji datum i vrijeme u formatu: dan. naziv_mjeseca godina. sati:minuta:sekunda - "
# )
# datum_korisnik = "14. February 2023. 18:52:23"
# datum_objekt = dt.datetime.strptime(datum_korisnik, "%d. %B %Y. %H:%M:%S")
# print(datum_korisnik)
# print(datum_objekt)

# print(datum_objekt.year)
# print(datum_objekt.month)

sadasnji_trenutak = dt.datetime.now()
novi_datum_objekt = dt.datetime.strptime("24. July 1975. 4:45:4", "%d. %B %Y. %H:%M:%S")

razlika = sadasnji_trenutak - novi_datum_objekt
print(razlika)

# zbroj = novi_datum_objekt + sadasnji_trenutak
# print(zbroj)

za_2_tjedna = sadasnji_trenutak + dt.timedelta(days=14, hours=14)
print(za_2_tjedna)


danas = dt.date.today()
jucer = danas - dt.timedelta(days=1)
sutra = danas + dt.timedelta(days=1)

print("Jucerasnji dan:", jucer)
print("Danasnji dan:", danas)
print("Sutrasnji dan:", sutra)


# datum = dt.date(2023, 2, 20)
# print(datum)

# VREMENSKE ZONE
tz_tk = tz.gettz("Asia/Tokyo")
termin_olimpijskih_tk = dt.datetime(2021, 7, 23, 20, tzinfo=tz_tk)

tz_zg = tz.gettz("Europe/Zagreb")
termin_olimpijskih_zg = termin_olimpijskih_tk.astimezone(tz_zg)

tz_ny = tz.gettz("America/New_York")
termin_ny = termin_olimpijskih_tk.astimezone(tz_ny)

print(
    f"Otvorenje olimpijskih igara u Tokyu pocinje u {termin_olimpijskih_tk.strftime('%A %d.%m.%Y. %H:%M')}"
)
print(
    f"Termin u Zagrebu pocinje u {termin_olimpijskih_zg.strftime('%A %d.%m.%Y. %H:%M')}"
)
print(f"Termin u New Yorku pocinje u {termin_ny.strftime('%A %d.%m.%Y. %H:%M')}")
