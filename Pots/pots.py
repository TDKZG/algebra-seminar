import tkinter as tk

from Database.database import *

CALIBRI_FONT = "Calibri"

class UserPots:
    def __init__(self, py_posude, parent_frame, logged_user):
        self.py_posude = py_posude
        self.parent_frame = parent_frame
        self.logged_user = logged_user
        self.create_gui()
    
    def create_gui(self):
        #self.frame_settings = tk.Frame(self.parent_frame)
        self.list_user_pots()
    



    def list_user_pots(self):

        self.user_pots = db_user_pots(self.logged_user)
        #print("self.user_pots:",self.user_pots)
        self.frame_list_pots = tk.Frame(self.parent_frame)
        self.frame_list_pots.pack(padx=10, pady=10, fill=tk.Y, side=tk.LEFT)

        pots_info = []

        for i, pot in enumerate(self.user_pots):
            naziv = f"Biljka: {pot.biljka.naziv}".ljust(25)
            if i==0:
                naziv = f"Biljka: {pot.biljka.naziv}".ljust(27) # ne pitaj zasto
            lokacija = f" Lokacija: {pot.naziv_lokacije}"
            pots_info.append(f"{naziv}{lokacija}")

        self.pots_var = tk.Variable(value=pots_info)
        self.listbox = tk.Listbox(self.frame_list_pots,
                                  listvariable=self.pots_var,
                                  height=20,
                                  selectmode=tk.SINGLE, 
                                  width=45)
        self.listbox.pack(fill=tk.Y)
        self.listbox.bind("<<ListboxSelect>>", self.pot_selected)
    


    def pot_selected(self, event):
        selected_pot = self.listbox.curselection()
        if not selected_pot:
            return
        pot_index = selected_pot[0]
        pot = self.user_pots[pot_index]

        if hasattr(self, "frame_pot"):
            self.pot_lokacija.set("Lokacija posude: " + pot.naziv_lokacije)
            self.postavi_sliku(pot)
        else:
            self.frame_pot = tk.Frame(self.parent_frame)
            self.frame_pot.pack(padx=10, pady=10, ipady=20, fill=tk.BOTH, expand=True)

            self.pot_lokacija = tk.StringVar()
            self.pot_lokacija.set("Lokacija posude: " + pot.naziv_lokacije)
            lbl_pot_lokacija = tk.Label(self.frame_pot, textvariable=self.pot_lokacija, font=(CALIBRI_FONT, 16))
            lbl_pot_lokacija.pack(pady=5)

            self.pot_slika_label = None
            self.postavi_sliku(pot)

    def postavi_sliku(self, pot):
        if self.pot_slika_label is not None:
            self.pot_slika_label.destroy()  # Uklanja prethodnu sliku iz prikaza
        naziv_final = str(pot.biljka.naziv).lower().replace("ž","z").replace("š","s")
        path = f"Pictures/{naziv_final}.png"
        try:
            self.pot_slika = tk.PhotoImage(file=path)
            self.pot_slika_label = tk.Label(self.frame_pot, image=self.pot_slika)
            self.pot_slika_label.pack(pady=5)
        except tk.TclError:
            print("Slika nije pronađena!")

    def clear_frame_list_pots(self):
        print("clear_frame_list_pots")
        self.frame_list_pots.destroy()

            
            




            

            
