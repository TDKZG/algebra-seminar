import tkinter as tk

from Database.database import *

CALIBRI_FONT = "Calibri"

class Forme:
    def __init__(self, py_posude, parent_frame, logged_user):
        self.py_posude = py_posude
        self.parent_frame = parent_frame
        self.logged_user = logged_user
        self.create_gui()
    
    def create_gui(self):

        self.clear_parent()
        self.frame_forma_nova_posuda = tk.Frame(self.parent_frame)
        self.frame_forma_nova_posuda.pack(padx=10, pady=10)

        lbl_naziv_posude = tk.Label(self.parent_frame, text="Naziv posude:")
        lbl_naziv_posude.pack(padx=10, pady=10, side=tk.LEFT)

        lbl_empty = tk.Label(self.parent_frame, text="")
        lbl_empty.pack(side=tk.LEFT, padx=5)

        lbl_biljka = tk.Label(self.parent_frame, text="Odaberi biljku:")
        lbl_biljka.pack(padx=10, pady=10, side=tk.LEFT)

    def clear_parent(self):
        for child in self.parent_frame.winfo_children():
            child.destroy()