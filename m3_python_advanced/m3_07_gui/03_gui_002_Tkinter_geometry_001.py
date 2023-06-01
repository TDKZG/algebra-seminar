"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Pozicioniranje elemenata unutar prozora
"""

import tkinter as tk


root = tk.Tk()
root.title("Algebra - Python programer")
root.geometry("600x400")


photo_image = tk.PhotoImage(file="m3_05_foto/Fotografije/python-logo.png").subsample(50)
button_image = tk.Button(
    root,
    text="Gumb sa slicicom",
    image=photo_image,
    compound=tk.LEFT,
).place(x=150, y=75)

label = tk.Label(root, text="Labela")
label.place(x=200, y=90)

root.mainloop()
