"""
MODUL               Modul 4 - Python u području Internet stvari (IoT)
TEMA                Vjezba koristenja senzora pomocu Sense HAT Emulatora
NASLOV              Upoznavanje sa Sense HAT Emulatorom
                    Ziroskop - orjentacija
"""


# Na Sense HAT Simulatoru imate dio naziva Orientation. 
# Tu imate vrijednosti kuteva zakreta oko x, y i z osi
    # x = Roll
    # y = Pitch
    # z = Yaw

from sense_emu import SenseHat

sense = SenseHat()

ziroskop = sense.get_orientation()
roll, pitch, yaw = ziroskop.values()
roll, pitch, yaw = sense.get_orientation().values()

roll = round(roll, 2)
pitch = round(pitch, 2)
yaw = round(yaw, 2)

accelerometer = sense.get_accelerometer_raw().values()
sense.show_letter('P')
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)
