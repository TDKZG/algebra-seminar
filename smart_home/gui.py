import tkinter as tk

from Database.database import *
from Tabs.Settings.settings import SettingsTab
from Tabs.Meteo.meteo import MeteoTab

CALIBRI_FONT = "Calibri"


class MySmartHome:
    def __init__(self, root):
        self.root = root
        self.create_login_screen()

    def clear_root(self):
        for child in self.root.winfo_children():
            child.destroy()

    def login(self):
        self.user = db_login(self.username.get(), self.password.get())
        if self.user == None:
            print("Ne postoji user s tim usernamom i passwordom")
            return
        print(f"Dobrodosli {self.user.name}")
        self.clear_root()
        self.create_main_screen()

    def logout(self):
        self.clear_root()
        self.create_login_screen()

    def create_login_screen(self):
        self.frame_login = tk.Frame(self.root)
        self.frame_login.pack(fill=tk.X, padx=10, pady=10)

        lbl_header = tk.Label(
            self.frame_login, text="Smart Home", font=(CALIBRI_FONT, 20)
        )
        lbl_header.pack()

        lbl_login = tk.Label(self.frame_login, text="Login", font=(CALIBRI_FONT, 16))
        lbl_login.pack(pady=30)

        lbl_username = tk.Label(
            self.frame_login, text="Username", font=(CALIBRI_FONT, 12)
        )
        lbl_username.pack(pady=15)

        self.username = tk.StringVar()
        ent_username = tk.Entry(self.frame_login, textvariable=self.username)
        ent_username.pack(pady=5)

        lbl_password = tk.Label(
            self.frame_login, text="Password", font=(CALIBRI_FONT, 12)
        )
        lbl_password.pack(pady=15)

        self.password = tk.StringVar()
        ent_password = tk.Entry(self.frame_login, textvariable=self.password, show="*")
        ent_password.pack(pady=5)

        btn_login = tk.Button(self.frame_login, text="Login", command=self.login)
        btn_login.pack(pady=10, ipadx=5, ipady=5)
        self.frame_login.update_idletasks()

    def activate_tab(self, tab_name):
        for name, btn in self.btn_tabs.items():
            if name == tab_name:
                btn["state"] = "disable"
            else:
                btn["state"] = "normal"

        for name, tab in self.tabs.items():
            if name == tab_name:
                tab.activate_tab()
            else:
                tab.deactivate_tab()

    def create_main_screen(self):
        self.frame_main_screen = tk.Frame(self.root)
        self.frame_main_screen.pack(fill=tk.BOTH, expand=True)

        self.frame_header = tk.Frame(self.frame_main_screen)
        self.frame_header.pack(fill=tk.X, padx=10, pady=10)

        self.frame_display = tk.Frame(self.frame_main_screen)
        self.frame_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        settings_tab = SettingsTab(self, self.frame_display, self.user)
        meteo_tab = MeteoTab(self, self.frame_display, self.user)

        self.tabs = {"settings": settings_tab, "meteo": meteo_tab}

        btn_settings = tk.Button(
            self.frame_header,
            text="Settings",
            command=lambda: self.activate_tab("settings"),
        )
        btn_settings.pack(padx=10, pady=10, ipadx=5, ipady=5, side=tk.LEFT, expand=True)

        btn_lights = tk.Button(
            self.frame_header,
            text="Control Lights and Blinds",
            command=lambda: self.activate_tab("lights"),
        )
        btn_lights.pack(padx=40, pady=10, ipadx=5, ipady=5, side=tk.LEFT, expand=True)

        btn_tasks = tk.Button(
            self.frame_header,
            text="Daily Tasks",
            command=lambda: self.activate_tab("tasks"),
        )
        btn_tasks.pack(padx=40, pady=10, ipadx=5, ipady=5, side=tk.LEFT, expand=True)

        btn_meteo = tk.Button(
            self.frame_header,
            text="Meteo",
            command=lambda: self.activate_tab("meteo"),
        )
        btn_meteo.pack(padx=40, pady=10, ipadx=5, ipady=5, side=tk.LEFT, expand=True)

        self.btn_tabs = {
            "settings": btn_settings,
            "lights": btn_lights,
            "tasks": btn_tasks,
            "meteo": btn_meteo,
        }


root = tk.Tk()
root.geometry("1000x600")
root.title("My Smart Home")
smart_home = MySmartHome(root)
root.mainloop()
