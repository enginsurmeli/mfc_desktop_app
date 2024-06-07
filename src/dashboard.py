from customtkinter import *
import settings
import json


class Dashboard(CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        # create tabs
        self.add("Home")
        self.add("Devices")
        self.add("Settings")

        # remove segmented button of tabview
        self._top_spacing = 0
        self._top_button_overhang = 0
        self._segmented_button.grid_forget()
        self._configure_grid()

        # add frames on tabs
        home_frame = CTkFrame(master=self.tab("Home"))
        home_frame.pack(fill=BOTH, expand=True)

        devices_frame = CTkFrame(master=self.tab("Devices"))
        devices_frame.pack(fill=BOTH, expand=True)

        settings_frame = settings.SettingsFrame(
            parent=self, master=self.tab("Settings"))
        settings_frame.pack(fill=BOTH, expand=True)

    def showTab(self, tab_name: str):
        self.set(tab_name)

    def sendSettingsData(self):
        return self.master.sendSettingsData()
