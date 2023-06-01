# def sakrij_znakove(tekst, znak_za_maskiranje):
#     zasticeni_tekst = ""
#     if len(tekst) < 5:
#         return "Duljina kartice je prekratka"
#     else:
#         limit_zastite = len(tekst) - 4
#         indeks = 0
#         for znak in tekst:
#             if indeks < limit_zastite:
#                 zasticeni_tekst += znak_za_maskiranje
#             else:
#                 zasticeni_tekst += znak
#             indeks += 1
#         return zasticeni_tekst


# kartica = input("Upisite broj vase kreditne kartice: ")
# znak_za_maskiranje = input("Upisite s kojim znakom zelite maskirati: ")
# tekst = sakrij_znakove(kartica, znak_za_maskiranje)
# print(kartica)
# print(tekst)


def maskiranje_kartice(kartica, maska):
    zamjenski_string = maska * (len(kartica) - 4)
    return zamjenski_string + kartica[-4:]


print(maskiranje_kartice("134245657854", "#"))
