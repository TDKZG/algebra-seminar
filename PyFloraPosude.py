import tkinter as tk
from Database.database import *

CALIBRI_FONT = "Calibri"


class PyFloraPosude:
    def __init__(self, root):
        self.root = root
        self.create_login_ekran()
    
    def ocisti_root(self):
        for child in self.root.winfo_children():
            child.destroy()
        
    def napravi_glavni_ekran(self):
        
        self.frame_glavni_ekran = tk.Frame(self.root)
        self.frame_glavni_ekran.pack(fill=tk.X, padx=10, pady=10)
        
        lbl_header = tk.Label(self.frame_glavni_ekran, text="PyFloraPosude", font=(
            CALIBRI_FONT, 16), padx=20, pady=20)
        lbl_header.grid(row=0, column=0, sticky="w")
        self.frame_glavni_ekran.grid_columnconfigure(0, weight=1)

        lbl_naslov_sredina = tk.Label(self.frame_glavni_ekran, text="Biljke", font=(
            CALIBRI_FONT, 16), pady=10, padx=10)
        lbl_naslov_sredina.grid(row=0, column=1)
        self.frame_glavni_ekran.grid_columnconfigure(1, weight=1)

        btn_profil = tk.Button(self.frame_glavni_ekran, text="Moj Profil", font=(CALIBRI_FONT, 12), padx=10)
        btn_profil.grid(row=0, column=2)
        self.frame_glavni_ekran.grid_columnconfigure(1, weight=1)













    
    def login(self):
        self.user = db_login(self.username.get(), self.password.get())
        if not self.user: 
            print("Ne postoji korisnik sa tim korisničkim imenom i passwordom")
            return
        print(f"Dobrodošli {self.user.korisnicko_ime}")
        self.ocisti_root()
        self.napravi_glavni_ekran()

    # tk.X označava da želimo da se widget ili okvir proširi i popuni dostupni horizontalni prostor
    def create_login_ekran(self):
        self.frame_login = tk.Frame(self.root)
        self.frame_login.pack(fill=tk.X, padx=10, pady=10)
        
        lbl_header = tk.Label(self.frame_login, text="PyFloraPosude", font=(
            CALIBRI_FONT, 16), padx=20, pady=20)
        lbl_header.pack(anchor="w")
        
        lbl_username = tk.Label(self.frame_login, text="Korisničko ime", font=(CALIBRI_FONT, 12))
        lbl_username.pack(pady=5)

        self.username = tk.StringVar()
        ent_username = tk.Entry(self.frame_login, textvariable=self.username)
        ent_username.pack(pady=5)
        ent_username.focus_set()

        lbl_password = tk.Label(self.frame_login, text="Lozinka", font=(CALIBRI_FONT, 12))
        lbl_password.pack(pady=15)

        self.password = tk.StringVar()
        ent_password = tk.Entry(self.frame_login, textvariable=self.password, show="*")
        ent_password.pack(pady=5)

        btn_login = tk.Button(self.frame_login, text="Prijavi me", command=self.login)
        btn_login.pack(pady=10)

        ent_username.insert(0, "kruno")
        ent_password.insert(0, "123")




root = tk.Tk()
root.geometry("1000x600")
root.title("Py Flora Posude")
flora_posude = PyFloraPosude(root)
root.mainloop()
