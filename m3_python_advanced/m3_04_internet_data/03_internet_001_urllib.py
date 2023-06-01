"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s podacima s Interneta
NASLOV              urllib i requests moduli
"""

import urllib.request
import urllib.parse

# Adresa koju zelimo otvoriti
URL = "https://www.algebra.hr"

# objekt koji predstavlja konekciju prema adresi
konekcija = urllib.request.urlopen(URL)

# citanje i dekodiranje sadrzaja koristeci konekciju
stranica = konekcija.read().decode()


print(stranica)
