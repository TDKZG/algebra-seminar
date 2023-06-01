def kreiraj_naslovni_redak():
    break_line = "_" * 90
    header_top_line = "ID\tTip\t\tProizvodac\tRegistarska\t\tGodina prve\tCijena"
    header_bottom_line = "  \t   \t\t          \toznaka\t\t\tregistracije\t(EUR)"
    return (
        "\n"
        + break_line
        + "\n"
        + header_top_line
        + "\n"
        + header_bottom_line
        + "\n"
        + break_line
        + "\n"
    )


def vrati_ispis_elementa(element):
    if type(element) == str:
        if len(element) > 9:
            return f"{element}\t"
        else:
            return f"{element}\t\t"
    else:
        return f"{element}\t\t"


# Baza je rječnik. Evo primjera s podacima:
vozni_park = {
    1: ["Kamion", "Iveco", "OS 001 ZZ", 2015, 45000.00],
    2: ["Kamion", "Iveco", "OS 002 ZZ", 2015, 47000.00],
    3: ["Tegljač", "MAN", "RI 001 ZZ", 2018, 78000.00],
    4: ["Tegljač", "MAN", "RI 002 ZZ", 2020, 97000.00],
    5: ["Kombi", "Mercedes Benz", "ST 001 ZZ", 2013, 12000.00],
    6: ["Kombi", "Volkswagen", "ST 002 ZZ", 2021, 35000.00],
    7: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", 2010, 9000.00],
    8: ["Dostavno vozilo", "Volkswagen", "ZG 002 ZZ", 2010, 9300.00],
}

# HEADER TABLE ROW
naslovni_redak = kreiraj_naslovni_redak()
print(naslovni_redak)

# BODY TABLE ROWs
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")

    for element in vrijednost:
        ispis_elementa = vrati_ispis_elementa(element)
        print(ispis_elementa, end="")
    print()
print("_" * 90, "\n\n")
