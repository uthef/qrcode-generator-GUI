from tkinter import *
from customtkinter import CTkFrame, CTkLabel, CTkTextbox, CTkComboBox, CTkEntry, CTkSlider, CTkButton, CTkCheckBox


GAP_Y = [16, 4]
 
class MainWindowLayout:
    def __init__(self, window):
        self.__window = window
        self.__root = window.app.root


    def __update_ui_action(self, e = ""):
        self.__window.update_ui(e)


    def __select_logo_action(self):
        self.__window.select_logo()

    
    def __create_and_save_qr_action(self):
        self.__window.create_and_save_qr();

    
    def __open_folder_action(self):
        self.__window.open_folder()


    def repack_main_frames(self, show_preview: bool):
        self.settings_frame.pack_forget()

        if show_preview:
            self.preview_frame.pack(anchor="e", side=RIGHT, expand=False, fill=Y)
        else:
            self.preview_frame.pack_forget()

        self.settings_frame.pack(anchor="w", padx=26, pady=26, fill=X)


    def set_logo_settings_visibility(self, value: bool):
        if value:
            self.logosize_slider_label.pack(anchor="nw", side=LEFT)
            self.logosize_slider.pack(anchor="nw")
            self.logo_select_button.pack(anchor="nw", side=LEFT, pady=[GAP_Y[0] / 2, 0], padx=[5, 0])
        else:
            self.logo_select_button.pack_forget()
            self.logosize_slider.pack_forget()
            self.logosize_slider_label.pack_forget()   


    def __build_advanced_settings(self):
        # Advanced Options Frame + Label
        self.advanced_options_label = CTkLabel(master=self.settings_frame,
                                            text="Advanced Options",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.advanced_options_label.pack(side=TOP, anchor="w", pady=GAP_Y)


        self.advanced_options = CTkFrame(master=self.settings_frame,
                                            border_width=2,
                                            corner_radius=10)

        self.advanced_options.pack(fill=X, ipadx=16, ipady=16)

        self.combo_boxes = CTkFrame(master=self.advanced_options, fg_color="transparent")
        self.combo_boxes.pack(pady=[16, 16])

        # Combobox containers
        self.box1 = CTkFrame(master=self.combo_boxes, fg_color="transparent")
        self.box1.pack(side=LEFT, padx=[4, 4])

        self.box2 = CTkFrame(master=self.combo_boxes, fg_color="transparent")
        self.box2.pack(side=LEFT, padx=[4, 4])

        self.box3 = CTkFrame(master=self.combo_boxes, fg_color="transparent")
        self.box3.pack(side=LEFT, padx=[4, 4])

        self.box4 = CTkFrame(master=self.combo_boxes, fg_color="transparent")
        self.box4.pack( padx=[4, 4])

        # Filetype Combobox + Label
        self.filetype_box_label = CTkLabel(master=self.box1,
                                            text="File Extension",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.filetype_box_label.pack()

        self.filetype_box = CTkComboBox(master=self.box1,
                                            height=20,
                                            width=90,
                                            values=[".png",".jpg",".svg",".webp"],
                                            state="readonly",
                                            command=self.__update_ui_action)
        self.filetype_box.pack()
        self.filetype_box.set(".png")  # Sets initial value

        # Errorcorrection Combobox + Label

        self.error_correction_box_label = CTkLabel(master=self.box2,
                                            text="Error Correction",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.error_correction_box_label.pack()

        self.error_corection_box = CTkComboBox(master=self.box2,
                                            height=20,
                                            width=90,
                                            values=["L (7%)","M (15%)","Q (25%)","H (30%)"],
                                            state="readonly",
                                            command=self.__update_ui_action)
        self.error_corection_box.pack()
        self.error_corection_box.set("M (15%)")  # Sets initial value

        # Color Combobox # Label

        self.fill_color_box_label = CTkLabel(master=self.box3,
                                            text="Color", 
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.fill_color_box_label.pack()

        self.fill_color_box = CTkComboBox(master=self.box3,
                                            width=90,
                                            height=20,
                                            values=["black","white","red","green", "blue", "yellow", "orange", "pink", "purple"],
                                            state="readonly",
                                            command=self.__update_ui_action)
        self.fill_color_box.pack()
        self.fill_color_box.set("black")  # Sets initial value

        # Backgroundcolor Combobox + Slider

        self.background_color_box_label = CTkLabel(master=self.box4,
                                            text="Background Color",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.background_color_box_label.pack()

        self.background_color_box = CTkComboBox(master=self.box4,
                                            width=120,
                                            height=20,
                                            values=["transparent","black","white","red","green", "blue", "yellow", "orange", "pink", "purple"],
                                            state="readonly",
                                            command=self.__update_ui_action)
        self.background_color_box.pack()
        self.background_color_box.set("white")  # Sets initial value

        # Slider grid
        self.slider_grid = CTkFrame(master=self.advanced_options, fg_color="transparent")
        self.slider_grid.pack()

        # Version Slider + Label
        self.version_slider = CTkSlider(master=self.slider_grid,
                                                width=320,
                                                height=20,
                                                from_=1,
                                                to=40,
                                                number_of_steps=40,
                                                command=self.__update_ui_action)
        self.version_slider.grid(column=1, row=0)
        self.version_slider.set(1) # Sets initial value

        self.version_slider_label = CTkLabel(master=self.slider_grid,
                                            text=f"Version ({round(self.version_slider.get())})",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.version_slider_label.grid(column=0, row=0, pady=4)


        # Border Slider + Label
        self.border_slider = CTkSlider(master=self.slider_grid,
                                                width=320,
                                                height=20,
                                                from_=0,
                                                to=100,
                                                number_of_steps=101,
                                                command=self.__update_ui_action)
        self.border_slider.grid(column=1, row=1)
        self.border_slider.set(4) # Sets initial value

        self.border_slider_label = CTkLabel(master=self.slider_grid,
                                            text=f"Border Size ({round(self.border_slider.get())})",
                                            width=120,
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.border_slider_label.grid(column=0, row=1, pady=4)

        # Boxsize Slider + Label
        self.boxsize_slider = CTkSlider(master=self.slider_grid,
                                            width=320,
                                            height=20,
                                            from_=1,
                                            to=100,
                                            number_of_steps=100,
                                            command=self.__update_ui_action)
        self.boxsize_slider.grid(column=1, row=2)
        self.boxsize_slider.set(10) # Sets initial value

        self.boxsize_slider_label = CTkLabel(master=self.slider_grid,
                                            text=f"Size ({round(self.boxsize_slider.get())})",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.boxsize_slider_label.grid(column=0, row=2, pady=[4, 0])


    def __build_main_frames(self):
        # Preview Frame
        self.preview_frame = CTkFrame(master=self.__root,
                                        border_width=0,
                                        corner_radius=0)

        self.preview_image = CTkLabel(master=self.preview_frame,
                                        width=400,
                                        height=400,
                                        corner_radius=0,
                                        text="")
        
        self.preview_image.pack(anchor="center", expand=True)

        # Settings Frame
        self.settings_frame = CTkFrame(master=self.__root,
                                            width=600,
                                            fg_color="transparent",
                                            height=600,
                                            border_width=0,
                                            corner_radius=0)

        self.repack_main_frames(True)

        # Filename Entrybox + Label
        self.filename_box_label = CTkLabel(master=self.settings_frame,
                                            text="Filename",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.filename_box_label.pack(side=TOP, anchor="w", pady=[0, GAP_Y[1]])

        self.filename_box = CTkEntry(master=self.settings_frame,
                                            height=20,
                                            border_width=2,
                                            corner_radius=10)
        self.filename_box.pack(side=TOP, anchor="w", fill=X)
        self.filename_box.insert(0, "qr-code")

        # Content Textbox + Label
        self.content_box_label = CTkLabel(master=self.settings_frame,
                                            text="Content",
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")
        self.content_box_label.pack(side=TOP, anchor="w", pady=GAP_Y)

        self.content_box = CTkTextbox(master=self.settings_frame,
                                            height=130,
                                            border_width=2,
                                            corner_radius=10)
        self.content_box.pack(fill=X)
        self.content_box.bind("<KeyRelease>", self.__update_ui_action)


    def __build_logo_settings(self):
        # Logosize Slider + Label
        self.logosize_slider = CTkSlider(master=self.settings_frame,
                                            width=120,
                                            height=20,
                                            from_=1,
                                            to=10,
                                            number_of_steps=10,
                                            command=self.__update_ui_action)
        self.logosize_slider.set(5) # Sets initial value

        self.logosize_slider_label = CTkLabel(master=self.settings_frame,
                                            text=f"Logosize ({round(self.logosize_slider.get())})",
                                            width=100,
                                            height=20,
                                            corner_radius=8,
                                            fg_color="transparent")

        # Logo Select Button
        self.logo_select_button = CTkButton(master=self.settings_frame,
                                        width=110,
                                        height=20,
                                        fg_color="#888888",
                                        hover_color="#666666",
                                        text="Change Logo",
                                        command=self.__select_logo_action)
    

    def __build_bottom_frame(self):
        # Bottom frame
        self.bottom_frame = CTkFrame(master=self.settings_frame, fg_color="transparent")
        self.bottom_frame.pack(fill=X, pady=[0, 12])

        # Logo Checkbox
        self.logo_checkbox = CTkCheckBox(master=self.bottom_frame,
                                        height=20,
                                        text="Enable Logo",
                                        command=self.__update_ui_action)

        self.logo_checkbox.pack(side=LEFT, anchor="n", pady=GAP_Y)

        # Preview Checkbox
        self.preview_checkbox = CTkCheckBox(master=self.bottom_frame,
                                        height=20,
                                        text="Enable Preview",
                                        command=self.__update_ui_action)

        self.preview_checkbox.pack(side=LEFT, anchor="n", padx=[16, 0], pady=GAP_Y)
        self.preview_checkbox.select()


        # Save Button
        self.save_button = CTkButton(master=self.bottom_frame,
                                            width=120,
                                            corner_radius=8,
                                            text="Save",
                                            command=self.__create_and_save_qr_action)
        self.save_button.pack(side=RIGHT, padx=[8, 0], anchor="n", pady=[GAP_Y[0] - 3, 0])


        # Open Folder Button
        self.open_folder_button = CTkButton(master=self.bottom_frame,
                                            width=110,
                                            fg_color="#666666",
                                            hover_color="#444444",
                                            text="Open Folder",
                                            command=self.__open_folder_action)
        self.open_folder_button.pack(side=RIGHT, anchor="n", pady=[GAP_Y[0] - 3, 0])


    def build(self):
        self.__build_main_frames()
        self.__build_advanced_settings()
        self.__build_bottom_frame()
        self.__build_logo_settings()
