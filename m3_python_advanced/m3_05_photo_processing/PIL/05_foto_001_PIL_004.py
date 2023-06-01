"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              PIL Python library
"""


from PIL import Image

putanja_fotografije = "m3_05_foto/Fotografije/Algebra_campus.jpg"

fotografija = Image.open(putanja_fotografije)

fotografija_crno_bijela = fotografija.convert(mode="L")

fotografija_crno_bijela.save("m3_05_foto/Fotografije/Algebra_campus_crno_bijela.jpg")

fotografija_crno_bijela.show()
