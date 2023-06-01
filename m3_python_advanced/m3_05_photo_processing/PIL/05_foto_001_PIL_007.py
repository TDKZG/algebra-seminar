"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              PIL Python library
"""


from PIL import Image


fotografija = Image.open("m3_05_foto/Fotografije/Algebra_campus.jpg")

fotografija.close()
