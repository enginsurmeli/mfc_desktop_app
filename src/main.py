import customtkinter as ctk

import serial_console
import settings_window
import quit_app_window


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # assign quit app window
        self.protocol("WM_DELETE_WINDOW", self.OnQuitApp)

        # configure window
        self.title("FlowFusion 1.0")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

    def saveSettingsOnExit(self):
        pass

    def disconnectDevices(self):
        pass

    def OnQuitApp(self):
        quit_app = quit_app_window.OnQuitApp(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
