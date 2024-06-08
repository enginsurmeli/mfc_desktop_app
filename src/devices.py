from customtkinter import *


class DevicesFrame(CTkFrame):
    def __init__(self, parent, master):
        super().__init__(master)

        self.parent = parent


class DeviceButton(CTkButton):
    def __init__(self, master, device_name):
        super().__init__(master, text=device_name)
