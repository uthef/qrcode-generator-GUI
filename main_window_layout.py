import tkinter
from customtkinter import CTkFrame, CTkLabel, CTkTextbox, CTkComboBox, CTkEntry, CTkSlider, CTkButton, CTkCheckBox


class MainWindowLayout:
    def __init__(self, window):
        self.__window = window
        self.__root = window.app.root


    def __update_ui_action(self, _ = ""):
        self.__window.update_ui()


    def __select_logo_action(self):
        self.__window.select_logo()

    
    def __create_and_save_qr_action(self):
        self.__window.create_and_save_qr();

    
    def __open_folder_action(self):
        self.__window.open_folder()


    def build(self):
        ## GUI Elements. All are structured very similar

        # Settings Frame
        self.settings_frame = CTkFrame(master=self.__root,
                                            width=600,
                                            height=600,
                                            border_width=0,
                                            corner_radius=0)
        self.settings_frame.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

        # Filename Entrybox + Label
        self.filename_box = CTkEntry(master=self.settings_frame,
                                            width=450,
                                            height=20,
                                            border_width=2,
                                            corner_radius=10)
        self.filename_box.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.filename_box.insert(0,"qr-code")

        self.filename_box_label = CTkLabel(master=self.settings_frame,
                                            text="Filename",
                                            width=100,
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.filename_box_label.place(relx=0.175, rely=0.060, anchor=tkinter.CENTER)

        # Content Textbox + Label
        self.content_box = CTkTextbox(master=self.settings_frame,
                                            width=450,
                                            height=200,
                                            border_width=2,
                                            corner_radius=10)
        self.content_box.place(relx=0.5, rely=0.335, anchor=tkinter.CENTER)

        self.content_box.bind("<Key>", self.__update_ui_action)

        self.content_box_label = CTkLabel(master=self.settings_frame,
                                            text="Content",
                                            width=100,
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.content_box_label.place(relx=0.170, rely=0.15, anchor=tkinter.CENTER)

        # Advanced Options Frame + Label
        self.advanced_options = CTkFrame(master=self.settings_frame,
                                            width=450,
                                            height=150,
                                            border_width=2,
                                            corner_radius=10)
        self.advanced_options.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.advanced_options_label = CTkLabel(master=self.settings_frame,
                                            text="Advanced Options",
                                            width=100,
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.advanced_options_label.place(relx=0.22, rely=0.55, anchor=tkinter.CENTER)

        # Filetype Combobox + Label
        self.filetype_box = CTkComboBox(master=self.advanced_options,
                                            width=70,
                                            height=20,
                                            values=[".png",".jpg",".svg",".webp"],
                                            state="readonly",
                                            command=self.__update_ui_action)
        self.filetype_box.place(relx=0.2, rely=0.27, anchor=tkinter.CENTER)
        self.filetype_box.set(".png")  # Sets initial value

        self.filetype_box_label = CTkLabel(master=self.advanced_options,
                                            text="File Extension",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.filetype_box_label.place(relx=0.2, rely=0.12, anchor=tkinter.CENTER)

        # Errorcorrection Combobox + Label
        self.error_corection_box = CTkComboBox(master=self.advanced_options,
                                            width=70,
                                            height=20,
                                            values=["L (7%)","M (15%)","Q (25%)","H (30%)"],
                                            state="readonly",
                                            command=self.__update_ui_action)
        self.error_corection_box.place(relx=0.4, rely=0.27, anchor=tkinter.CENTER)
        self.error_corection_box.set("M (15%)")  # Sets initial value

        self.filetype_box_label = CTkLabel(master=self.advanced_options,
                                            text="Error Correction",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.filetype_box_label.place(relx=0.4, rely=0.12, anchor=tkinter.CENTER)

        # Color Combobox # Label
        self.fill_color_box = CTkComboBox(master=self.advanced_options,
                                            width=70,
                                            height=20,
                                            values=["black","white","red","green", "blue", "yellow", "orange", "pink", "purple"],
                                            state="readonly",
                                            command=self.__update_ui_action)
        self.fill_color_box.place(relx=0.6, rely=0.27, anchor=tkinter.CENTER)
        self.fill_color_box.set("black")  # Sets initial value

        self.filetype_box_label = CTkLabel(master=self.advanced_options,
                                            text="Color",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.filetype_box_label.place(relx=0.6, rely=0.12, anchor=tkinter.CENTER)

        # Backgroundcolor Combobox + Slider
        self.background_color_box = CTkComboBox(master=self.advanced_options,
                                            width=70,
                                            height=20,
                                            values=["transparent","black","white","red","green", "blue", "yellow", "orange", "pink", "purple"],
                                            state="readonly",
                                            command=self.__update_ui_action)
        self.background_color_box.place(relx=0.8, rely=0.27, anchor=tkinter.CENTER)
        self.background_color_box.set("white")  # Sets initial value

        self.filetype_box_label = CTkLabel(master=self.advanced_options,
                                            text="Background Color",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.filetype_box_label.place(relx=0.8, rely=0.12, anchor=tkinter.CENTER)

        # Version Slider + Label
        self.version_slider = CTkSlider(master=self.advanced_options,
                                                width=320,
                                                height=20,
                                                from_=1,
                                                to=40,
                                                number_of_steps=40,
                                                command=self.__update_ui_action)
        self.version_slider.place(relx=0.6, rely=0.47, anchor=tkinter.CENTER)
        self.version_slider.set(1) # Sets initial value

        self.version_slider_label = CTkLabel(master=self.advanced_options,
                                            text=f"Version ({round(self.version_slider.get())})",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.version_slider_label.place(relx=0.125, rely=0.47, anchor=tkinter.CENTER)


        # Border Slider + Label
        self.border_slider = CTkSlider(master=self.advanced_options,
                                                width=320,
                                                height=20,
                                                from_=0,
                                                to=100,
                                                number_of_steps=101,
                                                command=self.__update_ui_action)
        self.border_slider.place(relx=0.6, rely=0.67, anchor=tkinter.CENTER)
        self.border_slider.set(4) # Sets initial value

        self.border_slider_label = CTkLabel(master=self.advanced_options,
                                            text=f"Border Size ({round(self.border_slider.get())})",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.border_slider_label.place(relx=0.125, rely=0.67, anchor=tkinter.CENTER)

        # Boxsize Slider + Label
        self.boxsize_slider = CTkSlider(master=self.advanced_options,
                                            width=320,
                                            height=20,
                                            from_=1,
                                            to=100,
                                            number_of_steps=100,
                                            command=self.__update_ui_action)
        self.boxsize_slider.place(relx=0.6, rely=0.87, anchor=tkinter.CENTER)
        self.boxsize_slider.set(10) # Sets initial value

        self.boxsize_slider_label = CTkLabel(master=self.advanced_options,
                                            text=f"Size ({round(self.boxsize_slider.get())})",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.boxsize_slider_label.place(relx=0.125, rely=0.87, anchor=tkinter.CENTER)

        # Preview Frame
        self.preview_frame = CTkFrame(master=self.__root,
                                        width=600,
                                        height=600,
                                        border_width=0,
                                        corner_radius=0)
        self.preview_frame.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

        # Preview Checkbox
        self.preview_checkbox = CTkCheckBox(master=self.settings_frame,
                                        width=100,
                                        height=20,
                                        text="Enable Preview",
                                        command=self.__update_ui_action)

        self.preview_checkbox.place(relx=0.45, rely=0.87, anchor=tkinter.CENTER)

        # Logo Checkbox
        self.logo_checkbox = CTkCheckBox(master=self.settings_frame,
                                        width=100,
                                        height=20,
                                        text="Enable Logo",
                                        command=self.__update_ui_action)

        self.logo_checkbox.place(relx=0.22, rely=0.87, anchor=tkinter.CENTER)

        # Logo Select Button

        self.logo_select_button = CTkButton(master=self.settings_frame,
                                        width=110,
                                        height=20,
                                        fg_color="#888888",
                                        hover_color="#666666",
                                        text="Change Logo",
                                        command=self.__select_logo_action)

        self.logo_select_button.place(relx=0.225, rely=0.965, anchor=tkinter.CENTER)

        # Logosize Slider + Label
        self.logosize_slider = CTkSlider(master=self.settings_frame,
                                            width=120,
                                            height=20,
                                            from_=1,
                                            to=10,
                                            number_of_steps=10,
                                            command=self.__update_ui_action)
        self.logosize_slider.place(relx=0.23, rely=0.92, anchor=tkinter.CENTER)
        self.logosize_slider.set(5) # Sets initial value

        self.logosize_slider_label = CTkLabel(master=self.settings_frame,
                                            text=f"Logosize ({round(self.logosize_slider.get())})",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.logosize_slider_label.place(relx=0.065, rely=0.92, anchor=tkinter.CENTER)

        # Save Button
        self.save_button = CTkButton(master=self.settings_frame,
                                            width=120,
                                            height=32,
                                            corner_radius=8,
                                            text="Save",
                                            command=self.__create_and_save_qr_action)
        self.save_button.place(relx=0.77, rely=0.88, anchor=tkinter.CENTER)


        # Open Folder Button
        self.open_folder_button = CTkButton(master=self.settings_frame,
                                            width=110,
                                            height=20,
                                            fg_color="#888888",
                                            hover_color="#666666",
                                            text="Open Folder",
                                            command=self.__open_folder_action)
        self.open_folder_button.place(relx=0.77, rely=0.94, anchor=tkinter.CENTER)
        
        self.preview_image = CTkLabel(master=self.preview_frame,
                                        width=400,
                                        height=400,
                                        corner_radius=0,
                                        text="")

        self.preview_image.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
