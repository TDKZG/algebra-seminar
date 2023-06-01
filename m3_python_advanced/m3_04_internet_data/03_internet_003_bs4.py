"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s podacima s Interneta
NASLOV              BeautifulSoup modul
"""


import requests
from bs4 import BeautifulSoup

URL = "https://www.algebra.hr"
URL_COVID = "https://www.worldometers.info/coronavirus"

# response = requests.get(URL)

# page = BeautifulSoup(response.content)

# paragraphs = page.find_all("p")
# for p in paragraphs:
#     print(p)

# print(page.prettify())


response = requests.get(URL_COVID)
covid_page = BeautifulSoup(response.content, "html.parser")

data = covid_page.find_all("div", id="maincounter-wrap")
# print(data)
# coronavirus_cases = data[0]
# heading = coronavirus_cases.find("h1").get_text()
# value = coronavirus_cases.find("span").get_text()
# print(value)

for item in data:
    heading = item.find("h1").get_text()
    value = item.find("span").get_text()
    print(heading, value)
