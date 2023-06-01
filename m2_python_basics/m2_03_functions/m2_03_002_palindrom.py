# def provjera_palindrom(rijec):
#     smanjena_rijec = rijec.lower()
#     if smanjena_rijec == smanjena_rijec[::-1]:
#         return True
#     else:
#         return False


def provjera_palindrom(rijec):
    smanjena_rijec = rijec.lower()
    return smanjena_rijec == smanjena_rijec[::-1]


while True:
    rijec = input("Upisi rijec koju zelis provjeriti: ")
    rezultat = provjera_palindrom(rijec)
    if rezultat:
        print("Je palindrom")
    else:
        print("Nije palindrom")



