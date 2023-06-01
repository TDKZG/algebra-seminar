"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              PIL Python library
"""


from PIL import Image

putanja_fotografije = "m3_05_foto/Fotografije/Algebra_campus.jpg"

fotografija = Image.open(putanja_fotografije)

lijevo = 0 + 500
gore = 0 + 500
desno = 0 + fotografija.size[0] - 500
dolje = 0 + fotografija.size[1] - 500

fotografija_crop = fotografija.crop((lijevo, gore, desno, dolje))

fotografija_crop.save("m3_05_foto/Fotografije/Algebra_campus_crop.jpg", "JPEG")
fotografija_crop.save("m3_05_foto/Fotografije/Algebra_campus_crop.png")
