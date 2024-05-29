import customtkinter as ctk


class DeviceControl(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(self, text="Device Control")
        label.pack()
