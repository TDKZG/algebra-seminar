# class PrvaKlasa:
#     """
#     Docstring koji pojasnjava za sto sluzi ova klasa
#     """

#     pass


# objekt1 = PrvaKlasa()
# objekt2 = PrvaKlasa()


# class Televizor:
#     dijagonala = 55
#     sirina = 124
#     visina = 79
#     proizvodac = "Grundig"
#     model = "Ultra Smart Turbo Extra"
#     je_ukljucen = False

#     def ukljuci(self):
#         self.je_ukljucen = True


# tv_dnevni_boravak = Televizor()
# tv_kuhinja = Televizor()

# print(f"Proivodac: {tv_dnevni_boravak.proizvodac}")
# print(f"Sirina: {tv_dnevni_boravak.sirina}, visina: {tv_dnevni_boravak.visina}")

# print("Status oba televizora")
# if tv_dnevni_boravak.je_ukljucen:
#     print(f"Status: Tv u dnevnom boravku JE ukljucen")
# else:
#     print(f"Status: Tv u dnevnom boravku NIJE ukljucen")
# if tv_kuhinja.je_ukljucen:
#     print(f"Status: Tv u kuhinji JE ukljucen")
# else:
#     print(f"Status: Tv u kuhinji NIJE ukljucen")

# print("\nUkljuci tv u kuhinji")
# tv_kuhinja.ukljuci()

# print("Status oba televizora")
# if tv_dnevni_boravak.je_ukljucen:
#     print(f"Status: Tv u dnevnom boravku JE ukljucen")
# else:
#     print(f"Status: Tv u dnevnom boravku NIJE ukljucen")
# if tv_kuhinja.je_ukljucen:
#     print(f"Status: Tv u kuhinji JE ukljucen")
# else:
#     print(f"Status: Tv u kuhinji NIJE ukljucen")


class Televizor:
    def __init__(
        self,
        dijagonala,
        sirina,
        visina,
        proizvodac,
        model,
        je_ukljucen=False,
        program=0,
        glasnoca=0,
    ):
        self.dijagonala = dijagonala
        self.sirina = sirina
        self.visina = visina
        self.proizvodac = proizvodac
        self.model = model
        self.je_ukljucen = je_ukljucen
        self.program = program
        self.glasnoca = glasnoca

    def ukljuci(self):
        self.je_ukljucen = True
        self.program = 1
        self.glasnoca = 10

    def promijeni_program(self, novi_program):
        self.program = novi_program

    def podesi_glasnocu(self, akcija):
        if akcija == "glasnije":
            self.glasnoca += 1
        elif akcija == "tise":
            self.glasnoca -= 1
        elif akcija == "prigusi":
            self.glasnoca = 0


novi_tv_dnevni_boravak = Televizor(105, 250, 180, "Sony", "Bravia")

print(
    f"Status tv-a: {novi_tv_dnevni_boravak.je_ukljucen}, program: {novi_tv_dnevni_boravak.program}, glasnoca: {novi_tv_dnevni_boravak.glasnoca}"
)
novi_tv_dnevni_boravak.ukljuci()
print(
    f"Status tv-a: {novi_tv_dnevni_boravak.je_ukljucen}, program: {novi_tv_dnevni_boravak.program}, glasnoca: {novi_tv_dnevni_boravak.glasnoca}"
)

novi_tv_dnevni_boravak.promijeni_program(3)

print(
    f"Status tv-a: {novi_tv_dnevni_boravak.je_ukljucen}, program: {novi_tv_dnevni_boravak.program}, glasnoca: {novi_tv_dnevni_boravak.glasnoca}"
)

novi_tv_dnevni_boravak.podesi_glasnocu("glasnije")

print(
    f"Status tv-a: {novi_tv_dnevni_boravak.je_ukljucen}, program: {novi_tv_dnevni_boravak.program}, glasnoca: {novi_tv_dnevni_boravak.glasnoca}"
)

novi_tv_dnevni_boravak.podesi_glasnocu("prigusi")


print(
    f"Status tv-a: {novi_tv_dnevni_boravak.je_ukljucen}, program: {novi_tv_dnevni_boravak.program}, glasnoca: {novi_tv_dnevni_boravak.glasnoca}"
)
