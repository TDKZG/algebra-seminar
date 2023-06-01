"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              PIL Python library
"""


from PIL import Image, ImageDraw


fotografija = Image.open("m3_05_foto/Fotografije/Algebra_campus.jpg")

fotografija_crtanje = ImageDraw.Draw(fotografija)

fotografija_crtanje.rectangle(
    (2500, 610, 3330, 1250), fill=None, outline="red", width=5
)
# fotografija.show()


fotografija_crtanje.ellipse(
    (2500, 610, 3330, 1250), fill=None, outline="blue", width=10
)
fotografija.show()
