"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s podacima s Interneta
NASLOV              Web API
"""

import requests
import json

URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(URL)
users = json.loads(response.text)
first_user = users[0]
print(first_user["address"])
