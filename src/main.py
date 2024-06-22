from customtkinter import *
import json
import os
import sys
from PIL import ImageTk

import sidebar_menu
import dashboard
import quit_app_window


class App(CTk):

    def __init__(self):
        super().__init__()

        # assign quit app window
        self.protocol("WM_DELETE_WINDOW", self.OnQuitApp)

        # configure window
        self.title("FlowFusion 1.0")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        app_window_width = 1100
        app_window_height = 600
        self.geometry(
            f"{app_window_width}x{app_window_height}+{int(screen_width/2-app_window_width/2)}+{int(screen_height/2-app_window_height/2)}")
        # self.minsize(app_window_width, app_window_height)
        self.resizable(False, False)
        self.grab_set()

        self.icons_folder_path = os.path.join(
            os.getcwd(), 'src', 'icons')

        # load app icon
        try:
            # self.iconbitmap(os.path.join(self.icons_folder_path, "microscope_logo.ico"))
            iconpath = os.path.join(
                self.icons_folder_path, "app_logo_light.png")
            icon = ImageTk.PhotoImage(file=iconpath)
            self.wm_iconbitmap()
            self.after(300, lambda: self.iconphoto(False, icon))
        except:
            pass

        # configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=15)
        self.grid_rowconfigure(0, weight=1)

        # load settings
        self.settings_data = self.loadSettings()

        # create frames
        self.sidebar_menu_frame = sidebar_menu.SidebarMenu(self)
        self.sidebar_menu_frame.grid(row=0, column=0, sticky="nsew")

        self.dashboard_frame = dashboard.Dashboard(self)
        self.dashboard_frame.grid(row=0, column=1, sticky="nsew")

        # apply settings
        self.applySettings(self.settings_data)

    def loadSettings(self):
        settings_data = {}
        jfile = None

        try:
            jfile = open('settings.json')
            settings_data = json.load(jfile)
        except FileNotFoundError as fnfe:
            pass
        if jfile:
            jfile.close()

        return settings_data

    def applySettings(self, settings_data: dict):
        serial_line_ending = settings_data.get('lineending')
        baudrate = settings_data.get('baudrate')
        serial_port = settings_data.get('port')
        appearance = settings_data.get('appearance')
        save_folder = settings_data.get('save_folder')

        # # change serial settings
        # self.serial_console_frame.updateSerialSettings(
        #     serial_port=serial_port, baudrate=baudrate, line_ending=serial_line_ending)

        # set theme and appearance mode
        set_appearance_mode(appearance)
        # set_default_color_theme("blue")

        # change color of plot area
        # TODO: when 'System' is selected, the colors should be either dark or light based on the system theme
        color_palette = {'Light': {'bg': '#dbdbdb', 'fg': '#252526'}, 'Dark': {
            'bg': '#2b2b2b', 'fg': '#dce4ee'}, 'System': {'bg': '', 'fg': ''}}
        self.dashboard_frame.updatePlotTheme(color_palette.get(appearance))

        # change save folder
        # TODO: implement save folder change

    # def sendSerialCommand(self, command: str):
    #     self.serial_console_frame.send(button_command=command)

    def saveSettingsOnExit(self):
        settings_data = self.loadSettings()
        with open('settings.json', 'w') as jfile:
            json.dump(settings_data, jfile, indent=4)
            jfile.close()

    def configureButtons(self, frame: str, buttons: tuple, state: str):
        # TODO: implement enable/disable buttons when a device is connected/disconnected
        pass

    def updateDeviceStatus(self, status: str):
        # TODO: implement this to show if the device is connected or not
        pass

    def disconnectDevices(self):
        # self.serial_console_frame.closePort()
        pass

    def OnQuitApp(self):
        quit_app_window.OnQuitApp(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
