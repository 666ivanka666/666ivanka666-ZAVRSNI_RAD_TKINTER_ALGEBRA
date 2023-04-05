from tkinter import *
from PIL import Image, ImageTk
from src.gui.plant_details import PlantDetails


class PlantList(Frame):
    def __init__(self, plant_repo, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.plant_repo = plant_repo
        self.image_path = StringVar()
        self.canvas = Canvas(self)
        self.init_window()

    def init_window(self):
        self.canvas.destroy()
        self.canvas = Canvas(self)
        self.canvas.configure(width=900, height=900)
        self.canvas.pack(fill="both", expand=True, padx=150)

        self.plants_frame = Frame(self.canvas)
        self.canvas.create_window(1, 0, window=self.plants_frame, anchor="nw")

        plants = self.plant_repo.get_all_plants()
        for (i, p) in enumerate(plants):
            self.draw_plant(self.plants_frame, p, i)

        self.draw_insert_plant(self.plants_frame, len(plants))

        self.plants_frame.pack(side="top", fill="both", expand=True)
        self.canvas.create_window(self.winfo_width() / 3, self.canvas.winfo_height() / 3, window=self.plants_frame,
                                  anchor="center")


        self.plants_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.plants_frame.bind("<Enter>", lambda e: self.plants_frame.bind("<Motion>"))


    def draw_plant(self, main_frame, plant, index):
        info_frame = LabelFrame(main_frame, bg="light grey", width=main_frame.winfo_width(),
                                height=main_frame.winfo_height(), text=str(plant.plant_name), font=("Arial", 10, "bold"))
        info_frame.grid_propagate(True)
        info_frame.grid(row=int(index / 3), column=index % 3, padx=5, pady=5, sticky="nsew")

        info_frame.grid_rowconfigure(0, weight=1)
        info_frame.grid_columnconfigure(1, weight=1)
        info_frame.grid(sticky="nsew")

        Label(info_frame, text="Substrate:", bg="light grey", fg="black",
              font=("Arial", 10, "normal", "underline")).grid(
            row=0, column=0, padx=0.01, pady=0.01)
        Label(info_frame, text=str(plant.substrate), bg="light grey", fg="black", font=("Arial", 10)).grid(row=0,
                                                                                                           column=1,
                                                                                                           padx=0.01,
                                                                                                           pady=0.01)
        Label(info_frame, text="Illumination:", bg="light grey", fg="black",
              font=("Arial", 10, "normal", "underline")).grid(
            row=1, column=0, padx=0.01, pady=0.01)
        Label(info_frame, text=str(plant.required_illumination), bg="light grey", fg="black", font=("Arial", 10)).grid(
            row=1,
            column=1,
            padx=0.01,
            pady=0.01)

        img = Image.open(plant.image_path)
        resized = img.resize((80, 80))
        new_picture = ImageTk.PhotoImage(resized)

        e1 = Label(info_frame, image=new_picture)
        e1.grid(row=0, column=2, rowspan=2, padx=5, pady=5)
        e1.image = new_picture
        e1.bind("<Button-1>", lambda e: self.open_plant_details(plant.id))

    def open_plant_details(self, plant_id):
        details = PlantDetails(self.plant_repo, self.parent, self.controller, plant_id)
        details.grid(row=1, column=0, sticky="nsew")
        details.tkraise()

    def draw_insert_plant(self, main_frame, index):
        new_plant_frame = LabelFrame(main_frame, text="New Plant", bg="light grey", fg="black",font=("Arial", 10, "bold"))
        new_plant_frame.grid_propagate(True)
        new_plant_frame.grid(row=int(index / 3), column=index % 3, padx=5, pady=5, sticky="nsew")

        Button(new_plant_frame, text="Add plant", font=("Arial", 10),bg="light grey", fg="black",
               command=lambda: self.redirect_to_insert_plant()).pack()

    def redirect_to_insert_plant(self):
        self.controller.show_frame("PlantInput").clean()
        self.controller.show_frame("PlantInput").init_window()
