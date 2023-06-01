"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s bazama podataka
NASLOV              Uvod u rad s SQLite
                    Dodavanje podataka u tablicu
"""


import sqlite3

database_name = "m03_06_baze_podataka/CompanyDB.db"

insert_into_table_query = """   INSERT INTO Employees (name, email)
                                VALUES (?, ?)"""

lista_djelatnika = [
    ("Petar Peric", "pperic@gmail.com"),
    ("Ana Anic", "aanica@gmail.com"),
    ("Kresimir Horvat", "khorvat@gmail.com"),
]

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()

    for djelatnik in lista_djelatnika:
        cursor.execute(insert_into_table_query, djelatnik)

    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatvorena")
