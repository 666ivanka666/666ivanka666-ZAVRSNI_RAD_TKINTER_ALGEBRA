from tkinter import *

from PIL import Image, ImageTk


class PlantDetails(Frame):

    def __init__(self, plant_repo, parent, controller, plant_id):
        Frame.__init__(self, parent)
        self.controller = controller
        self.plant_id = StringVar()
        self.plant_repo = plant_repo
        self.root = Frame(self, width=1000, height=1000)
        self.root.pack(side="top", fill="both", expand=True)
        self.init_window(plant_id)
        

    def init_window(self, plant_id):
        self.root.configure(bg="light grey")
        plant = self.plant_repo.get_by_id(plant_id)
       
        img = Image.open(plant.image_path)
        resized = img.resize((700, 500))
        new_picture = ImageTk.PhotoImage(resized)
        image_label = Label(self.root, image=new_picture, bg="light grey")
        image_label.grid(row=15, column=35, rowspan=5, padx=10, pady=10, sticky="n")
        image_label.place(x=350, y=350, anchor="w")
        image_label.image = new_picture

        name_label = Label(self.root, text="Plant name: " + plant.plant_name, bg="light grey", fg="black", font=("Arial", 10))
        name_label.grid(row=15, column=10, padx=10, pady=10, sticky="w")
        name_label.place(x=10, y=50, anchor="w")

        days_to_water_label = Label(self.root, text= "Days to water: " + str(plant.days_to_water), bg="light grey", fg="black", font=("Arial", 10))
        days_to_water_label.grid(row=16, column=10, padx=10, pady=10, sticky="w")
        days_to_water_label.place(x=10, y=90, anchor="w")

        likes_shade_label = Label(self.root, text="Likes shade: " + str(plant.likes_shade), bg="light grey", fg="black", font=("Arial", 10))
        likes_shade_label.grid(row=17, column=10, padx=10, pady=10, sticky="w")
        likes_shade_label.place(x=10, y=140, anchor="w")

        substrate_label = Label(self.root, text="Substrate: " + plant.substrate, bg="light grey", fg="black", font=("Arial", 10))
        substrate_label.grid(row=18, column=10, padx=10, pady=10, sticky="w")
        substrate_label.place(x=10, y=180, anchor="w")

        required_illumination_label = Label(self.root, text="Required_illumination: " + str(plant.required_illumination), bg="light grey", fg="black", font=("Arial", 10))
        required_illumination_label.grid(row=19, column=10, padx=10, pady=10, sticky="w")
        required_illumination_label.place(x=10, y=220, anchor="w")

        desired_ph_value_label = Label(self.root, text="Desired_ph_value: " + str(plant.desired_ph_value), bg="light grey", fg="black", font=("Arial", 10))
        desired_ph_value_label.grid(row=21, column=10, padx=10, pady=10, sticky="w")
        desired_ph_value_label.place(x=10, y=260, anchor="w")


        
        edit_plant_label = Button(self.root, text="Edit plant", bg="light grey", fg="black", font=("Arial", 10), command=lambda: self.edit_plant(plant_id))
        edit_plant_label.grid(row=22, column=10, padx=10, pady=10, sticky="w")
        edit_plant_label.place(x=10, y=300, anchor="w")

        back_to_plants_list_button = Button(self.root, text="Back to Plants", bg="light grey", fg="black",
                                  font=("Arial", 10),
                                  command=self.redirect_to_pot_list)
        back_to_plants_list_button.place(x=950, y=650, anchor="w")


    def edit_plant(self, plant_id):      
        self.controller.frames["PlantInput"].set_plant_id(plant_id)
        self.controller.show_frame("PlantInput").init_window()
 

    def redirect_to_pot_list(self):
        self.controller.show_frame("PlantList").init_window()
  
