from customtkinter import *


class DeviceControl(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        self.spinbox = Spinbox(self, label='Setpoint',
                               min_value=0, max_value=100)
        self.spinbox.grid(row=0, column=0)


class Spinbox(CTkFrame):
    def __init__(self, *args,
                 label: str = "Spinbox",
                 step_size: float = 1,
                 decimal_places: int = 0,
                 min_value, max_value,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.step_size = step_size
        self.min_value = min_value
        self.max_value = max_value
        self.decimal_places = decimal_places

        self.grid_columnconfigure((0, 1, 3), weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1), weight=0)

        validation = self.register(self.only_numbers)

        self.label = CTkLabel(self, text=label)
        self.label.grid(row=0, column=0, rowspan=2, padx=3, pady=3)

        self.entrybox = CTkEntry(
            self, width=50, border_width=0, validate="key", validatecommand=(validation, '%P'))
        self.entrybox.grid(row=0, column=1, rowspan=2,
                           padx=3, pady=3, sticky="nsew")

        increment_button_height = self.entrybox.winfo_reqheight() - 5

        self.add_button = CTkButton(self, text="+", width=increment_button_height, height=increment_button_height,
                                    command=lambda: self.increment_callback('add'))
        self.add_button.grid(row=0, column=2)

        self.subtract_button = CTkButton(self, text="-", width=increment_button_height, height=increment_button_height,
                                         command=lambda: self.increment_callback('subtract'))
        self.subtract_button.grid(row=1, column=2)

        # default value
        self.entrybox.insert(0, "0")
        # Bind all elements on mousewheel and keyboard events
        self.entrybox.bind("<MouseWheel>", self.on_mouse_wheel)
        self.subtract_button.bind("<MouseWheel>", self.on_mouse_wheel)
        self.add_button.bind("<MouseWheel>", self.on_mouse_wheel)
        self.bind("<MouseWheel>", self.on_mouse_wheel)

        self.entrybox.bind("<Up>", lambda e: self.increment_callback('add'))
        self.entrybox.bind(
            "<Down>", lambda e: self.increment_callback('subtract'))
        self.entrybox.bind("<FocusOut>", self.focusOutEvent)
        self.entrybox.bind("<Return>", lambda event: self.focus_set())

    def increment_callback(self, operation: str = "add"):
        try:
            if operation == "add":
                value = float(self.entrybox.get()) + self.step_size
            if operation == "subtract":
                value = float(self.entrybox.get()) - self.step_size
            value = self.constrain(value, self.min_value, self.max_value)
            self.set(value)
        except ValueError:
            return

    def on_mouse_wheel(self, event):
        if event.delta > 0:
            self.increment_callback('add')
        else:
            self.increment_callback('subtract')

    # def set(self, value: float):
    #     self.entrybox.delete(0, "end")
    #     str_value = f"{value:.{self.decimal_places}}"
    #     self.entrybox.insert(0, str_value)

    def set(self, value):
        self.entrybox.delete(0, "end")
        if isinstance(value, (int, float)):
            # Format the value explicitly without scientific notation
            str_value = "{:.{}f}".format(value, self.decimal_places)
            self.entrybox.insert(0, str_value)
        else:
            # Handle non-numeric values (maybe display an error message?)
            print("Error: Value must be numeric")

    def only_numbers(self, char):
        def is_float(char):
            try:
                float(char)
                return True
            except ValueError:
                return False

        # Validate true for only numbers
        if (is_float(char) or char == ""):
            return True
        else:
            return False

    def constrain(self, value, min_value, max_value):
        if value < min_value:
            return min_value
        elif value > max_value:
            return max_value
        else:
            return value

    def focusOutEvent(self, event):
        self.set(self.constrain(float(self.entrybox.get()),
                 self.min_value, self.max_value))

    def get(self):
        return self.entrybox.get()
