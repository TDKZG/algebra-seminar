"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Tkinter events
"""

import tkinter as tk


unesena_slova = ""

def on_keypress(event):
    print(event.char)
    global unesena_slova
    unesena_slova += str(event.char)
    label_text_var.set(unesena_slova)


root = tk.Tk()
root.title("Algebra")
root.geometry("600x400")

label_text_var = tk.StringVar()
label_text_var.set("Ovo je mjesto gdje ce se prikazivati unesena slova")

label_naslov = tk.Label(root, text="Key event", font=("Segoe UI", 18))
label_naslov.grid(column=0, row=0)

label_ispis = tk.Label(
    root, textvariable=label_text_var, font=("Segoe UI", 24), fg="red"
)
label_ispis.grid(column=0, row=1)

root.bind("<Key>", on_keypress)

root.mainloop()
