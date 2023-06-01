from sqlalchemy.orm import Session
from database import *


def populate_db():
    with Session(bind=db_engine) as session:

        korisnik = Korisnik(korisnicko_ime="kruno",
                            lozinka="123",
                            ime="Krunoslav",
                            prezime="Dretar")
        session.add(korisnik)

        biljke = {"naziv":["Ruža", "Tulipan", "Agava", "Maslina", "Jagoda"],
                  "ucestalost_zalijevanja": [3,6,15, 25, 20],
                  "preferirana_osvjetljenost" : [35, 25, 55, 53, 68],
                  "preferirana_temperatura": [18,18,22,20,25],
                  "preporuka_za_supstrat" : ["uneverzalni","univerzalni","za sukulente", "za acedofilne potrebe", "univerzalni"]}
        


        for i in range(5):
            biljka = Biljka(naziv= biljke["naziv"][i],
                            ucestalost_zalijevanja= biljke["ucestalost_zalijevanja"][i],
                            preferirana_osvjetljenost= biljke["preferirana_osvjetljenost"][i],
                            preferirana_temperatura= biljke["preferirana_temperatura"][i],
                            preporuka_za_supstrat= biljke["preporuka_za_supstrat"][i])
            session.add(biljka)
        
            session.commit()
            print(biljka)





def populate_db2():
    with Session(bind=db_engine) as session:

        # Pre-existing user and plant data
        korisnik = Korisnik(korisnicko_ime="kruno",
                            lozinka="123",
                            ime="Krunoslav",
                            prezime="Dretar")
        session.add(korisnik)

        biljke = {"naziv":["Ruža", "Tulipan", "Agava", "Maslina", "Jagoda"],
                  "ucestalost_zalijevanja": [3,6,15, 25, 20],
                  "preferirana_osvjetljenost" : [35, 25, 55, 53, 68],
                  "preferirana_temperatura": [18,18,22,20,25],
                  "preporuka_za_supstrat" : ["uneverzalni","univerzalni","za sukulente", "za acedofilne potrebe", "univerzalni"]}
        
        biljka_objects = []
        for i in range(5):
            biljka = Biljka(naziv= biljke["naziv"][i],
                            ucestalost_zalijevanja= biljke["ucestalost_zalijevanja"][i],
                            preferirana_osvjetljenost= biljke["preferirana_osvjetljenost"][i],
                            preferirana_temperatura= biljke["preferirana_temperatura"][i],
                            preporuka_za_supstrat= biljke["preporuka_za_supstrat"][i])
            biljka_objects.append(biljka)
            session.add(biljka)
        
        # New pot data
        lokacije = ["Kuhinja", "Dnevni boravak", "Spavaća soba", "Kupaonica", "Balkon"]

        for i in range(5):
            posuda = Posuda(naziv_lokacije=lokacije[i],
                            korisnik_id=korisnik.id,
                            biljka_id=biljka_objects[i].id,
                            korisnik=korisnik,
                            biljka=biljka_objects[i])
            session.add(posuda)
        
        session.commit()

        print(f'Korisnik: {korisnik}')
        print('Biljke:')
        for biljka in biljka_objects:
            print(biljka)
        print('Posude:')
        for posuda in korisnik.posude:
            print(posuda)


            
if __name__ == "__main__":
    populate_db2()
