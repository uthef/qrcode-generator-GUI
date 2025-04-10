import customtkinter
import tkinter
from pathlib import Path
from main_window import MainWindow

class Application:
    def __init__(self):
        self.version = "0.0.2"

        # customtkinter setup
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("960x600")
        self.root.title(f"QR Code Generator v{self.version}")
        self.root.resizable(False,False)

        if Path("icon.png").is_file():
            self.root.iconphoto(False, tkinter.PhotoImage(file='icon.png'))

        self.__window = MainWindow(self)
    

    def run(self):
        self.root.mainloop()
