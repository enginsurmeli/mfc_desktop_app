from customtkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time


class DataDisplay(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Create grid layout
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    #     # Checkbox to start/pause data logging
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
