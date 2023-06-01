"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s bazama podataka
NASLOV              Uvod u rad s SQLite
                    Azuriranje podataka u tablici
"""

import sqlite3

database_name = "m03_06_baze_podataka/CompanyDB.db"

update_table_query = """UPDATE Employees
                            SET name = ?,
                                email = ?
                            WHERE id = ?"""

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print("Baza je USPJESNO kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(update_table_query, ("Ana Anic Horvat", "aahorvat@gmail.com", 2))
    sqliteConnection.commit()
    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspjesno otpusteni")

except sqlite3.Error as error:
    print("Dogodila se greska prilikom pokusaja spajanja na SQLite:", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatvorena")
