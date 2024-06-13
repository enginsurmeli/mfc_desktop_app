from customtkinter import *
import data_display
import device_control
import serial_console


class HomeFrame(CTkFrame):
    def __init__(self, parent, master):
        super().__init__(master)

        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # Create frames
        self.data_display_frame = data_display.DataDisplay(self)
        self.data_display_frame.grid(
            row=0, column=0, columnspan=2, sticky="nsew")
        device_control_frame = device_control.DeviceControl(self)
        device_control_frame.grid(row=1, column=0, sticky="nsew")
        serial_console_frame = serial_console.SerialConsole(self)
        serial_console_frame.grid(row=1, column=1, sticky="nsew")

    def getIconsFolderPath(self):
        return self.parent.getIconsFolderPath()

    def updatePlotTheme(self, color_palette: dict):
        self.data_display_frame.updateTheme(color_palette)
