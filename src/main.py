import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        # configure window
        self.title("FlowFusion 1.0")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
