from customtkinter import *


class Dashboard(CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Home")
        self.add("Devices")
        self.add("Settings")

        # remove segmented button
        self._top_spacing = 0
        self._top_button_overhang = 0
        self._segmented_button.grid_forget()
        self._configure_grid()

        # add widgets on tabs
