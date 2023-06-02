import tkinter as tk

from Database.database import *
from Pots.pots import UserPots
from Forme.forme import Forme

CALIBRI_FONT = "Calibri"

class PyPosude():
    def __init__(self, root):
        self.root = root
        self.create_login_screen()

    def clear_root(self):
        for child in self.root.winfo_children():
            child.destroy()
    
    def login(self):
        self.korisnik = db_login(self.username.get(), self.password.get())
        if self.korisnik is None:
            print("Ne postoji korisnik s tim korisničkim imenom i lozinkom")
            return
        print(f"Dobrodošli {self.korisnik.ime}")
        self.clear_root()
        self.create_main_screen()

    def create_login_screen(self):
        self.frame_prijava = tk.Frame(self.root)
        self.frame_prijava.pack(fill=tk.X, padx=10, pady=10)

        lbl_header = tk.Label(
            self.frame_prijava, text="Py Flora Posude", font=(CALIBRI_FONT, 20)
        )
        lbl_header.pack()

        lbl_login = tk.Label(self.frame_prijava, text="Prijava", font=(CALIBRI_FONT, 16))
        lbl_login.pack(pady=30)

        lbl_username = tk.Label(
            self.frame_prijava, text="Korisničko ime", font=(CALIBRI_FONT, 12)
        )
        lbl_username.pack(pady=15)

        self.username = tk.StringVar()
        ent_username = tk.Entry(self.frame_prijava, textvariable=self.username)
        ent_username.pack(pady=5)

        lbl_password = tk.Label(
            self.frame_prijava, text="Lozinka", font=(CALIBRI_FONT, 12)
        )
        lbl_password.pack(pady=15)

        self.password = tk.StringVar()
        ent_password = tk.Entry(self.frame_prijava, textvariable=self.password, show="*")
        ent_password.pack(pady=5)

        btn_login = tk.Button(self.frame_prijava, text="Prijava", command=self.login)
        btn_login.pack(pady=10, ipadx=5, ipady=5)

        ent_username.insert(0, "kruno")
        ent_password.insert(0, "123")

  
    def create_main_screen(self):
        self.frame_main_screen = tk.Frame(self.root)
        self.frame_main_screen.pack(fill=tk.BOTH, expand=True)

        self.frame_header = tk.Frame(self.frame_main_screen)
        self.frame_header.pack(fill=tk.X, padx=10, pady=10)
        
        lbl_naslov = tk.Label(
            self.frame_header, text="Py Flora Posude", font=(CALIBRI_FONT, 20)
        )
        lbl_naslov.pack()
        
        self.opis = tk.StringVar()
        self.opis.set("Lista Posuda")
        lbl_header = tk.Label(self.frame_header, textvariable=self.opis, font=(CALIBRI_FONT, 14))
        lbl_header.pack(side=tk.LEFT, padx=0, pady=10)

        btn_profil = tk.Button(self.frame_header, text="Moj profil", font=(CALIBRI_FONT, 12))
        btn_profil.pack(side=tk.RIGHT, padx=10, pady=10, ipadx=5, ipady=5)

        self.frame_srednji_dio = tk.Frame(self.frame_main_screen)
        self.frame_srednji_dio.pack(fill=tk.BOTH, expand=True, padx=10, pady=0)

        self.user_pots = UserPots(self, self.frame_srednji_dio, self.korisnik)

        btn_dodaj_posudu = tk.Button(self.frame_srednji_dio, text="Dodaj novu posudu", anchor="e", command=self.dodaj_posudu)
        btn_dodaj_posudu.pack(side=tk.RIGHT, padx=10, pady=10, ipadx=5, ipady=5)
  
    def dodaj_posudu(self):
        self.opis.set("Upišite i odaberite podatke vezane za posudu")
        self.user_pots.clear_frame_list_pots()
        forma_dodaj_posudu = Forme(self, self.frame_srednji_dio, self.korisnik)
        
    
root = tk.Tk()
root.geometry("1200x800")
root.title("My Py Flora Posuda")
smart_home = PyPosude(root)
root.mainloop()
