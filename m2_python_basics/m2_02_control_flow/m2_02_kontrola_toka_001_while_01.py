"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              UVJETNO IZVRSAVANJE PROGRAMA
                    WHILE petlja
"""


brojevi = []
for broj in range(1, 21):
    brojevi.append(broj)

print(brojevi)

print("FOR petlja")
for broj in brojevi:
    print(broj, end=" ")

print()
print()


print("WHILE petlja")
brojac = 0
while brojac < len(brojevi):
    print(brojevi[brojac], end=" ")
    brojac += 1

print()

print("IF petlja")
if brojac < len(brojevi):
    print(brojevi[brojac], end=" ")
    brojac += 1
print()

while True:
    print("bok")
