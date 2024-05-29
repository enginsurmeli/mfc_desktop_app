import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time


class DataDisplay(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
