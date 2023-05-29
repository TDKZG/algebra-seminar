from sqlalchemy.orm import Session
from database import *


def populate_database():
    with Session(bind=db_engine) as session:
        korisnik = Korisnik(ime="Kruno", prezime="Dretar", korisnicko_ime = "kruno", lozinka = "123")
        session.add(korisnik)

        session.commit()



if __name__ == "__main__":
    populate_database()