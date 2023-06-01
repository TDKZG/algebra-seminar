import os

"""
    Import os modula je nužan ako želimo postići da se 
"""

polje_na_ploci = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def Status_Igre():
    if (
        polje_na_ploci[1] == polje_na_ploci[2]
        and polje_na_ploci[2] == polje_na_ploci[3]
    ):
        return 1
    elif (
        polje_na_ploci[4] == polje_na_ploci[5]
        and polje_na_ploci[5] == polje_na_ploci[6]
    ):
        return 1
    elif (
        polje_na_ploci[7] == polje_na_ploci[8]
        and polje_na_ploci[8] == polje_na_ploci[9]
    ):
        return 1
    elif (
        polje_na_ploci[1] == polje_na_ploci[4]
        and polje_na_ploci[4] == polje_na_ploci[7]
    ):
        return 1
    elif (
        polje_na_ploci[2] == polje_na_ploci[5]
        and polje_na_ploci[5] == polje_na_ploci[8]
    ):
        return 1
    elif (
        polje_na_ploci[3] == polje_na_ploci[6]
        and polje_na_ploci[6] == polje_na_ploci[9]
    ):
        return 1
    elif (
        polje_na_ploci[1] == polje_na_ploci[5]
        and polje_na_ploci[5] == polje_na_ploci[9]
    ):
        return 1
    elif (
        polje_na_ploci[3] == polje_na_ploci[5]
        and polje_na_ploci[5] == polje_na_ploci[7]
    ):
        return 1
    elif (
        polje_na_ploci[1] != 1
        and polje_na_ploci[2] != 2
        and polje_na_ploci[3] != 3
        and polje_na_ploci[4] != 4
        and polje_na_ploci[5] != 5
        and polje_na_ploci[6] != 6
        and polje_na_ploci[7] != 7
        and polje_na_ploci[8] != 8
        and polje_na_ploci[9] != 9
    ):
        return 0
    else:
        return -1


def Iscrtaj_Plocu():
    os.system("cls" if os.name == "nt" else "clear")

    print("\n\n\t  VUA ALGEBRA")
    print("\n\tKrizic Kruzic\n\n")

    print("IGRAC 1 (X)  -  IGRAC 2 (O)")
    print()

    print("\t     |     |     ")
    print("\t ", polje_na_ploci[1], " | ", polje_na_ploci[2], " |  ", polje_na_ploci[3])

    print("\t_____|_____|_____")
    print("\t     |     |     ")

    print("\t ", polje_na_ploci[4], " | ", polje_na_ploci[5], " |  ", polje_na_ploci[6])

    print("\t_____|_____|_____")
    print("\t     |     |     ")

    print("\t ", polje_na_ploci[7], " | ", polje_na_ploci[8], " |  ", polje_na_ploci[9])

    print("\t     |     |     ")


igrac = 1
status_igre = -1

while status_igre == -1:
    Iscrtaj_Plocu()

    if igrac % 2 == 1:
        igrac = 1
    else:
        igrac = 2

    print("\n\nIgrac", igrac)
    izabrano_polje = int(input("Unesite broj polja na ploci:"))

    # PROVJERA IGRE
    if igrac == 1:
        oznaka_igraca = "X"
    else:
        oznaka_igraca = "O"

    if izabrano_polje == 1 and polje_na_ploci[1] == 1:
        polje_na_ploci[1] = oznaka_igraca
    elif izabrano_polje == 2 and polje_na_ploci[2] == 2:
        polje_na_ploci[2] = oznaka_igraca
    elif izabrano_polje == 3 and polje_na_ploci[3] == 3:
        polje_na_ploci[3] = oznaka_igraca
    elif izabrano_polje == 4 and polje_na_ploci[4] == 4:
        polje_na_ploci[4] = oznaka_igraca
    elif izabrano_polje == 5 and polje_na_ploci[5] == 5:
        polje_na_ploci[5] = oznaka_igraca
    elif izabrano_polje == 6 and polje_na_ploci[6] == 6:
        polje_na_ploci[6] = oznaka_igraca
    elif izabrano_polje == 7 and polje_na_ploci[7] == 7:
        polje_na_ploci[7] = oznaka_igraca
    elif izabrano_polje == 8 and polje_na_ploci[8] == 8:
        polje_na_ploci[8] = oznaka_igraca
    elif izabrano_polje == 9 and polje_na_ploci[9] == 9:
        polje_na_ploci[9] = oznaka_igraca
    else:
        print("Pogresan potez ")
        igrac -= 1

    status_igre = Status_Igre()
    igrac += 1

Iscrtaj_Plocu()
print("\n\nREZULTAT\n")
if status_igre == 1:
    print("Igrac", igrac - 1, "je pobijedio!\n\n")
else:
    print("Nerijeseno\n\n")
