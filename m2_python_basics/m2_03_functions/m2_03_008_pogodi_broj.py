import random

zamisljeni_broj = random.randint(1, 100)
broj_pokusaja = 0

while True:
    odgovor = int(input("Pogodi broj od 1 do 100 koji sam zamislio.\t"))
    broj_pokusaja += 1

    if odgovor == zamisljeni_broj:
        print("Cestitam! To je broj koji sam zamislio")
        print(f"Za pogoditi ti je trebalo {broj_pokusaja} pokusaja")
        print()
        break
    elif odgovor < zamisljeni_broj:
        print(f"Zamisljeni broj je veci od {odgovor}")
    elif odgovor > zamisljeni_broj:
        print(f"Zamisljeni broje je manji od {odgovor}")
