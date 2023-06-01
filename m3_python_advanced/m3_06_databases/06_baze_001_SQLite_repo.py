"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s bazama podataka
NASLOV              Uvod u rad s SQLite
                    Repozitorij metoda za rad s bazom podataka
"""

import sqlite3


def create_connection(db_file):
    """
    Kreira konekciju prema SQLite bazi podataka
    Ako baza ne postoji, kreirat ce novu
    :param db_file: Putanja do SQLite datoteke
    :return: Sqlite db connection objekt
    """

    db_connection = None

    try:
        db_connection = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        print(error)
    return db_connection


def create_table(db_connection, create_table_sql):
    """
    Kreira tablicu definiranu u create_table_sql parametru
    :param db_connection: SQLite db connection objekt
    :param create_table_sql: Tekstualna varijabla s CREATE TABLE upitom
    :return:
    """
    try:
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as error:
        print(error)


def create_employee(db_connection, djelatnik):
    """
    Kreira novi red u tabeli Employees na osnovu podataka
    pohranjenih u djelatnik parametru tipa tuple.
    :param db_connection: SQLite db connection objekt
    :param djelatnik: Tuple s podacima o djelatniku
    :return: id novog retka s podacima o djelatniku
    """
    sql_query = """INSERT INTO Employees (name, email)
                    VALUES (?, ?)"""
    cursor = db_connection.cursor()
    cursor.execute(sql_query, djelatnik)
    db_connection.commit()
    return cursor.lastrowid


def update_employee(db_connection, djelatnik):
    """
    Azurira podtke o Djelatniku
    :param db_connection: SQLite db connection objekt
    :param djelatnik: Tuple s podacima o djelatniku
    :return: None
    """


def delete_employee(db_connection, id):
    """
    Brise zapis o djelatniku u tabeli na osnovu ID broja retka
    :param db_connection: SQLite db connection objekt
    :param id: id retka djelatnika
    :return: None
    """


def delete_all_employees(db_connection):
    """
    Brise sve zapise o djelatnicima iz tabele
    :param db_connection: SQLite db connection objekt
    :return: None
    """


def select_all_employees(db_connection):
    """
    Dohvaca sve zapise o djelatnicima
    :param db_connection: SQLite db connection objekt
    :return: print redak
    """


def select_employees_by_id(db_connection, id):
    """
    Dohvaca zapise o djelatniku na osnovu ID broja
    :param db_connection: SQLite db connection objekt
    :param id: id retka djelatnika
    :return: print redak
    """
