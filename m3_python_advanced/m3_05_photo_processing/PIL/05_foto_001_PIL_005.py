"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              PIL Python library
"""


from PIL import Image


logo_fotografija = Image.open("m3_05_foto/Fotografije/Python_logo_and_wordmark.png")
kampus_fotografija = Image.open("m3_05_foto/Fotografije/Algebra_campus.jpg")

print(logo_fotografija.size)
print(kampus_fotografija.size)

kampus_fotografija.paste(logo_fotografija, (500, 300))

kampus_fotografija.show()
