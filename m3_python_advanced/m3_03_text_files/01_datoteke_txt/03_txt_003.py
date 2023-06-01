"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s datotekama
NASLOV              Uvod u rad s tekstualnim datotekama
                    Citanje liniju po liniju
"""


# try:
#     with open(
#         "m3_03_tekstualne_datoteke/01_datoteke_txt/adresar.txt", "r"
#     ) as file_reader:
#         file_data = file_reader.read()
#         print(file_data)
# except Exception as e:
#     print(f"Dogodila se pogreska {e}")


# try:
#     with open(
#         "m3_03_tekstualne_datoteke/01_datoteke_txt/adresar.txt", "r"
#     ) as file_reader:
#         for row in file_reader:
#             row_parts = row.rstrip().split(";")
#             print(
#                 f"ID: {row_parts[0]}\tIme: {row_parts[1]}\tPrezime: {row_parts[2]}\tTelefon: {row_parts[3]}"
#             )

# except Exception as e:
#     print(f"Dogodila se pogreska {e}")


class Contact:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def print_contact(self):
        print(
            f"ID: {self.id}\tIme: {self.first_name}\tPrezime: {self.last_name}\tTelefon: {self.phone}"
        )


address_book = {}

try:
    with open(
        "m3_03_tekstualne_datoteke/01_datoteke_txt/adresar.txt", "r"
    ) as file_reader:
        for row in file_reader:
            row = row.rstrip()  # maknemo \n s kraja
            row_parts = row.split(";")
            contact = Contact(row_parts[0], row_parts[1], row_parts[2], row_parts[3])
            address_book[row_parts[0]] = contact
            # address_book[contact.id] = contact

except Exception as e:
    print(f"Dogodila se pogreska {e}")


for key, value in address_book.items():
    print(key, end="\t")
    value.print_contact()
