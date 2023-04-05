from tkinter import *

from PIL import Image, ImageTk
from src.gui.pot_details import PotDetails
import random


class PotList(Frame):
    def __init__(self, pot_repo, plant_repo, plant_in_pot_repo, parent, controller, user_state):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.pot_repo = pot_repo
        self.plant_repo = plant_repo
        self.plant_in_pot_repo = plant_in_pot_repo
        self.image_path = StringVar()
        self.canvas = Canvas(self)
        self.user_state = user_state
        self.moisture_level = random.randint(1, 50)
        self.light_level = random.randint(0, 1200)
        self.init_window()

    def init_window(self):
        self.parent.configure(bg="light grey")
        self.canvas.destroy()
        self.canvas = Canvas(self)
        self.canvas.configure(width=900, height=900)
        self.canvas.pack(fill="both", expand=True, padx=75)

        self.pots_frame = Frame(self.canvas)
        self.canvas.create_window(1, 1, window=self.pots_frame, anchor="nw")

        pots = self.pot_repo.get_all_pots(self.user_state.user_id)
        for (i, p) in enumerate(pots):
            self.draw_pot(self.pots_frame, p, i)

        self.draw_insert_pot(self.pots_frame, len(pots))

        self.draw_sync_button(self.pots_frame)

        self.pots_frame.pack(side="top", fill="both", expand=True)
        self.canvas.create_window(self.winfo_width() / 3, self.canvas.winfo_height() / 3, window=self.pots_frame,
                                  anchor="center")

        self.pots_frame.pack(side="top", fill="both", expand=True)
        self.canvas.create_window(self.winfo_width() / 3, self.canvas.winfo_height() / 3, window=self.pots_frame,
                                  anchor="center")

        self.pots_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.pots_frame.bind("<Enter>", lambda e: None)

    def draw_pot(self, main_frame, pot, index):
        info_frame = LabelFrame(main_frame, bg="light grey", width=main_frame.winfo_width(),
                                height=main_frame.winfo_height(), text=str(pot[0].name), font=("Arial", 10, "bold"))
        info_frame.grid_propagate(True)
        info_frame.grid(row=int(index / 3), column=index % 3, padx=5, pady=5, sticky="nsew")

        info_frame.grid_rowconfigure(0, weight=1)
        info_frame.grid_columnconfigure(1, weight=1)
        info_frame.grid(sticky="nsew")

        if pot[1] is None:
            plant_name = "No plant"
            plant_image = None
        else:
            plant_name = pot[1].plant_name
            plant_image = Image.open(pot[1].image_path)

        moisture_level = random.randint(1, 51)
        light_level = random.randint(1, 1001)
        needs_watering = False

        Label(info_frame, text="PlantName: " + str(plant_name), bg="light grey", fg="black",
              font=("Arial", 10, "normal")).grid(row=0, column=0, padx=0.01, pady=0.01)
        Label(info_frame, text=f"Moisture level: {moisture_level} %", bg="light grey", fg="black",
              font=("Arial", 10, "normal")).grid(row=2, column=0, padx=0.01, pady=0.01)
        Label(info_frame, text=f"Light level: {light_level} lux", bg="light grey", fg="black",
              font=("Arial", 10, "normal")).grid(row=3, column=0, padx=0.01, pady=0.01)

        if plant_image is not None:
            image_width, image_height = plant_image.size
            max_width = 100
            max_height = 100
            if image_width > max_width or image_height > max_height:
                resize_factor = min(max_width / image_width, max_height / image_height)
                new_width = int(image_width * resize_factor)
                new_height = int(image_height * resize_factor)
                plant_image = plant_image.resize((new_width, new_height))

            plant_photo = ImageTk.PhotoImage(plant_image)
            plant_label = Label(info_frame, image=plant_photo)
            plant_label.image = plant_photo
            plant_label.grid(row=0, column=2, padx=5)

        status = "Empty" if pot[1] is None else "Full"

        Label(info_frame, text="PlantName: " + str(plant_name), bg="light grey", fg="black",
              font=("Arial", 10, "normal")).grid(row=0, column=0, padx=0.01, pady=0.01)
        Label(info_frame, text=f"Moisture level: {moisture_level} %", bg="light grey", fg="black",
            font=("Arial", 10, "normal")).grid(row=2, column=0, padx=0.01, pady=0.01)
        Label(info_frame, text=f"Light level: {light_level} lux", bg="light grey", fg="black",
            font=("Arial", 10, "normal")).grid(row=3, column=0, padx=0.01, pady=0.01)

        status_label = Label(info_frame, text=f"Status: {status}", bg="light grey", fg="black", font=("Arial", 10))
        status_label.grid(row=4, column=0)

        if status == "Full":
            desired_ph_value = pot[1].desired_ph_value
            humidity_label = "You need to water the plant." if desired_ph_value < moisture_level else "The plant does not need watering."
            light_level_label = "You need to put the plant in the sun." if light_level < 1000 else "The plant needs to be in the shade."

            water_label = Label(info_frame, text=f"{humidity_label}", bg="light grey", fg="black", font=("Arial", 10))
            water_label.grid(row=5, column=0)

            shade_label = Label(info_frame, text=f"{light_level_label}", bg="light grey", fg="black", font=("Arial", 10))
            shade_label.grid(row=6, column=0)

        redirect = Button(info_frame, text="Click me", bg="light grey", fg="black", font=("Arial", 10, "normal"))
        redirect.grid(row=8, column=0, padx=0.01, pady=0.01)
        redirect.bind("<Button-1>", lambda e: self.open_pot_details(pot[0].id))

    def open_pot_details(self, pot_id):
        details = PotDetails(self.pot_repo, self.plant_repo, self.plant_in_pot_repo, self.parent, self.controller,
                             pot_id, self.user_state.user_id)
        details.grid(row=1, column=0, sticky="nsew")
        details.tkraise()

    def draw_insert_pot(self, main_frame, index):
        new_pot_frame = LabelFrame(main_frame, text="New Pot", bg="light grey", fg="black", font=("Arial", 10, "bold"))
        new_pot_frame.grid_propagate(True)
        new_pot_frame.grid(row=int(index / 3), column=index % 3, padx=5, pady=5, sticky="nsew")

        Button(new_pot_frame, text="Add pot", bg="light grey", fg="black", font=("Arial", 10),
               command=lambda: self.redirect_to_insert_pot()).pack()

    def redirect_to_insert_pot(self):
        self.controller.show_frame("PotInput").init_window()

    def draw_sync_button(self, main_frame):
        sync_button = Button(main_frame, text="Sync", bg="light grey", font=("Arial", 10),command=lambda: self.init_window())
        sync_button.grid(row=2, column=0, padx=(5, 0), pady=5, sticky="w")


