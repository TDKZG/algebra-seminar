"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Gumb - BUTTON
"""


import tkinter as tk


def click():
    print("Gumb je kliknut")


root = tk.Tk()
root.title("Algebra - Python programer")
root.geometry("600x400")


label = tk.Label(root, text="PORUKA", font=("Segoe UI", 16))
label.pack(padx=30)

photo_image = tk.PhotoImage(file="m3_05_foto/Fotografije/python-logo.png").subsample(10)
label_image = tk.Label(
    root,
    text="Tekst u oznaci",
    font=("Segoe UI", 20),
    compound=tk.CENTER,
    image=photo_image,
).pack(padx=5)


root.mainloop()
