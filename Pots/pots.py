import tkinter as tk

from Database.database import *

class UserPots:
    def __init__(self, py_posude, parent_frame, logged_user):
        self.py_posude = py_posude
        self.parent_frame = parent_frame
        self.logged_user = logged_user
        self.create_gui()
    
    def create_gui(self):
        self.frame_settings = tk.Frame(self.parent_frame)
        self.list_user_pots()
    



    def list_user_pots(self):

        self.user_pots = db_user_pots(self.logged_user)
        #print("self.user_pots:",self.user_pots)
        self.frame_list_pots = tk.Frame(self.parent_frame)
        self.frame_list_pots.pack(padx=10, pady=10, fill=tk.Y, side=tk.LEFT)

        pots_info = []

        for pot in self.user_pots:
            pots_info.append(f"{pot.id}  {pot.naziv_lokacije}   {pot.korisnik_id}")

        self.pots_var = tk.Variable(value=pots_info)
        self.listbox = tk.Listbox(self.frame_list_pots,
                                  listvariable=self.pots_var,
                                  height=10,
                                  selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.Y, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.pot_selected)
    


    def pot_selected(self, event):
        selected_pot = self.listbox.curselection()
        if not selected_pot:
            return
        pot_index = selected_pot[0] 
        pot = self.user_pots[pot_index]

        if hasattr(self, "frame_pot"):
            self.pot_lokacija.set("Lokacija posude: " + pot.naziv_lokacije)
        else:
            self.frame_pot = tk.Frame(self.parent_frame)
            self.frame_pot.pack(padx=10, pady=10, ipady=20, fill=tk.BOTH, expand=True)
            self.pot_lokacija = tk.StringVar()
            self.pot_lokacija.set("Lokacija posude: " + pot.naziv_lokacije)
            lbl_pot_lokacija = tk.Label(self.frame_pot, textvariable=self.pot_lokacija)
            lbl_pot_lokacija.pack(pady=5)


            

            
