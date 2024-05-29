import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time


class LivePlotApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Live Plot with Tkinter")
        self.geometry("800x600")

        # Create a figure and axis
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Create a canvas and add the figure to it
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Checkbox for start/pause
        self.plotting = tk.BooleanVar(value=True)
        self.checkbox = ttk.Checkbutton(
            self, text="Pause", variable=self.plotting, command=self.toggle_plotting)
        self.checkbox.pack(side=tk.TOP)

        # Initialize data
        self.x_data = []
        self.y_data = []
        self.start_time = time.time()
        self.paused_time = 0

        # Start updating the plot
        self.update_plot()

    def toggle_plotting(self):
        if self.plotting.get():
            self.checkbox.config(text="Pause")
            # Adjust start time to account for the pause duration
            self.start_time += time.time() - self.paused_time
        else:
            self.checkbox.config(text="Start")
            self.paused_time = time.time()

    def update_plot(self):
        if self.plotting.get():
            # Update data
            current_time = time.time() - self.start_time
            self.x_data.append(current_time)
            self.y_data.append(np.sin(current_time))

            # Clear the axis and replot
            self.ax.clear()
            self.ax.plot(self.x_data, self.y_data, label="Sine Wave")
            self.ax.set_title("Live Updating Plot")
            self.ax.set_xlabel("Time (s)")
            self.ax.set_ylabel("Value")
            self.ax.legend()

            # Draw the canvas
            self.canvas.draw()

        # Call this function again after 100 milliseconds
        self.after(10, self.update_plot)


if __name__ == "__main__":
    app = LivePlotApp()
    app.mainloop()
