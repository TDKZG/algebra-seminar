"""
MODUL               Modul 4 - Python u području Internet stvari (IoT)
TEMA                Vjezba koristenja senzora pomocu Sense HAT Emulatora
NASLOV              Upoznavanje sa Sense HAT Emulatorom
                    Temperatura, tlak i vlaga zraka
"""


from sense_emu import SenseHat

sense = SenseHat()

temperature = sense.get_temperature()
print(temperature)

temperature_from_humidity = sense.get_temperature_from_humidity()
temperature_from_pressure = sense.get_temperature_from_pressure()

print(temperature_from_humidity)
print(temperature_from_pressure)

tlak = sense.get_pressure()
print(tlak)

vlaznost = sense.get_humidity()
print(vlaznost)

temperature = sense.get_temperature()
temperature = round(temperature, 1)
print(temperature)
tlak = round(sense.get_pressure(), 1)
print(tlak)
vlaznost = round(sense.get_humidity(), 1)
print(vlaznost)


mjerenje =f'Temperatura: {temperature}; Tlak: {tlak}; Vlaznost: {vlaznost}'
sense.show_message(mjerenje)
