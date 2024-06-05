from customtkinter import *
import settings_window
from PIL import Image


class SidebarMenu(CTkFrame):
    def __init__(self, master, logo):
        super().__init__(master)

        self.master = master
        self.configure(fg_color="#1f6ba5")
        self.configure(corner_radius=0)

        inner_frame_padding = 5

        logo_img = CTkImage(
            dark_image=Image.open(logo), light_image=Image.open(logo), size=(77.68, 85.42))
        logo_label = CTkLabel(self, text="", image=logo_img).pack(
            pady=(38, 0), anchor="center")

        settings_button = CTkButton(
            self, text="Settings", font=("Arial Bold", 14), command=self.openSettings)
        # settings_button.grid(
        #     row=0, column=0, padx=inner_frame_padding, pady=inner_frame_padding)
        settings_button.pack(
            side="top", padx=inner_frame_padding, pady=inner_frame_padding)

    def openSettings(self):
        settings = settings_window.SettingsWindow(
            self.master, self.master.sendSettingsData())
