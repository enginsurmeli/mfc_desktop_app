from customtkinter import *
import serial.tools.list_ports
import tkinter.ttk as ttk
from tkinter import filedialog
import json


class SettingsFrame(CTkFrame):
    def __init__(self, master, settings_data: dict):
        super().__init__(master)

        self.master = master
        self.settings_data = settings_data

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2, 3), weight=0)

        ok_button = CTkButton(
            self, text="OK", command=self.applyAndReturn)
        ok_button.grid(row=1, column=1, padx=10, pady=10)

        cancel_button = CTkButton(
            self, text="Cancel", command=self.revertSettings)
        cancel_button.grid(row=1, column=2, padx=10, pady=10)

        apply_button = CTkButton(
            self, text="Apply", command=self.applySettings)
        apply_button.grid(row=1, column=3, padx=10, pady=10)
        # TODO: activate apply button onlt if changes are made

        self.settings_frame = CTkFrame(self)
        self.settings_frame.grid(
            row=0, column=0, columnspan=3, padx=10, pady=10)

        # self.settings_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)
        # self.settings_frame.grid_columnconfigure((0, 1, 2, 3), weight=0)

        # # create labels and separators
        # serial_port_label = CTkLabel(
        #     self.settings_frame, text="Serial Port")
        # serial_port_label.grid(row=0, column=0, padx=10, pady=10)
        # separator_1 = ttk.Separator(
        #     self.settings_frame, orient="horizontal")
        # separator_1.grid(row=1, column=0, columnspan=4,
        #                  padx=10, pady=5, sticky="ew")
        # appearance_label = CTkLabel(
        #     self.settings_frame, text="Appearance")
        # appearance_label.grid(row=4, column=0, padx=10, pady=10)
        # separator_2 = ttk.Separator(self.settings_frame, orient="horizontal")
        # separator_2.grid(row=5, column=0, columnspan=4,
        #                  padx=10, pady=5, sticky="ew")
        # save_folder_label = CTkLabel(
        #     self.settings_frame, text="Save Location")
        # save_folder_label.grid(row=6, column=0, padx=10, pady=10)

        # # list available serial ports
        # self.serial_ports_optionmenu = CTkOptionMenu(
        #     self.settings_frame, values=[], dynamic_resizing=False)
        # self.refreshSerialPorts(self.serial_ports_optionmenu)
        # self.serial_ports_optionmenu.grid(row=0, column=1, padx=10, pady=10)

        # # create a list of baud rates
        # baud_rates = ["9600", "19200", "38400", "57600", "115200"]
        # self.baud_rates_optionmenu = CTkOptionMenu(
        #     self.settings_frame, values=baud_rates)
        # self.baud_rates_optionmenu.grid(row=0, column=2, padx=10, pady=10)

        # # create a list of line endings
        # line_endings = ["None", "CR", "LF", "Both CR&LF"]
        # self.line_endings_optionmenu = CTkOptionMenu(
        #     self.settings_frame, values=line_endings)
        # self.line_endings_optionmenu.grid(row=0, column=3, padx=10, pady=10)

        # # create a list of appearance modes and accent colors
        # self.appearance_optionmenu = CTkOptionMenu(
        #     self.settings_frame, values=["Light", "Dark", "System"])
        # self.appearance_optionmenu.grid(row=4, column=1, padx=10, pady=10)

        # # entrybox for save data path
        # self.save_folder_entry = CTkEntry(self.settings_frame)
        # self.save_folder_entry.grid(
        #     row=6, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        # self.selectFolder_button = CTkButton(
        #     self.settings_frame, text="Select Folder", command=self.selectFolder)
        # self.selectFolder_button.grid(row=6, column=3, padx=10, pady=10)

        # Frame for serial port settings
        serial_port_frame = CTkFrame(self.settings_frame)
        serial_port_frame.pack(fill="x", padx=10, pady=5)

        serial_port_label = CTkLabel(serial_port_frame, text="Serial Port")
        serial_port_label.pack(side="left", padx=10, pady=10)

        self.serial_ports_optionmenu = CTkOptionMenu(
            serial_port_frame, values=[], dynamic_resizing=False)
        self.refreshSerialPorts(self.serial_ports_optionmenu)
        self.serial_ports_optionmenu.pack(side="left", padx=10, pady=10)

        baud_rates = ["9600", "19200", "38400", "57600", "115200"]
        self.baud_rates_optionmenu = CTkOptionMenu(
            serial_port_frame, values=baud_rates)
        self.baud_rates_optionmenu.pack(side="left", padx=10, pady=10)

        line_endings = ["None", "CR", "LF", "Both CR&LF"]
        self.line_endings_optionmenu = CTkOptionMenu(
            serial_port_frame, values=line_endings)
        self.line_endings_optionmenu.pack(side="left", padx=10, pady=10)

        separator_1 = ttk.Separator(self.settings_frame, orient="horizontal")
        separator_1.pack(fill="x", padx=10, pady=5)

        # Frame for appearance settings
        appearance_frame = CTkFrame(self.settings_frame)
        appearance_frame.pack(fill="x", padx=10, pady=5)

        appearance_label = CTkLabel(appearance_frame, text="Appearance")
        appearance_label.pack(side="left", padx=10, pady=10)

        self.appearance_optionmenu = CTkOptionMenu(
            appearance_frame, values=["Light", "Dark", "System"])
        self.appearance_optionmenu.pack(side="left", padx=10, pady=10)

        separator_2 = ttk.Separator(self.settings_frame, orient="horizontal")
        separator_2.pack(fill="x", padx=10, pady=5)

        # Frame for save folder settings
        save_folder_frame = CTkFrame(self.settings_frame)
        save_folder_frame.pack(fill="x", padx=10, pady=5)

        save_folder_label = CTkLabel(save_folder_frame, text="Save Location")
        save_folder_label.pack(side="left", padx=10, pady=10)

        self.save_folder_entry = CTkEntry(save_folder_frame)
        self.save_folder_entry.pack(
            side="left", fill="x", expand=True, padx=10, pady=10)

        self.selectFolder_button = CTkButton(
            save_folder_frame, text="Select Folder", command=self.selectFolder)
        self.selectFolder_button.pack(side="left", padx=10, pady=10)

        self.setCurrentSettings()

    def setCurrentSettings(self):
        self.serial_ports_optionmenu.set(self.settings_data.get('port'))
        self.baud_rates_optionmenu.set(self.settings_data.get('baudrate'))
        self.line_endings_optionmenu.set(self.settings_data.get('lineending'))
        self.appearance_optionmenu.set(self.settings_data.get('appearance'))
        self.save_folder_entry.delete(0, "end")
        self.save_folder_entry.insert(0, self.settings_data.get('save_folder'))

    def refreshSerialPorts(self, serial_ports_optionmenu):
        # refresh available serial ports and cameras every 1 second
        myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        self.ports_list = sorted([p[0] for p in myports])
        serial_ports_optionmenu.configure(values=self.ports_list)
        self.after(1000, self.refreshSerialPorts, serial_ports_optionmenu)

    # def changeAppearanceMode(self, new_appearance_mode: str):
    #     set_appearance_mode(new_appearance_mode)

    def applySettings(self):

        # get serial port, baud rate and line ending
        serial_port = self.serial_ports_optionmenu.get()
        baud_rate = self.baud_rates_optionmenu.get()
        line_ending = self.line_endings_optionmenu.get()

        # change appearance mode
        appearance = self.appearance_optionmenu.get()

        # save settings to json file
        settings_data = {}
        settings_data['lineending'] = line_ending
        settings_data['baudrate'] = baud_rate
        settings_data['port'] = serial_port
        settings_data['portlist'] = self.ports_list
        settings_data['appearance'] = appearance
        settings_data['save_folder'] = self.save_folder_entry.get()
        with open('settings.json', 'w') as jfile:
            json.dump(settings_data, jfile, indent=4)
            jfile.close()
        self.master.updateSettings(settings_data)

    def applyAndReturn(self):
        # apply changes and return to home tab
        self.applySettings()
        self.master.showTab("Home")

    def revertSettings(self):
        # cancel changes and return to home tab
        # self.setCurrentSettings()
        self.master.showTab("Home")

    def selectFolder(self):
        folder = filedialog.askdirectory()
        self.save_folder_entry.delete(0, "end")
        self.save_folder_entry.insert(0, folder)
