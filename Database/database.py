# Database/database.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, Session, joinedload
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Korisnik(Base):
    __tablename__ = 'korisnici'

    id = Column(Integer, primary_key=True)
    korisnicko_ime = Column(String)
    lozinka = Column(String)
    ime = Column(String)
    prezime = Column(String)
    posude = relationship("Posuda", back_populates='korisnik')


class Biljka(Base):
    __tablename__ = 'biljke'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    ucestalost_zalijevanja = Column(Float)
    preferirana_osvjetljenost = Column(Float)
    preferirana_temperatura = Column(Float)
    preporuka_za_supstrat = Column(String)
    posude = relationship("Posuda", back_populates='biljka')


    def __repr__(self) -> str:
        return f"id={self.id}, ime={self.naziv}"


class Posuda(Base):
    __tablename__ = 'posude'

    id = Column(Integer, primary_key=True)
    naziv_lokacije = Column(String)  # Na primjer: "Kuhinja - polica pored prozora."
    korisnik_id = Column(Integer, ForeignKey('korisnici.id'))
    biljka_id = Column(Integer, ForeignKey('biljke.id'))
    korisnik = relationship("Korisnik", back_populates='posude')
    biljka = relationship("Biljka", back_populates='posude')
    mjerenja = relationship("Mjerenje", back_populates='posuda')
    
    def __repr__(self) -> str:
        return f"(id={self.id}, ime={self.naziv_lokacije})"

class Mjerenje(Base):
    __tablename__ = 'mjerenja'

    id = Column(Integer, primary_key=True)
    vremenska_oznaka = Column(DateTime)
    vlaznost_zemlje = Column(Float)
    ph_vrijednost = Column(Float)
    razina_osvjetljenja = Column(Float)
    temperatura_zraka = Column(Float)
    posuda_id = Column(Integer, ForeignKey('posude.id'))
    posuda = relationship("Posuda", back_populates='mjerenja')


db_engine = create_engine("sqlite:///PyPosude.db")
Base.metadata.create_all(bind=db_engine)



def db_login(korisnicko_ime, lozinka):
    with Session(db_engine) as session:
        korisnik = (
            session.query(Korisnik)
            .filter(Korisnik.korisnicko_ime == korisnicko_ime, Korisnik.lozinka == lozinka)
            .one_or_none()
        )
        return korisnik

def db_user_pots(korisnik):
    with Session(db_engine) as session:
        user_pots = session.query(Posuda).filter(Posuda.korisnik_id == korisnik.id).options(joinedload(Posuda.biljka)).all()
        return user_pots