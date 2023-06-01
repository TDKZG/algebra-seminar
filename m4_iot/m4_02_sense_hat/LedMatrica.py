"""
MODUL               Modul 4 - Python u području Internet stvari (IoT)
TEMA                Vjezba koristenja senzora pomocu Sense HAT Emulatora
NASLOV              Upoznavanje sa Sense HAT Emulatorom
                    LED 8x8 matrica
                    Moguce je testirati ovaj modul i unutar Internet preglednika na adresi:
                    https://trinket.io/sense-hat
"""



from sense_emu import SenseHat
sense = SenseHat()
sense.show_message('Cestitam, uspjeli ste!')

plavo = (0, 0, 255)
sense.show_message('Cestitam, uspjeli ste!', text_colour = plavo)

pozadina = (0, 255, 0)
sense.show_message('Cestitam, uspjeli ste!', 
            text_colour = plavo, 
            scroll_speed = 0.05,
            back_colour = pozadina)

while True:
    sense.show_message('Cestitam, uspjeli ste!', 
                text_colour = plavo, 
                scroll_speed = 0.05,
                back_colour = pozadina)


while True:
    sense.show_letter('Cestitam, uspjeli ste!', 
                text_colour = plavo, 
                scroll_speed = 0.05,
                back_colour = pozadina)
    
# NE radi zato jer slovo ce UVIJEK biti prikazano, a osim toga slovo nema scroll_speed, 
# jer se ne pomice zato sto slovo stane na matricu i nema potrebe ga pomicati
# Pa bi ispravn kod bio:
sense.show_letter('P', 
                text_colour = plavo, 
                back_colour = pozadina)
                

### 2. Prikaz slika tocku po tocku
# Naredba set_pixel() nam to omogucava. Ova naredba prima tri parametra:
    # x koordinata - od 0 do 7
    # y koordinata - od 0 do 7
    # polje koje definira RBG boju
# Ishodiste 0,0 je gornji lijevi kut
sense.set_pixel(0, 2, [255, 0, 0])

sense.clear()
sense.set_pixel(0, 2, [255, 0, 0])

sense.clear(plavo)
sense.set_pixel(0, 2, pozadina)

R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
W = (255, 255, 255)

slika = [
    G, G, G, G, G, G, G, G,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    G, G, G, G, G, G, G, G,
]

sense.set_pixels(slika)


sense.set_rotation(90)


kutevi = [0, 90, 180, 270, 0, 90, 180, 270]

for kut in kutevi:    
    sense.set_rotation(kut)
    time.sleep(0.5)
