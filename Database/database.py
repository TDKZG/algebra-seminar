from sqlalchemy import (Column, Integer, Float, String,
                        Boolean, DateTime, ForeignKey, create_engine)

from sqlalchemy.orm import Session, relationship, declarative_base
from datetime import datetime

from datetime import datetime

Base = declarative_base()

class Korisnik(Base):
    __tablename__ = "korisnici"

    id = Column(Integer, primary_key=True)
    ime = Column(String)
    prezime = Column(String)
    korisnicko_ime = Column(String, unique=True)
    lozinka = Column(String)

    posude = relationship("Posuda", backref="korisnik")

class Biljka(Base):
    __tablename__ = "biljke"

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    slika_path = Column(String)
    njega_vlaga = Column(String)
    njega_osvjetljenje = Column(String)
    njega_temperatura = Column(String)
    supstrat_preporuka = Column(String)

    posude = relationship("Posuda", backref="biljka")

class Posuda(Base):
    __tablename__ = "posude"

    id = Column(Integer, primary_key=True)
    lokacija = Column(String)
    je_prazna = Column(Boolean, default=True)
    biljka_id = Column(Integer, ForeignKey("biljke.id"))
    korisnik_id = Column(Integer, ForeignKey("korisnici.id"))

    mjerenja = relationship("Mjerenja", backref="posuda")

class Mjerenja(Base):
    __tablename__ = "mjerenja"

    id = Column(Integer, primary_key=True)
    ts_mjerenja = Column(DateTime, default=datetime.now())
    vlaznost_zemlje = Column(Float)
    ph_vrijednost = Column(Float)
    razine_svjetla = Column(Float)
    temp_zraka = Column(Float)
    posuda_id = Column(Integer, ForeignKey("posude.id"))


db_engine = create_engine("sqlite:///PyFloraPosude.db")
Base.metadata.create_all(bind=db_engine)


def db_login(korisnicko_ime, lozinka):
    with Session(db_engine) as session:
        korisnik = (session.query(Korisnik).filter(
            Korisnik.korisnicko_ime == korisnicko_ime, Korisnik.lozinka == lozinka).one_or_none())
        return korisnik
