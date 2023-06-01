import tkinter as tk

from Database.database import *


class SettingsTab:
    def __init__(self, smart_home, parent_frame, logged_user):
        self.smart_home = smart_home
        self.parent_frame = parent_frame
        self.logged_user = logged_user
        self.create_gui()

    def create_gui(self):
        self.frame_settings = tk.Frame(self.parent_frame)

        btn_devices = tk.Button(
            self.frame_settings, text="Devices", command=self.list_devices
        )
        btn_devices.pack(padx=10, pady=10, fill=tk.X)

        if self.logged_user.admin:
            btn_users = tk.Button(self.frame_settings, text="Users")
            btn_users.pack(padx=10, pady=10, fill=tk.X)

        btn_logout = tk.Button(
            self.frame_settings, text="Logout", command=self.smart_home.logout
        )
        btn_logout.pack(padx=10, pady=10, fill=tk.X)

    def activate_tab(self):
        self.frame_settings.pack(padx=10, pady=10, fill=tk.Y, side=tk.LEFT)
        self.frame_settings.update_idletasks()

    def deactivate_tab(self):
        self.frame_settings.pack_forget()
        if hasattr(self, "frame_list_devices"):
            self.frame_list_devices.pack_forget()
        if hasattr(self, "frame_device"):
            self.frame_device.pack_forget()

    def list_devices(self):
        if hasattr(self, "frame_list_devices"):
            return
        self.frame_list_devices = tk.Frame(self.parent_frame)
        self.frame_list_devices.pack(padx=10, pady=10, fill=tk.Y, side=tk.LEFT)

        self.devices = db_devices()
        devices_info = []
        for device in self.devices:
            devices_info.append(f"{device.name} {device.brand}")

        self.devices_var = tk.Variable(value=devices_info)
        self.listbox = tk.Listbox(
            self.frame_list_devices,
            listvariable=self.devices_var,
            height=10,
            selectmode=tk.SINGLE,
        )
        self.listbox.pack(fill=tk.Y, expand=True)

        self.listbox.bind("<<ListboxSelect>>", self.device_selected)

        self.frame_list_devices.update_idletasks()

    def on_save_device(self):
        index_device = self.listbox.curselection()
        device = self.devices[index_device[0]]
        db_update_device(device)
        self.frame_device.destroy()
        delattr(self, "frame_device")

    def on_cancel(self):
        self.frame_device.destroy()
        delattr(self, "frame_device")

    def device_selected(self, event):
        selected_device = self.listbox.curselection()
        if not selected_device:
            return
        index_device = selected_device[0]
        device = self.devices[index_device]

        if hasattr(self, "frame_device"):
            self.device_brand.set(device.brand)
            self.device_name.set(device.name)
            self.device_location.set(device.location)
            self.device_status.set(device.status)
        else:
            self.frame_device = tk.Frame(self.parent_frame)
            self.frame_device.pack(
                padx=10, pady=10, ipadx=20, ipady=20, fill=tk.BOTH, expand=True
            )

            lbl_device_brand = tk.Label(self.frame_device, text="Device brand")
            lbl_device_brand.pack(pady=5)

            self.device_brand = tk.StringVar()
            self.device_brand.set(device.brand)
            ent_device_brand = tk.Entry(
                self.frame_device, textvariable=self.device_brand
            )
            ent_device_brand.pack(pady=5)

            lbl_device_name = tk.Label(self.frame_device, text="Device name")
            lbl_device_name.pack(pady=5)

            self.device_name = tk.StringVar()
            self.device_name.set(device.name)
            ent_device_name = tk.Entry(self.frame_device, textvariable=self.device_name)
            ent_device_name.pack(pady=5)

            lbl_device_location = tk.Label(self.frame_device, text="Device location")
            lbl_device_location.pack(pady=5)

            self.device_location = tk.StringVar()
            self.device_location.set(device.location)
            ent_device_location = tk.Entry(
                self.frame_device, textvariable=self.device_location
            )
            ent_device_location.pack(pady=5)

            lbl_device_status = tk.Label(self.frame_device, text="Device status")
            lbl_device_status.pack(pady=5)

            self.device_status = tk.BooleanVar()
            self.device_status.set(device.status)
            chk_device_status = tk.Checkbutton(
                self.frame_device, variable=self.device_status
            )
            chk_device_status.pack()

            btn_save = tk.Button(
                self.frame_device, text="Save", command=self.on_save_device
            )
            btn_save.pack(padx=20, pady=10, ipadx=5, ipady=5, side=tk.LEFT)

            btn_cancel = tk.Button(
                self.frame_device, text="Cancel", command=self.on_cancel
            )
            btn_cancel.pack(padx=20, pady=10, ipadx=5, ipady=5, side=tk.RIGHT)
