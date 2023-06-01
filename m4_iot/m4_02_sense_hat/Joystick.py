"""
MODUL               Modul 4 - Python u području Internet stvari (IoT)
TEMA                Vjezba koristenja senzora pomocu Sense HAT Emulatora
NASLOV              Upoznavanje sa Sense HAT Emulatorom
                    Joystick - komandna palica
"""
from sense_emu import SenseHat
import time

sense = SenseHat()

dogadaji = sense.stick.get_events()

while True:
    events = sense.stick.get_events()
    print(events)

while True:
    events = sense.stick.get_events()
    print(events)
    time.sleep(1)

while True:
      for event in sense.stick.get_events():
          print(event.direction, event.action)

while True:
    events = sense.stick.get_events()
    if events:
        for event in events:
            if event.action == 'pressed':
                print('Palica je pomaknuta', end=' ')
                if event.direction == 'up':
                    print('prema gore.')
                elif event.direction == 'down':
                    print('prema dolje.')
                elif event.direction == 'left':
                    print('prema lijevo.')
                elif event.direction == 'right':
                    print('prema desno.')
                elif event.direction == 'middle':
                    print(', NIJE pritisnuta je.')
            elif event.action == 'released':
                print('Palica je otpustena', end=' ')
                if event.direction == 'up':
                    print('prema gore.')
                elif event.direction == 'down':
                    print('prema dolje.')
                elif event.direction == 'left':
                    print('prema lijevo.')
                elif event.direction == 'right':
                    print('prema desno.')
                elif event.direction == 'middle':
                    print(', NIJE otpustena je.')
    else:
        print('Palica miruje')
    
    time.sleep(1)
    sense.clear()


# A mozemo iskoristiti i nas LED ekran pa ispisati pocetno slovo ovisno o smjeru u kojem smo pomjerili palicu
# Ostavit cemo pocetna slova engleskih naziva jer mi imamo Desno i Dolje pa bi nastala zabuna
while True:
  for event in sense.stick.get_events():
    if event.action == "pressed":
      if event.direction == "up":
        sense.show_letter("U")
      elif event.direction == "down":
        sense.show_letter("D")
      elif event.direction == "left": 
        sense.show_letter("L")
      elif event.direction == "right":
        sense.show_letter("R")
      elif event.direction == "middle":
        sense.show_letter("M")
      sleep(1)
      sense.clear()


### ZADATAK ###
# Napravite dvije slike/ikone ljubimca (psa, macke ...) tako da kada se izmjenjuju izgleda kao da se krece
# Koristeci palicu pokrenite animaciju ljubimca. 
# Napravite prvo animaciju tako da se pokrece samo u jednom smjeru i onda ga pokrenite samo kada se palica pomjeri u tom smjeru

p = (204, 0, 204) # Plava
s = (0, 102, 102) # Siva
b = (200, 200, 200) # Bijela
z = (204, 204, 0) # Zuta
pr = (0, 0, 0) # Prazno
ljubimac1 = [
    pr, pr, pr, pr, pr, pr, pr, pr,
    p, pr, pr, pr, pr, pr, pr, pr,
    pr, p, pr, pr, p, pr, p, pr,
    pr, p, s, s, p, b, b, pr,
    pr, s, s, s, b, z, b, z,
    pr, s, s, s, s, b, b, pr,
    pr, s, pr, s, pr, s, pr, pr,
    pr, pr, pr, pr, pr, pr, pr, pr
]
ljubimac2 = [
    pr, pr, pr, pr, pr, pr, pr, pr,
    p, pr, pr, pr, pr, pr, pr, pr,
    pr, p, pr, pr, p, pr, p, pr,
    pr, p, s, s, p, b, b, pr,
    pr, s, s, s, b, z, b, z,
    pr, s, s, s, s, b, b, pr,
    pr, pr, s, pr, s, pr, pr, pr,
    pr, pr, pr, pr, pr, pr, pr, pr
]
sense.clear(0, 0, 0)
x, y, z = sense.get_accelerometer_raw().values()
def setnja():
    for i in range(10):
        sense.set_pixels(ljubimac1)
        time.sleep(0.5)
        sense.set_pixels(ljubimac2)
        time.sleep(0.5)

sense.set_pixels(ljubimac1)

while True:
    events = sense.stick.get_events()
    if events:
        if events[0].direction == 'right':
            setnja()

def crveno():
  sense.clear(255, 0, 0)

def plavo():
  sense.clear(0, 0, 255)

def zeleno():
  sense.clear(0, 255, 0)
  
def zuto():
  sense.clear(255, 255, 0)

# I sada "slusamo" dogadaje i ovisno o dogadaju pozovemo funkciju
sense.stick.direction_up = crveno
sense.stick.direction_down = plavo
sense.stick.direction_left = zeleno
sense.stick.direction_right = zuto
sense.stick.direction_middle = sense.clear

while True:
  pass  # Ovo pokrece program u beskonacno