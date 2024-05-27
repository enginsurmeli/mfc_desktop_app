import customtkinter as ctk

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
        self.menu_frame.grid(row=0, column=0, sticky="ns")

    def sendSettingsData(self):
        pass

    def saveSettingsOnExit(self):
        pass

    def disconnectDevices(self):
        pass

    def OnQuitApp(self):
        quit_app = quit_app_window.OnQuitApp(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
