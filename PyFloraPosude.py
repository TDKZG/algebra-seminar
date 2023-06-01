import tkinter as tk    

from Database.database import *
from Pots.pots import UserPots

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
        if self.korisnik == None:
            print("Ne postoji user s tim usernamom i passwordom")
            return
        print(f"Dobrodosli {self.korisnik.ime}")
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
            self.frame_prijava, text="Korisnicko ime", font=(CALIBRI_FONT, 12)
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
        lbl_header = tk.Label(
            self.frame_header, text="Py Flora Posuda", font=(CALIBRI_FONT, 16)
        )
        lbl_header.pack(side=tk.LEFT, padx=(10, 0), pady=10, expand=True)
        btn_profil = tk.Button(self.frame_header, text="Moj profil", font=(CALIBRI_FONT, 12))
        btn_profil.pack(padx=(0,10), pady=10, ipadx=5, ipady=5, side=tk.RIGHT, expand=True)

        self.frame_srednji_dio = tk.Frame(self.frame_main_screen)
        self.frame_srednji_dio.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


        user_pots = UserPots(self, self.frame_srednji_dio, self.korisnik)




root = tk.Tk()
root.geometry("1200x800")
root.title("My Py Flora Posuda")
smart_home = PyPosude(root)
root.mainloop()