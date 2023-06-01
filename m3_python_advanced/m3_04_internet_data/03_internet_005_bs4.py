"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s podacima s Interneta
NASLOV              Beautifull Soup modul
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com/")
data = BeautifulSoup(response.content, "html.parser")


price_selector = ".price_color"
heading_selector = ".product_pod h3 a"
rating_selector = ".star-rating"

price_element = data.select(price_selector)
