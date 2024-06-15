from customtkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)  # type: ignore
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.widgets import SpanSelector
from matplotlib.backend_bases import key_press_handler
from matplotlib import gridspec
import numpy as np
from PIL import Image
import tkinter.ttk as ttk
import tkinter.filedialog as fd


class DataDisplay(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        icons_folder_path = master.getIconsFolderPath()

        # Load icons
        button_padding = 5
        button_width = 90
        button_height = 35
        icon_size = (button_height, button_height)

        save_file_icon = CTkImage(light_image=Image.open(os.path.join(icons_folder_path, "save_light.png")),
                                  dark_image=Image.open(os.path.join(
                                      icons_folder_path, "save_dark.png")),
                                  size=icon_size)
        export_image_icon = CTkImage(light_image=Image.open(os.path.join(icons_folder_path, "export_image_light.png")),
                                     dark_image=Image.open(os.path.join(
                                         icons_folder_path, "export_image_dark.png")),
                                     size=icon_size)
        load_file_icon = CTkImage(light_image=Image.open(os.path.join(icons_folder_path, "open_light.png")),
                                  dark_image=Image.open(os.path.join(
                                      icons_folder_path, "open_dark.png")),
                                  size=icon_size)
        clear_plot_icon = CTkImage(light_image=Image.open(os.path.join(icons_folder_path, "clear_plot_light.png")),
                                   dark_image=Image.open(os.path.join(
                                       icons_folder_path, "clear_plot_dark.png")),
                                   size=icon_size)

        # Create frames
        toolbar_frame = CTkFrame(self)
        toolbar_frame.pack(fill="both", expand=False)

        plot_frame = CTkFrame(self)
        plot_frame.pack(fill="both", expand=True)

        # Create toolbar buttons
        self.start_data_log_var = StringVar(value="Off")
        self.start_data_log_switch = CTkSwitch(
            master=toolbar_frame, text="Data Stream", command=self.startDataStream, variable=self.start_data_log_var, onvalue="On", offvalue="Off")
        self.start_data_log_switch.pack(
            side='left', expand=False, padx=button_padding, pady=(0, button_padding))

        separator1 = ttk.Separator(
            toolbar_frame, orient="vertical")
        separator1.pack(side='left', expand=False,
                        padx=button_padding, pady=(0, button_padding))

        self.save_file_button = CTkButton(
            master=toolbar_frame, text="Save", image=save_file_icon, command=self.saveFile, width=button_width, height=button_height)
        self.save_file_button.pack(
            side='left', expand=False, padx=button_padding, pady=(0, button_padding))

        self.load_file_button = CTkButton(
            master=toolbar_frame, text="Open", image=load_file_icon, command=self.loadFile, width=button_width, height=button_height)
        self.load_file_button.pack(
            side='left', expand=False, padx=button_padding, pady=(0, button_padding))

        separator2 = ttk.Separator(
            toolbar_frame, orient="vertical")
        separator2.pack(side='left', expand=False,
                        padx=button_padding, pady=(0, button_padding))

        self.export_image_button = CTkButton(
            master=toolbar_frame, text="Export\nImage", image=export_image_icon, command=self.exportGraphImage, width=button_width, height=button_height)
        self.export_image_button.pack(
            side='left', expand=False, padx=button_padding, pady=(0, button_padding))

        separator3 = ttk.Separator(
            toolbar_frame, orient="vertical")
        separator3.pack(side='left', expand=False,
                        padx=button_padding, pady=(0, button_padding))

        self.clear_plot_button = CTkButton(
            master=toolbar_frame, text="Clear", image=clear_plot_icon, command=self.clearPlot, width=button_width, height=button_height)
        self.clear_plot_button.pack(
            side='left', expand=False, padx=button_padding, pady=(0, button_padding))

        # Create a figure and axis
        self.figure = Figure(figsize=(4, 2), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.line_plot, = self.ax.plot([], [])

        self.canvas = FigureCanvasTkAgg(self.figure, master=plot_frame)
        self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True)
        # self.canvas.draw()

    def startDataStream(self):
        pass

    def saveFile(self):
        pass

    def loadFile(self):
        pass

    def exportGraphImage(self):
        save_filepath = fd.asksaveasfilename(
            initialdir=f"{self.save_folder}/", title="Select a file", filetypes=(("PNG files", ".png"), ("PDF files", ".pdf"), ("SVG files", ".svg"), ("EPS files", ".eps")), defaultextension="*.*")
        if save_filepath:
            self.fig.savefig(save_filepath, dpi=400, transparent=False,
                             facecolor=self.fig.get_facecolor(), edgecolor='none')

    def clearPlot(self):
        pass

    def updateSaveFolder(self, save_folder_path):
        self.save_folder_path = save_folder_path

    def updateTheme(self, color_palette: dict):
        self.figure.set_facecolor(color_palette["bg"])
        self.ax.set_facecolor(color_palette["bg"])
        self.ax.tick_params(axis='x', colors=color_palette["fg"], labelsize=11)
        self.ax.tick_params(axis='y', colors=color_palette["fg"], labelsize=11)
        self.ax.xaxis.label.set_color(color_palette["fg"])
        self.ax.spines['bottom'].set_color(color_palette["fg"])
        self.ax.spines['top'].set_color(color_palette["fg"])
        self.ax.spines['right'].set_color(color_palette["fg"])
        self.ax.spines['left'].set_color(color_palette["fg"])
        self.ax.set_xlabel("Time (s)", fontsize=12, color=color_palette["fg"])
        self.ax.set_ylabel("Flow Rate (sccm)", fontsize=12,
                           color=color_palette["fg"])

        self.figure.canvas.draw_idle()

    def configureButtons(self, buttons: tuple, state: str):
        pass

    #     # Checkbox to start/pause data Stream
    #     self.plotting = BooleanVar(value=False)
    #     self.checkbox = CTkCheckBox(
    #         self, text="Start Data Log", variable=self.plotting, command=self.toggle_plotting)
    #     self.checkbox.grid(row=0, column=0)

    #     # Create a figure and axis
    #     self.figure = Figure(figsize=(4, 3), dpi=100)
    #     self.ax = self.figure.add_subplot(111)

    #     # Create a canvas and add the figure to it
    #     self.canvas = FigureCanvasTkAgg(self.figure, master=self)
    #     self.canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")

    #     # Initialize data
    #     self.x_data = []
    #     self.y_data = []
    #     self.start_time = time.time()
    #     self.paused_time = 0

    #     # Start updating the plot
    #     self.update_plot()

    # def toggle_plotting(self):
    #     if self.plotting.get():
    #         # self.checkbox.configure(text="Pause")
    #         # Adjust start time to account for the pause duration
    #         self.start_time += time.time() - self.paused_time
    #     else:
    #         # self.checkbox.configure(text="Start")
    #         self.paused_time = time.time()

    # def update_plot(self):
    #     if self.plotting.get():
    #         # Update data
    #         current_time = time.time() - self.start_time
    #         self.x_data.append(current_time)
    #         self.y_data.append(np.sin(current_time))

    #         # Clear the axis and replot
    #         self.ax.clear()
    #         self.ax.plot(self.x_data, self.y_data, label="Sine Wave")
    #         self.ax.set_title("Live Updating Plot")
    #         self.ax.set_xlabel("Time (s)")
    #         self.ax.set_ylabel("Value")
    #         self.ax.legend()

    #         # Draw the canvas
    #         self.canvas.draw()

    #     # Call this function again after 10 milliseconds
    #     self.after(10, self.update_plot)
