import tkinter as tk
from datetime import datetime

from Tabs.Meteo.fetch_data import *
from Database.database import Meteo, db_add_meteo_data

# from fetch_data import *


FONT_BIG = ("Calibri", 25, "bold")
FONT_SMALL = ("Calibri", 15)


class MeteoTab:
    def __init__(self, smart_home, parent_frame, logged_user):
        self.smart_home = smart_home
        self.parent_frame = parent_frame
        self.logged_user = logged_user

        self.dhmz_data = extract_dhmz_data()
        self.inside_temp = simulate_inside_temp()
        self.outside_temp = random_gauss_variation(self.dhmz_data["temp"])

        self.create_gui()

    def create_gui(self):
        self.frame_meteo = tk.Frame(self.parent_frame)
        self.time_var = tk.StringVar()
        self.inside_var = tk.StringVar()
        self.outside_var = tk.StringVar()
        self.temp_var = tk.StringVar()
        self.humidity_var = tk.StringVar()
        self.pressure_var = tk.StringVar()

        self.frame_meteo.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1, minsize=30)
        self.frame_meteo.columnconfigure([0, 1], weight=1, minsize=50)

        tk.Label(
            self.frame_meteo, textvariable=self.time_var, font=FONT_BIG, bg="red"
        ).grid(row=0, column=0, columnspan=2, sticky="n", pady=10)

        tk.Label(self.frame_meteo, text="Inside temperature", font=FONT_SMALL).grid(
            row=1, column=0, sticky="e"
        )
        tk.Label(self.frame_meteo, textvariable=self.inside_var, font=FONT_SMALL).grid(
            row=1, column=1, sticky="w"
        )

        tk.Label(self.frame_meteo, text="Outside temperature", font=FONT_SMALL).grid(
            row=2, column=0, sticky="e"
        )
        tk.Label(self.frame_meteo, textvariable=self.outside_var, font=FONT_SMALL).grid(
            row=2, column=1, sticky="w"
        )

        tk.Label(self.frame_meteo, text="City temperature", font=FONT_SMALL).grid(
            row=3, column=0, sticky="e"
        )
        tk.Label(self.frame_meteo, textvariable=self.temp_var, font=FONT_SMALL).grid(
            row=3, column=1, sticky="w"
        )

        tk.Label(self.frame_meteo, text="City humidity", font=FONT_SMALL).grid(
            row=4, column=0, sticky="e"
        )
        tk.Label(
            self.frame_meteo, textvariable=self.humidity_var, font=FONT_SMALL
        ).grid(row=4, column=1, sticky="w")

        tk.Label(self.frame_meteo, text="City Pressure", font=FONT_SMALL).grid(
            row=5, column=0, sticky="e"
        )
        tk.Label(
            self.frame_meteo, textvariable=self.pressure_var, font=FONT_SMALL
        ).grid(row=5, column=1, sticky="w")

        self.add_icon()

        self.update_meteo_data()

    def update_meteo_data(self):
        inside_temp = random_variation(self.inside_temp)
        outside_temp = random_variation(self.outside_temp)
        datetime_now = datetime.now()

        self.time_var.set(datetime_now.strftime("%H:%M:%S  %d-%m-%Y"))
        self.inside_var.set(inside_temp)
        self.outside_var.set(outside_temp)
        self.temp_var.set(self.dhmz_data["temp"])
        self.humidity_var.set(self.dhmz_data["humidity"])
        self.pressure_var.set(self.dhmz_data["pressure"])

        meteo_entry = Meteo(
            datetime=datetime_now,
            city_temp=self.dhmz_data["temp"],
            city_humidity=self.dhmz_data["humidity"],
            city_pressure=self.dhmz_data["pressure"],
            inside_temp=inside_temp,
            outside_temp=outside_temp,
        )
        db_add_meteo_data(meteo_entry)

        # run this method every 1000ms to update labels in real time
        self.frame_meteo.after(1000, self.update_meteo_data)

    def add_icon(self):
        frame_icon = tk.Frame(self.frame_meteo)
        frame_icon.grid(row=6, column=0, columnspan=2)

        icons_folder = "C:\\Users\\kruno\\OneDrive\\Desktop\\python_tecaj\\python-predavanja\\smart_home\\Tabs\\Meteo\\icons\\"
        if self.outside_temp > 22:
            icon_name = "tshirt.png"
        elif self.outside_temp > 12:
            icon_name = "lightjacket.png"
        elif self.outside_temp > 0:
            icon_name = "warmjacket.png"
        else:
            icon_name = "winterclothes.png"

        self.img = tk.PhotoImage(file=icons_folder + icon_name).subsample(3)
        tk.Label(frame_icon, image=self.img).pack(pady=20)

    def activate_tab(self):
        self.frame_meteo.pack(padx=10, pady=10, fill=tk.BOTH)
        self.frame_meteo.update_idletasks()

    def deactivate_tab(self):
        self.frame_meteo.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    meteo = MeteoTab(root, None, root, None)
    meteo.activate_tab()
    root.mainloop()
