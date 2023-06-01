"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s bazama podataka
NASLOV              Uvod u rad s SQLite
                    Citanje, dohvat pojedinacnog podataka iz tabele
"""

import sqlite3

database_name = "m03_06_baze_podataka/CompanyDB.db"

select_query = "SELECT * FROM Employees WHERE id=?"

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print("Baza je USPJESNO kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(select_query, (3,))
    records = cursor.fetchall()

    for record in records:
        print(record)

    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspjesno otpusteni")

except sqlite3.Error as error:
    print("Dogodila se greska prilikom pokusaja spajanja na SQLite:", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatvorena")
