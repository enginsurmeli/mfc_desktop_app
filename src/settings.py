from customtkinter import *
import serial.tools.list_ports
import tkinter.ttk as ttk
from tkinter import filedialog
import json


class SettingsFrame(CTkFrame):
    def __init__(self, parent, master):
        super().__init__(master)

        self.parent = parent

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2, 3), weight=0)

        self.ok_button = CTkButton(
            self, text="OK", command=self.applyAndReturn, width=80, state="disabled")
        self.ok_button.grid(row=1, column=1, padx=0, pady=(0, 10))

        self.cancel_button = CTkButton(
            self, text="Cancel", command=self.revertSettings, width=80)
        self.cancel_button.grid(row=1, column=2, padx=10, pady=(0, 10))

        self.apply_button = CTkButton(
            self, text="Apply", command=self.saveSettingsandApply, width=80, state="disabled")
        self.apply_button.grid(row=1, column=3, padx=(0, 10), pady=(0, 10))
        # TODO: activate apply button onlt if changes are made

        # Dictionary to store option menus and their initial values
        self.option_menus = {}
        self.option_menu_values = {}

        self.settings_frame = CTkFrame(self)
        self.settings_frame.grid(
            row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Frame for serial port settings
        serial_port_frame = CTkFrame(self.settings_frame)
        serial_port_frame.pack(fill="x", padx=10, pady=5)

        serial_port_label = CTkLabel(serial_port_frame, text="Serial Port")
        serial_port_label.pack(side="left", padx=10, pady=10)

        self.serial_ports_var = StringVar()
        self.serial_ports_optionmenu = CTkOptionMenu(
            serial_port_frame, variable=self.serial_ports_var, values=[], dynamic_resizing=False)
        # refresh serial ports once at start
        self.refreshSerialPorts(self.serial_ports_optionmenu)
        self.serial_ports_optionmenu.pack(side="left", padx=10, pady=10)
        self.serial_ports_var.trace_add(
            "write", lambda name, index, mode: self.onValueChange("Serial Port"))

        baud_rates = ["9600", "19200", "38400", "57600", "115200"]
        self.baud_rates_var = StringVar()
        self.baud_rates_optionmenu = CTkOptionMenu(
            serial_port_frame, variable=self.baud_rates_var, values=baud_rates)
        self.baud_rates_optionmenu.pack(side="left", padx=10, pady=10)
        self.baud_rates_var.trace_add(
            "write", lambda name, index, mode: self.onValueChange("Baud Rate"))

        line_endings = ["None", "CR", "LF", "Both CR&LF"]
        self.line_endings_optionmenu = CTkOptionMenu(
            serial_port_frame, values=line_endings)
        self.line_endings_optionmenu.pack(side="left", padx=10, pady=10)

        refresh_serial_ports_button = CTkButton(
            serial_port_frame, text="⟳", width=30, font=("", 20), anchor="center", command=lambda: self.refreshSerialPorts(self.serial_ports_optionmenu))
        refresh_serial_ports_button.pack(side="left", padx=10, pady=10)

        separator_1 = ttk.Separator(self.settings_frame, orient="horizontal")
        separator_1.pack(fill="x", padx=10, pady=5)

        # Frame for appearance settings
        appearance_frame = CTkFrame(self.settings_frame)
        appearance_frame.pack(fill="x", padx=10, pady=5)

        appearance_label = CTkLabel(appearance_frame, text="Appearance")
        appearance_label.pack(side="left", padx=10, pady=10)

        self.appearance_optionmenu = CTkOptionMenu(
            appearance_frame, values=["Light", "Dark"])
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

        # Store the option menu and its initial value
        self.option_menus["Serial Port"] = self.serial_ports_optionmenu
        self.option_menu_values["Serial Port"] = self.serial_ports_var.get()
        self.option_menus["Baud Rate"] = self.baud_rates_optionmenu
        self.option_menu_values["Baud Rate"] = self.baud_rates_var.get()

        self.setCurrentSettings()

    def setCurrentSettings(self):
        settings_data = self.parent.getSettingsData()
        self.serial_ports_optionmenu.set(settings_data.get('port'))
        self.baud_rates_optionmenu.set(settings_data.get('baudrate'))
        self.line_endings_optionmenu.set(settings_data.get('lineending'))
        self.appearance_optionmenu.set(settings_data.get('appearance'))
        self.save_folder_entry.delete(0, "end")
        self.save_folder_entry.insert(0, settings_data.get('save_folder'))

    def refreshSerialPorts(self, serial_ports_optionmenu):
        # refresh available serial ports and cameras every 1 second
        myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        self.ports_list = sorted([p[0] for p in myports])
        serial_ports_optionmenu.configure(values=self.ports_list)
        # self.after(1000, self.refreshSerialPorts, serial_ports_optionmenu)

    # def changeAppearanceMode(self, new_appearance_mode: str):
    #     set_appearance_mode(new_appearance_mode)

    def saveSettingsandApply(self):

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
        self.parent.applySettings(settings_data)

    def applyAndReturn(self):
        # apply changes and return to home tab
        self.saveSettingsandApply()
        self.parent.showTab("Home")

    def revertSettings(self):
        # cancel changes and return to home tab
        self.setCurrentSettings()
        self.parent.showTab("Home")

    def selectFolder(self):
        folder = filedialog.askdirectory()
        self.save_folder_entry.delete(0, "end")
        self.save_folder_entry.insert(0, folder)

    def onValueChange(self, key: str):
        # detect changes in option menus to activate OK and Apply buttons
        option_menu = self.option_menus[key]
        current_value = option_menu.get()

        if current_value != self.option_menu_values[key]:
            self.ok_button.configure(state="normal")
            self.apply_button.configure(state="normal")
