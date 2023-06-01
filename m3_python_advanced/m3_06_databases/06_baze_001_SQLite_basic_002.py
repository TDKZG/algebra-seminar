"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s bazama podataka
NASLOV              Uvod u rad s SQLite
                    Kreiranje tabele unutar baze
"""

import sqlite3

create_table_query = """CREATE TABLE IF NOT EXISTS Employees (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE);"""
database_name = "m03_06_baze_podataka/CompanyDB.db"


try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print("Baza je USPJESNO kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(create_table_query)
    sqliteConnection.commit()
    print("Nova tablica Employees je uspjesno kreirana")
    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspjesno otpusteni")
except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatvorena")
