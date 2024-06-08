from customtkinter import *
from PIL import Image
import os


class SidebarMenu(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        icons_folder_path = master.icons_folder_path
        self.configure(fg_color="#1f6ba5")
        self.configure(corner_radius=0)

        button_font = ("Arial Bold", 16)

        logo_img_light = Image.open(os.path.join(
            icons_folder_path, "app_logo_dark.png"))
        logo_img_dark = Image.open(os.path.join(
            icons_folder_path, "app_logo_dark.png"))
        logo_img = CTkImage(
            dark_image=logo_img_light, light_image=logo_img_dark, size=(85, 85))
        logo_label = CTkLabel(self, text="", image=logo_img)
        logo_label.pack(pady=(38, 0), anchor="center")

        home_button = CTkButton(
            self, text="Home", font=button_font, command=self.showHome)
        home_button.pack(
            anchor="center", pady=(60, 0))

        devices_button = CTkButton(
            self, text="Devices", font=button_font, command=self.showDevices)
        devices_button.pack(
            anchor="center", pady=(16, 0))

        settings_button = CTkButton(
            self, text="Settings", font=button_font, command=self.showSettings)
        settings_button.pack(
            anchor="center", pady=(16, 0))

    def showHome(self):
        self.master.dashboard_frame.showTab("Home")

    def showDevices(self):
        self.master.dashboard_frame.showTab("Devices")

    def showSettings(self):
        self.master.dashboard_frame.showTab("Settings")
