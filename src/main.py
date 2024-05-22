import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter")
        self.geometry("400x400")
        self.label = customtkinter.CTkLabel(self, text="Hello, World!")
        self.label.pack(pady=10)
        self.button = customtkinter.CTkButton(
            self, text="Click Me", command=self.on_click)
        self.button.pack(pady=10)

    def on_click(self):
        self.label.configure(text="Button Clicked!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
