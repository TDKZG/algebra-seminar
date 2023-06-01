"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              PIL Python library
"""


from PIL import Image

putanja_fotografije = "m3_05_foto/Fotografije/Algebra_campus.jpg"

fotografija = Image.open(putanja_fotografije)


print(f"Format fotografije: {fotografija.format}")
print(f"Mod fotografije: {fotografija.mode}")
print(f"Dimenzije fotografije: {fotografija.size}")

# fotografija.show()
