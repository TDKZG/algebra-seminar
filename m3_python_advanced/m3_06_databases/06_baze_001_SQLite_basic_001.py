"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s bazama podataka
NASLOV              Uvod u rad s SQLite
"""


import sqlite3

select_query = "SELECT sqlite_version();"

try:
    sqliteConnection = sqlite3.connect("m03_06_baze_podataka/SQLite_Python.db")
    cursor = sqliteConnection.cursor()
    print("Baza je USPJESNO kreirana te je aplikacija spojena na SQLite!")
    cursor.execute(select_query)
    records = cursor.fetchall()
    print("SQLita verzija je:", records)
    cursor.close()
    print("Resursi SQLite CURSOR objekta su uspjesno otpusteni")

except sqlite3.Error as error:
    print("Dogodila se greska prilikom pokusaja spajanja na SQLite:", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite konekcija je uspjesno zatvorena")
