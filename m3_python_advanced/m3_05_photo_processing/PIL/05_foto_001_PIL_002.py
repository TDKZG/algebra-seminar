"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s foto datotekama
NASLOV              PIL Python library
"""


from PIL import Image

putanja_fotografije = "m3_05_foto/Fotografije/Algebra_campus.jpg"

fotografija = Image.open(putanja_fotografije)

# fotografija.crop()


# ORIGINALNA
# lijeva stranica = 0
# gornja stranica = 0
# desna stranica = 3992
# donja stranica = 2242

# CROPANA
# lijeva stranica = 0+500
# gornja stranica = 0+500
# desna stranica = 0+3992-500
# donja stranica = 0+2242-500


lijevo = 0 + 500
gore = 0 + 500
desno = 0 + fotografija.size[0] - 500
dolje = 0 + fotografija.size[1] - 500

fotografija_crop = fotografija.crop((lijevo, gore, desno, dolje))

fotografija.show()
fotografija_crop.show()
