"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s datotekama
NASLOV              Uvod u rad s JSON datotekama

NAPOMENA            Putanja do datoteke je UVIJEK vrsni folder u kojem je otvoren projekt.
"""

# preduvjet

import json


user = {
    "id": 1,
    "firstName": "Petar Peric",
    "lastName": "Petar Peric",
    "username": "pperic",
    "email": "pperic@email.adresa",
    "address": {"street": "Ilica 256", "city": "Zagreb", "zipcode": "10000"},
    "phone": "+385 1 8031 564",
    "website": "web.adresa",
    "company": {
        "name": "Medvednica d.o.o.",
        "catchPhrase": "Razvoj specijaliziranih Python aplikacija",
        "bs": "Najbolja poslovna rjesenja",
    },
}

# 1. nacin
try:
    with open(
        "m3_03_tekstualne_datoteke/02_datoteke_json/user_p02.json", "w"
    ) as file_writer:
        json.dump(user, file_writer)
except Exception as e:
    print(f"Dogodila se pogreska {e}")


try:
    with open(
        "m3_03_tekstualne_datoteke/02_datoteke_json/user_p02.json", "w"
    ) as file_writer:
        content = json.dumps(user)
        file_writer.write(content)
except Exception as e:
    print(f"Dogodila se pogreska {e}")
