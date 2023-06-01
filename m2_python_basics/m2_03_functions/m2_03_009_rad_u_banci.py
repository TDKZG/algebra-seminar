import os
import datetime
import time

racuni = {}

# testni podaci
testni_broj = "BA-2023-02-00001"
testni_podaci = [
    "Tvrtka doo",
    "Ilica 10",
    "10000",
    "Zagreb",
    "11111111111",
    "Pero Peric",
    "HRK",
    1000.0,
]

# dodavanje testnog racuna u rjecnik
# da ne moramo svaki put stvarati novi racun dok testiramo
racuni[testni_broj] = testni_podaci


def generiraj_broj_racuna():
    redni_broj = len(racuni) + 1

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    if month < 10:
        month = str("0" + str(month))
    else:
        month = str(month)

    broj_racuna = "BA-" + str(year) + "-" + month + "-"

    if redni_broj < 10:
        broj_racuna += "0000" + str(redni_broj)
    elif redni_broj < 100:
        broj_racuna += "000" + str(redni_broj)
    elif redni_broj < 1000:
        broj_racuna += "00" + str(redni_broj)
    elif redni_broj < 1000:
        broj_racuna += "0" + str(redni_broj)
    elif redni_broj < 10000:
        broj_racuna += str(redni_broj)
    else:
        print("error")
        exit()

    return broj_racuna


def otvaranje_racuna():
    os.system("cls" if os.name == "nt" else "clear")

    print("*" * 65)
    print("PyBANK ALGEBRA\n".center(65), "\n")
    print("KREIRANJE RACUNA\n".center(65))
    print("Podaci o vlasniku racuna\n".center(65))

    broj_racuna = generiraj_broj_racuna()

    naziv_tvrtke = input("Naziv Tvrtke:\t\t\t\t")
    ulica_i_broj = input("Ulica i broj sjedista Tvrtke:\t\t")
    postanski_broj = input("Postanski broj sjedista Tvrtke:\t\t")
    grad_sjediste = input("Grad u kojem je sjediste Tvrtke:\t")
    while True:
        oib = input("OIB Tvrtke:\t\t\t\t")
        # string.isdigit() vraca Ture ako su sve znamenke u stringu brojke
        if len(oib) != 11 and oib.isdigit():
            print(
                "OIB mora imati tocno 11 znamenki i moraju biti samo brojke.\nMolimo Vas ponovite unos\n"
            )
        else:
            break

    voditelj_tvrtke = input("Ime i prezime odgovorne osobe Tvrtke:\t")
    print()
    valuta = input("Upisite naziv valute racuna (EUR ili HRK):\t")
    if valuta.upper() == "HRK":
        valuta = " hr"
    else:
        valuta = " €"
    vrijednost = 0.0

    input("\nSPREMI? (Pritisnite bilo koju tipku) ")

    podaci_racuna = [
        naziv_tvrtke,
        ulica_i_broj,
        postanski_broj,
        grad_sjediste,
        oib,
        voditelj_tvrtke,
        valuta,
        vrijednost,
    ]
    racuni[broj_racuna] = podaci_racuna

    os.system("cls" if os.name == "nt" else "clear")
    print("*" * 65)
    print("PyBANK ALGEBRA\n".center(65), "\n")
    print("KREIRANJE RACUNA\n".center(65))
    print(f"Podaci o vlasniku racuna tvrtke {naziv_tvrtke}, su uspjesno spremljeni.")
    print(f"Broj racuna je: {broj_racuna}")
    input("Za nastavak pritisnite bilo koju tipku\t")


def prikaz_stanja_racuna():
    os.system("cls" if os.name == "nt" else "clear")
    broj_racuna = input("Upisite broj racuna: ")
    if broj_racuna not in racuni:
        print("Taj broj racuna ne postoji")
    else:
        podaci = racuni[broj_racuna]
        vrijednost = podaci[7]
        valuta = podaci[6]
        print(f"stanje racuna je: {vrijednost}{valuta}")


def prikaz_prometa_po_racunu():
    pass


def polog_novca():
    os.system("cls" if os.name == "nt" else "clear")
    broj_racuna = input("Upisite broj racuna: ")
    if broj_racuna not in racuni:
        print("Taj broj racuna ne postoji")
    else:
        polog = float(input("Upisite koliko zelite uplatiti: "))
        podaci_racuna = racuni[broj_racuna]
        vrijednost = podaci_racuna[7]
        nova_vrijednost = vrijednost + polog
        podaci_racuna[7] = nova_vrijednost
        print(f"Stanje racuna nakon pologa je: {nova_vrijednost}")


def podizanje_novca():
    pass


# izbornik
def izbornik():

    while True:
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")

        print("Dobrodosli u izbornik banke")
        print()
        print("Upisite 1 za kreiranje racuna")
        print("Upisite 2 za prikaz stanja racuna")
        print("Upisite 3 za prikaz prometa po racunu")
        print("Upisite 4 za polog novca")
        print("Upisite 5 za podizanje novca")
        print("Upisite 0 za izlaz")
        print()
        odgovor = int(input("Upisite vas odabir: "))
        if odgovor == 0:
            break
        elif odgovor == 1:
            otvaranje_racuna()
        elif odgovor == 2:
            prikaz_stanja_racuna()
        elif odgovor == 3:
            prikaz_prometa_po_racunu()
        elif odgovor == 4:
            polog_novca()
        elif odgovor == 5:
            podizanje_novca()
        else:
            print("Unijeli ste krivi unos, odaberite jednu od opcija")

    print("Hvala sto ste koristili ovaj program, aj bok")


# glavni program
izbornik()
