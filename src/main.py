import customtkinter as ctk
import json

import serial_console
import menu
import quit_app_window


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # assign quit app window
        self.protocol("WM_DELETE_WINDOW", self.OnQuitApp)

        # configure window
        self.title("FlowFusion 1.0")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        app_window_width = 1100
        app_window_height = 580
        self.geometry(
            f"{app_window_width}x{app_window_height}+{int(screen_width/2-app_window_width/2)}+{int(screen_height/2-app_window_height/2)}")
        self.minsize(app_window_width, app_window_height)
        self.grab_set()

        # configure grid layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # create frames
        self.menu_frame = menu.Menu(self)
        self.menu_frame.grid(row=0, column=0, rowspan=2, sticky="ns")

        self.serial_console_frame = serial_console.SerialConsole(self)
        self.serial_console_frame.grid(row=1, column=1, sticky="nsew")

        settings_data = self.loadSettings()
        self.updateSettings(settings_data)

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

    def updateSettings(self, settings_data: dict):
        self.settings_data = settings_data
        serial_line_ending = settings_data.get('lineending')
        baudrate = settings_data.get('baudrate')
        serial_port = settings_data.get('port')
        appearance = settings_data.get('appearance')
        save_folder = settings_data.get('save_folder')

        # change serial settings
        self.serial_console_frame.updateSerialSettings(
            serial_port=serial_port, baudrate=baudrate, line_ending=serial_line_ending)

        # set theme and appearance mode
        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme("blue")

        # change save folder
        # TODO: implement save folder change

    def sendSettingsData(self):
        return self.settings_data

    def saveSettingsOnExit(self):
        settings_data = self.loadSettings()
        with open('settings.json', 'w') as jfile:
            json.dump(settings_data, jfile, indent=4)
            jfile.close()

    def configureButtons(self, frame: str, buttons: tuple, state: str):
        # TODO: implement enable/disable buttons when a device is connected/disconnected
        pass

    def updateSerialDeviceStatus(self, status: str):
        # TODO: implement this
        pass

    def disconnectDevices(self):
        self.serial_console_frame.closePort()

    def OnQuitApp(self):
        quit_app = quit_app_window.OnQuitApp(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
