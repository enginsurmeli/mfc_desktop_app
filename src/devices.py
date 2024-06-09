from customtkinter import *


class DevicesFrame(CTkFrame):
    def __init__(self, parent, master):
        super().__init__(master)

        self.parent = parent

        add_device_button = DeviceButton(self)
        add_device_button.grid(row=0, column=0, padx=10, pady=10)


class DeviceButton(CTkButton):
    def __init__(self, master):
        super().__init__(master)

        self.configure(text="➕", width=50, height=30,
                       font=("", 30), anchor="center")
