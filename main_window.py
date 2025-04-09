import qrcode.image.pil
from main_window_layout import MainWindowLayout
import os
import tkinter
import qrcode
import io
import qrcode.image.svg
from PIL import Image
from fsutils import QR_CODES_DIR, make_sure_directory_exists

class MainWindow:
    def __init__(self, app):
        self.logo_buffer: io.BytesIO = io.BytesIO()
        self.img_buffer: io.BytesIO = io.BytesIO()

        self.app = app
        self.layout = MainWindowLayout(self)
        self.layout.build()
        self.layout.content_box.insert("end-1c", "temp")
        self.update_ui()


    # Generates the QR Code and saves it. Gets called when you press on "Generate" 
    def create_qr(self, mode=""):
        qr = qrcode.QRCode(
                version=round(self.layout.version_slider.get()),    # Gets values of sliders and error correction
                box_size=round(self.get_boxsize()),
                border=round(self.layout.border_slider.get()),
                error_correction=self.get_error_correction()
        )

        data = self.layout.content_box.get("1.0","end-1c")

        if len(data.strip()) == 0:
            data = "temp"
        
        # Gets content from row 1 idex 0 up to the end but deletes the last character (-1c) because using "end" always adds a linebreak at the end
        qr.add_data(data) 

        if mode == "temp": # If mode == "temp", save image to temp folder for use in the preview window
            self.img_buffer = io.BytesIO()

            if self.layout.logo_checkbox.get() == 1: # generates qr code and adds logo if enabled
                if self.layout.filetype_box.get() == ".jpg": img = qr.make_image(back_color=self.layout.background_color_box.get(),fill_color=self.layout.fill_color_box.get()).convert("RGB") # Converts to RGB without transparency as .jpg doenst support it
                else: img = qr.make_image(back_color=self.layout.background_color_box.get(),fill_color=self.layout.fill_color_box.get()).convert("RGBA")
                img = img.resize((400,400))

                try:
                    logo = Image.open(self.logo_buffer).convert("RGBA")
                    logo = logo.resize((x:=20 * round(self.layout.logosize_slider.get()),y:= 20 * round(self.layout.logosize_slider.get())))
                    img.paste(logo, (200 - int(x/2),200 - int(y/2)),logo)
                except:
                    MainWindow.__print_invalid_logo_error()

                img.save(self.img_buffer, format="PNG")
            else: # just generates qr code without adding the logo if disabled
                img = qr.make_image(back_color=self.layout.background_color_box.get(),fill_color=self.layout.fill_color_box.get())
                img = img.resize((400,400))
                img.save(self.img_buffer, format="PNG")
    
        elif self.layout.logo_checkbox.get() == 1: # checks if logo addition is enabled
            if self.layout.filetype_box.get() == ".jpg": img = qr.make_image(back_color=self.layout.background_color_box.get(),fill_color=self.layout.fill_color_box.get()).convert("RGB") # Converts to RGB without transparency as .jpg doenst support it
            else: img = qr.make_image(back_color=self.layout.background_color_box.get(),fill_color=self.layout.fill_color_box.get()).convert("RGBA")
            img = img.resize((2000,2000))

            try:
                logo = Image.open(self.logo_buffer).convert("RGBA")
                logo = logo.resize((x:=100 * round(self.layout.logosize_slider.get()),y:= 100 * round(self.layout.logosize_slider.get())))
                img.paste(logo, (1000 - int(x/2),1000 - int(y/2)),logo)
            except:
                MainWindow.__print_invalid_logo_error()

            return img

        elif self.layout.filetype_box.get() == ".svg":
            return qr.make_image(image_factory=qrcode.image.svg.SvgImage) # Use svg imagefactory if selected
        else: 
            return qr.make_image(back_color=self.layout.background_color_box.get(),fill_color=self.layout.fill_color_box.get())


    def create_and_save_qr(self):
        make_sure_directory_exists(QR_CODES_DIR)
        img = self.create_qr()
        img.save(f"{QR_CODES_DIR}/{self.layout.filename_box.get()}{self.layout.filetype_box.get()}") # Saves with chosen name and file extension


    @staticmethod
    def __print_invalid_logo_error():
        print("Error: invalid logo file")


    def get_boxsize(self):
        if self.layout.logo_checkbox == 1:
            return 100
        else:
            return self.layout.boxsize_slider.get()


    # Returns selected Error Correction Level. Gets called when Generating a QR Code
    def get_error_correction(self):
        if self.layout.error_corection_box.get()=="L (7%)":
            return qrcode.constants.ERROR_CORRECT_L
        elif self.layout.error_corection_box.get()=="M (15%)":
            return qrcode.constants.ERROR_CORRECT_M
        elif self.layout.error_corection_box.get()=="Q (25%)":
            return qrcode.constants.ERROR_CORRECT_Q
        elif self.layout.error_corection_box.get()=="H (30%)":
            return qrcode.constants.ERROR_CORRECT_H
        else: return qrcode.constants.ERROR_CORRECT_M


    def select_logo(self): #Gets called when someone presses the "select logo" button
        logo_path = tkinter.filedialog.askopenfilename(title="Select a logo",
            initialdir="/",
            filetypes=(
                ("Image file", "*.png"),
                ("Image file", "*.jpg"),
                ("Image file", "*.webp"),
                ("All files", "*.*")
                )
            )

        self.logo_buffer = io.BytesIO()
        logo = Image.open(logo_path)
        logo.save(self.logo_buffer, logo.format)
        self.update_ui()


    def open_folder(self):
        make_sure_directory_exists(QR_CODES_DIR)
        os.startfile(QR_CODES_DIR)


    # Updates ui to represent current values. Gets called whenever a slider or combobox is changed
    def update_ui(self, _ = ""):
        if self.layout.logo_checkbox.get() == 1:
            self.layout.logo_select_button.place(relx=0.225, rely=0.965, anchor=tkinter.CENTER)
            self.layout.logosize_slider.place(relx=0.23, rely=0.92, anchor=tkinter.CENTER)
            self.layout.logosize_slider_label.place(relx=0.065, rely=0.92, anchor=tkinter.CENTER)
        else:
            self.layout.logo_select_button.place(relx=2, rely=0.965, anchor=tkinter.CENTER)
            self.layout.logosize_slider.place(relx=2, rely=0.92, anchor=tkinter.CENTER)
            self.layout.logosize_slider_label.place(relx=2, rely=0.92, anchor=tkinter.CENTER)       

        if self.layout.preview_checkbox.get() == 1:

            self.app.root.geometry("1200x600")
            self.layout.settings_frame.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)
            self.layout.preview_frame.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)
            self.create_qr("temp")
            self.layout.preview_image.configure(image= tkinter.PhotoImage(data=self.img_buffer.getvalue()))
        elif self.app.root.geometry != "600x600":
            self.app.root.geometry("600x600")
            self.layout.settings_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            self.layout.preview_frame.place(relx=2, anchor=tkinter.CENTER)

        if self.layout.logo_checkbox.get() == 1:
            self.layout.border_slider.configure(state="disabled",button_color="grey")
            self.layout.border_slider.set(4)
            self.layout.boxsize_slider.configure(state="disabled",button_color="grey")
            self.layout.error_corection_box.configure(values=["Q (25%)","H (30%)"])
            if (self.layout.error_corection_box.get() != "H (30%)") and (self.layout.error_corection_box.get() != "Q (25%)") : self.layout.error_corection_box.set("H (30%)")
            if self.layout.filetype_box.get() == ".svg":
                self.layout.filetype_box.set(".png")
        else:
            self.layout.border_slider.configure(state="normal",button_color=["#3a7ebf", "#1f538d"])
            self.layout.boxsize_slider.configure(state="normal",button_color=["#3a7ebf", "#1f538d"])
            self.layout.error_corection_box.configure(values=["L (7%)","M (15%)","Q (25%)","H (30%)"])

        if self.layout.background_color_box.get() == "transparent":
            if self.layout.filetype_box.get() == ".jpg": self.layout.filetype_box.set(".png")
            if self.layout.logo_checkbox.get() == 1:
                self.layout.filetype_box.configure(values=[".png",".webp"])
            else:
                self.layout.filetype_box.configure(values=[".png",".svg",".webp"])
        else:
            if self.layout.logo_checkbox.get() == 1:
                self.layout.filetype_box.configure(values=[".png",".jpg",".webp"])
            else:
                self.layout.filetype_box.configure(values=[".png",".jpg",".svg",".webp"])

        self.layout.version_slider_label.configure(text=f"Version ({round(self.layout.version_slider.get())})")
        self.layout.border_slider_label.configure(text=f"Bordersize ({round(self.layout.border_slider.get())})")
        self.layout.boxsize_slider_label.configure(text=f"Size ({round(self.layout.boxsize_slider.get())})")
        self.layout.logosize_slider_label.configure(text=f"Logosize ({round(self.layout.logosize_slider.get())})")
