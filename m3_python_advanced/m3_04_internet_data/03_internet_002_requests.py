"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s podacima s Interneta
NASLOV              requests moduli
"""

import requests

URL = "https://www.algebra.hr"
response = requests.get(URL)
print(response.status_code)
print(response.content)
print(response.headers)
print(response.text)
