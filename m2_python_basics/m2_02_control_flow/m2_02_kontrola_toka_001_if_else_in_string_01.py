"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              STRING - tekstualni tip podataka uz FOR i IF
"""


# tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# lista_rijeci = tekst.split(" ")
# print(lista_rijeci)

tekst = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Vivamus cursus nulla arcu, sollicitudin aliquet dui tempus non. 
    Mauris vitae porttitor erat. Morbi vitae diam et urna volutpat hendrerit. 
    Donec aliquam velit a venenatis bibendum. 
    Nullam orci erat, bibendum in aliquam eget, finibus eu massa. 
    Duis tincidunt turpis eget elementum dapibus. 
    Fusce congue ac elit gravida faucibus. Pellentesque bibendum suscipit ullamcorper. 
    Nulla non nibh elementum, aliquet dui ac, pharetra eros. 
    Quisque vel mollis orci. 
    Nunc porttitor, risus eu sagittis mollis, lorem mauris varius leo, 
    faucibus semper dui dui vel est. 
    Donec rutrum velit vitae ex congue, vitae rhoncus nunc dictum. 
    Suspendisse imperdiet consequat pellentesque. 
    Curabitur condimentum eget enim at auctor. 
    In hac habitasse platea dictumst. Fusce semper id augue non sodales. 
     
    Cras non dui quam. Mauris porttitor mauris sit amet ligula vestibulum 
    sodales egestas vitae ligula. Nam eleifend sed turpis accumsan laoreet. 
    Aliquam vel venenatis nulla, et tristique nunc. 
    Mauris rhoncus tortor interdum nulla sollicitudin convallis. 
    Fusce euismod dui non metus finibus, et vehicula risus egestas. 
    In non fermentum lorem. Proin et magna tellus. 
    Nullam rhoncus luctus lorem, vel rutrum turpis sollicitudin vel. 
    Cras sit amet sapien vel orci pretium finibus consectetur eu enim. 
    Cras eget hendrerit sem. Sed ullamcorper sagittis malesuada. 
    Aenean auctor turpis quis mi egestas malesuada. 
    Praesent ac tortor vel odio lacinia tempus."""


smanjeni_tekst = tekst.lower()
smanjeni_tekst = smanjeni_tekst.replace(",", "")
smanjeni_tekst = smanjeni_tekst.replace(".", "")
# print(smanjeni_tekst)

lista_rijeci = smanjeni_tekst.split(" ")
# print(lista_rijeci)

trazena_rijec = input("Upisite rijec koju zelite pronaci: ").lower()
brojac = 0

for rijec in lista_rijeci:
    if rijec == trazena_rijec:
        brojac += 1

print(f"Rijec {trazena_rijec} se u tekstu ponavlja {brojac} puta")


smanjeni_tekst = tekst.lower()
# koristimo kada zelimo nesto zamjeniti u varijabli
smanjeni_tekst = smanjeni_tekst.replace(",", "")
smanjeni_tekst = smanjeni_tekst.replace(".", "")
# print(smanjeni_tekst)

lista_rijeci = smanjeni_tekst.split(" ")
print(lista_rijeci)

trazena_rijec = input("Upisite rijec koju zelite pronaci: ")
brojac = 0

for rijec in lista_rijeci:
    if rijec == trazena_rijec:
        brojac += 1

print(f"Rijec {trazena_rijec} se u tekstu ponavlja {brojac} puta")


# PALINDROM
rijec = input("Upisite rijec za koju mislite da je PALINDROM: ")

obrnuta_rijec = rijec[::-1]
print(obrnuta_rijec)

if rijec == obrnuta_rijec:
    print(f"Rijec {rijec} JE palindrom")
else:
    print(f"Rijec {rijec} NIJE palindrom")
