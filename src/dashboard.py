from customtkinter import *
import home
import devices
import settings
import json


class Dashboard(CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.configure(width=750)

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
        self.home_frame = home.HomeFrame(parent=self, master=self.tab("Home"))
        self.home_frame.pack(fill=BOTH, expand=True)

        devices_frame = devices.DevicesFrame(
            parent=self, master=self.tab("Devices"))
        devices_frame.pack(fill=BOTH, expand=True)

        settings_frame = settings.SettingsFrame(
            parent=self, master=self.tab("Settings"))
        settings_frame.pack(fill=BOTH, expand=True)

    def showTab(self, tab_name: str):
        self.set(tab_name)

    def getSettingsData(self):
        return self.master.settings_data

    def applySettings(self, settings_data):
        self.master.applySettings(settings_data)

    def getIconsFolderPath(self):
        return self.master.icons_folder_path

    def updatePlotTheme(self, color_palette: dict):
        self.home_frame.updatePlotTheme(color_palette)
