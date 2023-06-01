"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Rad s bazama podataka
NASLOV              SQLite ORM i SQLAlchemy
                    Rad s bazama podataka bez SQL jezika
                    Bookshop
"""

import sqlalchemy as db
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# MODELI

autor_izdavac = db.Table(
    "autor_izdavac",
    Base.metadata,
    db.Column("autor_id", db.Integer, db.ForeignKey("autor.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id")),
)

knjiga_izdavac = db.Table(
    "knjiga_izdavac",
    Base.metadata,
    db.Column("knjiga_id", db.Integer, db.ForeignKey("knjiga.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id")),
)


class Autor(Base):
    __tablename__ = "autor"
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String)
    prezime = db.Column(db.String)
    knjige = relationship("Knjiga", backref=backref("autor"))
    izdavaci = relationship("Izdavac", secondary=autor_izdavac, back_populates="autori")


class Knjiga(Base):
    __tablename__ = "knjiga"
    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"))
    naslov = db.Column(db.String)
    izdavaci = relationship(
        "Izdavac", secondary=knjiga_izdavac, back_populates="knjige"
    )


class Izdavac(Base):
    __tablename__ = "izdavac"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String)
    autori = relationship("Autor", secondary=autor_izdavac, back_populates="izdavaci")
    knjige = relationship("Knjiga", secondary=knjiga_izdavac, back_populates="izdavaci")


# CRUD operacije


def get_knjige_po_izdavacu(session):
    """Dohvati listu izdavaca s brojem knjiga koje su izdali."""

    return (
        session.query(
            Izdavac.naziv, db.func.count(Knjiga.naslov).label("ukupno_knjiga")
        )
        .join(Izdavac.knjige)
        .group_by(Izdavac.naziv)
        .order_by(db.desc("ukupno_knjiga"))
    )


# DZ
# TODO
# def get_autore_po_izdavacu(session)
# Dohvati listu izdavaca te broj autora cije knjige su izdali


def get_autore_po_izdavacu(session):
    """Dohvati listu izdavaca te broj autora cije knjige su izdali"""
    return (
        session.query(
            Izdavac.naziv,
            db.func.count(Autor.ime).label("ukupno_autora"),
        )
        .join(Izdavac.autori)
        .group_by(Izdavac.naziv)
        .order_by(db.desc("ukupno_autora"))
    )


def get_autori(session):
    """Dohvati listu autora sortiranih po prezimenu"""
    return session.query(Autor).order_by(Autor.prezime).all()


def add_knjiga(session, ime_autora, prezime_autora, naslov_knjige, naziv_izdavaca):
    """
    Dodaje novu knjigu u bazi ako vec ne postoji,
    takodjer dodaje i autora i izdavaca ako ne postoje.
    """
    knjiga = (
        session.query(Knjiga).join(Autor)
        # filtriraj po naslovu knjige
        .filter(Knjiga.naslov == naslov_knjige)
        # filtriraj po imenu AND prezimenu autora
        .filter(db.and_(Autor.ime == ime_autora, Autor.prezime == prezime_autora))
        # filtriraj po nazivu izdavaca
        .filter(Knjiga.izdavaci.any(Izdavac.naziv == naziv_izdavaca))
        # dohvati prvu koja zadovoljava ili ako nema vrati None
        .one_or_none()
    )
    if knjiga is not None:
        return

    # kreiraj novi objekt knjiga
    knjiga = Knjiga(naslov=naslov_knjige)

    autor = (
        session.query(Autor)
        .filter(db.and_(Autor.ime == ime_autora, Autor.prezime == prezime_autora))
        .one_or_none()
    )
    # ako nema takvog autora, stvorimo ga
    if autor is None:
        autor = Autor(ime=ime_autora, prezime=prezime_autora)

    izdavac = (
        session.query(Izdavac).filter(Izdavac.naziv == naziv_izdavaca).one_or_none()
    )
    # ako nema takvog izdavaca, stvorimo ga
    if izdavac is None:
        izdavac = Izdavac(naziv=naziv_izdavaca)
        session.add(izdavac)

    # podesimo relacije izmedu knige i autora i izdavaca
    knjiga.autor = autor

    # ***************************************************
    # ovaj dio je falio, nije se nikad dodao novi izdavac u
    # listu izdavaci u klasi autor
    autor.izdavaci.append(izdavac)
    # prebacio sam i ovaj session.add(autor) odozgo ovdje
    session.add(autor)
    # ***************************************************

    knjiga.izdavaci.append(izdavac)
    session.add(knjiga)

    # napokon pohranimo knjigu te eventualno nove objekte autora i izdavaca u bazu
    session.commit()


def main():
    db_engine = db.create_engine("sqlite:///m3_06_baze_podataka/BookshopDB.db")
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    print()
    knjige_po_izdavacu = get_knjige_po_izdavacu(session)
    for row in knjige_po_izdavacu:
        print(f"Izdavac {row.naziv}, ukupno knjiga: {row.ukupno_knjiga}")
    print()

    # DZ
    # TODO
    # dohvati broj autora po svakom izdavacu
    autori_po_izdavacu = get_autore_po_izdavacu(session)
    # print("autori_po_izdavacu", autori_po_izdavacu)
    for row in autori_po_izdavacu:
        print(f"Izdavac: {row.naziv}, ukupno autora: {row.ukupno_autora}")
    print()

    add_knjiga(
        session,
        ime_autora="Stephen",
        prezime_autora="King",
        naslov_knjige="The Stand",
        naziv_izdavaca="Random House",
    )

    nove_knjige = [
        ["Isaac", "Asimov", "Foundation", "Random House"],
        ["Pearl", "Buck", "The Good Earth", "Random House"],
        ["Pearl", "Buck", "The Good Earth", "Simon & Schuster"],
        ["Tom", "Clancy", "The Hunt For Red October", "Berkley"],
        ["Tom", "Clancy", "Patriot Games", "Simon & Schuster"],
        ["Stephen", "King", "It", "Random House"],
        ["Stephen", "King", "It", "Penguin Random House"],
        ["Stephen", "King", "Dead Zone", "Random House"],
        ["Stephen", "King", "The Shining", "Penguin Random House"],
        [
            "John",
            "Le Carre",
            "Tinker, Tailor, Soldier, Spy: A George Smiley Novel",
            "Berkley",
        ],
        ["Alex", "Michaelides", "The Silent Patient", "Simon & Schuster"],
        ["Carol", "Shaben", "Into The Abyss", "Simon & Schuster"],
    ]

    for knjiga in nove_knjige:
        add_knjiga(
            session,
            ime_autora=knjiga[0],
            prezime_autora=knjiga[1],
            naslov_knjige=knjiga[2],
            naziv_izdavaca=knjiga[3],
        )

    autori = get_autori(session)
    for autor in autori:
        print(f"Autor: {autor.ime} {autor.prezime}")


# glavni program
main()
