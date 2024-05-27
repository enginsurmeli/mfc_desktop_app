import customtkinter as ctk
import settings_window


class Menu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        inner_frame_padding = 5

        settings_button = ctk.CTkButton(
            self, text="Settings", command=self.openSettings)
        settings_button.grid(
            row=0, column=0, padx=inner_frame_padding, pady=inner_frame_padding)

    def openSettings(self):
        settings = settings_window.SettingsWindow(
            self.master, self.master.sendSettingsData())
