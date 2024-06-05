from customtkinter import *
from PIL import Image
import os
import sys


class SidebarMenu(CTkFrame):
    def __init__(self, master, icons_folder_path):
        super().__init__(master)

        self.master = master
        self.configure(fg_color="#1f6ba5")
        self.configure(corner_radius=0)

        button_font = ("Arial Bold", 16)

        logo_img_light = Image.open(os.path.join(
            icons_folder_path, "app_logo_light.png"))
        logo_img_dark = Image.open(os.path.join(
            icons_folder_path, "app_logo_dark.png"))
        logo_img = CTkImage(
            dark_image=logo_img_light, light_image=logo_img_dark, size=(85, 85))
        logo_label = CTkLabel(self, text="", image=logo_img)
        logo_label.pack(pady=(38, 0), anchor="center")

        home_button = CTkButton(
            self, text="Home", font=button_font, command=self.openHome)
        home_button.pack(
            anchor="center", pady=(60, 0))

        devices_button = CTkButton(
            self, text="Devices", font=button_font, command=self.openDevices)
        devices_button.pack(
            anchor="center", pady=(16, 0))

        settings_button = CTkButton(
            self, text="Settings", font=button_font, command=self.openSettings)
        settings_button.pack(
            anchor="center", pady=(16, 0))

    def openHome(self):
        # self.master.dashboard_frame.showTab("Home")
        pass

    def openDevices(self):
        # self.master.dashboard_frame.showTab("Devices")
        pass

    def openSettings(self):
        # settings = settings_window.SettingsWindow(
        #     self.master, self.master.sendSettingsData())
        pass
