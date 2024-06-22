from customtkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.widgets import SpanSelector
from matplotlib.backend_bases import key_press_handler
from matplotlib import gridspec
import numpy as np
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import time


class DataDisplay(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.icons_folder_path = master.getIconsFolderPath()

        self.createToolbarFrame()
        self.createPlotFrame()

    def createToolbarFrame(self):
        # Create frame
        toolbar_frame = CTkFrame(self)
        toolbar_frame.pack(fill="x", expand=False)

        # Define button properties
        button_padding = 5
        button_width = 90
        button_height = 35

        # Create toolbar buttons
        self.start_data_log_var = StringVar(value="Off")
        self.start_data_log_switch = CTkSwitch(
            master=toolbar_frame, text="Data Stream", command=self.togglePlotting, variable=self.start_data_log_var, onvalue="On", offvalue="Off")
        self.start_data_log_switch.pack(
            side='left', expand=False, padx=button_padding, pady=(0, button_padding))

        self.addSeparator(
            parent=toolbar_frame, padding=button_padding)

        self.save_file_button = self.createButton(toolbar_frame, "Save",
                                                  "save", button_width, button_height, button_padding, self.saveFile)

        self.load_file_button = self.createButton(toolbar_frame, "Open",
                                                  "open", button_width, button_height, button_padding, self.loadFile)

        self.addSeparator(
            parent=toolbar_frame, padding=button_padding)

        self.export_image_button = self.createButton(
            toolbar_frame, "Export\nImage", "export_image", button_width, button_height, button_padding, self.exportGraphImage)

        self.addSeparator(
            parent=toolbar_frame, padding=button_padding)

        self.clear_plot_button = self.createButton(
            toolbar_frame, "Clear", "clear_plot", button_width, button_height, button_padding, self.clearPlot)

    def createPlotFrame(self):
        # Create frame
        plot_frame = CTkFrame(self)
        plot_frame.pack(fill="both", expand=True)

        # Create figure, canvas and axis
        # self.canvas = CTkCanvas(plot_frame)
        # self.canvas.pack(fill='both', expand=True)
        # self.canvas.configure(borderwidth=0, highlightthickness=0)

        self.figure = Figure(dpi=100)
        self.ax = self.figure.add_subplot(111)
        # self.line_plot, = self.ax.plot(self.x_data, self.y_data)

        self.canvas = FigureCanvasTkAgg(self.figure, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        # Initialize data
        self.x_data = []
        self.y_data = []
        self.start_time = time.time()
        self.paused_time = 0

        # start the plot
        self.updatePlot()

        # self.figure.tight_layout()
        self.figure.subplots_adjust(
            left=0.05, right=0.99, top=0.99, bottom=0.1)

    def startDataStream(self):
        pass

    def saveFile(self):
        pass

    def loadFile(self):
        pass

    def exportGraphImage(self):
        save_filepath = fd.asksaveasfilename(
            initialdir=f"{self.save_folder_path}/", title="Select a file", filetypes=(("PNG files", ".png"), ("PDF files", ".pdf"), ("SVG files", ".svg"), ("EPS files", ".eps")), defaultextension="*.*")
        if save_filepath:
            self.figure.savefig(save_filepath, dpi=400, transparent=False,
                                facecolor=self.figure.get_facecolor(), edgecolor='none')

    def clearPlot(self):
        pass

    def updateSaveFolder(self, save_folder_path):
        self.save_folder_path = save_folder_path

    def updateTheme(self, color_palette: dict):
        self.figure.set_facecolor(color_palette["bg"])
        self.ax.set_facecolor(color_palette["bg"])
        self.ax.tick_params(axis='x', colors=color_palette["fg"], labelsize=9)
        self.ax.tick_params(axis='y', colors=color_palette["fg"], labelsize=9)
        self.ax.xaxis.label.set_color(color_palette["fg"])
        self.ax.spines['bottom'].set_color(color_palette["fg"])
        self.ax.spines['top'].set_color(color_palette["fg"])
        self.ax.spines['right'].set_color(color_palette["fg"])
        self.ax.spines['left'].set_color(color_palette["fg"])
        # self.ax.set_xlabel("Time (s)", fontsize=12, color=color_palette["fg"])
        # self.ax.set_ylabel("Flow Rate (sccm)", fontsize=12,
        #                    color=color_palette["fg"])

        self.figure.canvas.draw_idle()

    def configureButtons(self, buttons: tuple, state: str):
        pass

    def loadIcon(self, name, size):
        """Load an icon from the icons folder, handle file not found errors."""
        try:
            light_image_path = os.path.join(
                self.icons_folder_path, f"{name}_light.png")
            dark_image_path = os.path.join(
                self.icons_folder_path, f"{name}_dark.png")

            if not os.path.isfile(light_image_path):
                raise FileNotFoundError(
                    f"Light icon '{name}_light.png' not found in '{self.icons_folder_path}'")
            if not os.path.isfile(dark_image_path):
                raise FileNotFoundError(
                    f"Dark icon '{name}_dark.png' not found in '{self.icons_folder_path}'")

            light_image = Image.open(light_image_path)
            dark_image = Image.open(dark_image_path)
        except FileNotFoundError as e:
            print(e)  # Log the error for debugging

            # Fallback to a default icon or a transparent image
            light_image = self.default_icon(size)
            dark_image = self.default_icon(size)

        return CTkImage(light_image=light_image, dark_image=dark_image, size=size)

    def default_icon(self, size):
        """Create a default transparent icon or placeholder."""
        return Image.new('RGBA', size, (255, 0, 0, 0))  # Creates a transparent image

    def createButton(self, parent, text, icon_name, width, height, padding, command):
        icon = self.loadIcon(icon_name, (height, height))
        button = CTkButton(
            master=parent, text=text, image=icon, command=command,
            width=width, height=height
        )
        button.pack(side='left', expand=False, padx=padding, pady=(0, padding))
        return button

    def addSeparator(self, parent, padding):
        # Add a vertical separator to the toolbar
        separator = ttk.Separator(parent, orient="vertical")
        separator.pack(side='left', fill='y', padx=padding)

    def togglePlotting(self):
        if self.start_data_log_var.get() == "On":
            # self.checkbox.configure(text="Pause")
            # Adjust start time to account for the pause duration
            self.start_time += time.time() - self.paused_time
        else:
            # self.checkbox.configure(text="Start")
            self.paused_time = time.time()

    def updatePlot(self):
        if self.start_data_log_var.get() == "On":
            # Update data
            current_time = time.time() - self.start_time
            self.x_data.append(current_time)
            self.y_data.append(np.sin(current_time))

            # Clear the axis and replot
            self.ax.clear()
            self.ax.plot(self.x_data, self.y_data, label="Sine Wave")
            self.ax.legend()

            # Draw the canvas
            self.canvas.draw()

        # Call this function again after 10 milliseconds
        self.after(10, self.updatePlot)
