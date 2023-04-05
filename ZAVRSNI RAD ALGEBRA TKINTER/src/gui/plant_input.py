from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from src.db.model.plant import Plant
from tkinter import messagebox


class PlantInput(Frame):

    def __init__(self, plant_repo, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.plant_repo = plant_repo
        self.root = Frame(self)
        self.root.grid(row=0, column=0)
        self.plant = None
        self.init_window()

    def init_window(self):
        self.root.configure(bg="light grey")
        self.file_path = None 
        button_text = "Save" if self.plant is None else "Edit"
        
        self.browse_button = Button(self.root, text="Browse", command=self.browse_func)
        self.browse_button.grid(row=0, column=0, padx=10, pady=10)

        self.image_label = Label(self.root, bg="light grey")
        self.image_label.grid(row=0, column=1, padx=10, pady=10)

        name_label = Label(self.root, text="Name", bg="light grey", fg="black", font=("Arial", 10))
        name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = Entry(self.root, bg="light grey", fg="black", font=("Arial", 10), width=20)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        substrate_label = Label(self.root, text="Substrate", bg="light grey", fg="black", font=("Arial", 10))
        substrate_label.grid(row=2, column=0, padx=10, pady=10)
        self.substrate_entry = Entry(self.root, bg="light grey", fg="black", font=("Arial", 10), width=20)
        self.substrate_entry.grid(row=2, column=1, columnspan=10, padx=10, pady=10)

        illumination_label = Label(self.root, text="Illumination", bg="light grey", fg="black", font=("Arial", 10))
        illumination_label.grid(row=4, column=0, padx=10, pady=10)
        self.illumination_entry = Entry(self.root, bg="light grey", fg="black", font=("Arial", 10), width=20)
        self.illumination_entry.grid(row=4, column=1, columnspan=10, padx=10, pady=10)

        desired_ph_value_label = Label(self.root, text="Ph_value", bg="light grey", fg="black", font=("Arial", 10))
        desired_ph_value_label.grid(row=5, column=0, padx=10, pady=10)
        self.desired_ph_value_entry = Entry(self.root, bg="light grey", fg="black", font=("Arial", 10), width=20)
        self.desired_ph_value_entry.grid(row=5, column=1, columnspan=10, padx=10, pady=10)


        self.save_button = Button(self.root, text=button_text, command=self.save_func)
        self.save_button.grid(row=7, column=0, padx=10, pady=10)

        if self.plant is not None:  
            self.name_entry.insert(0, self.plant.plant_name)
            self.substrate_entry.insert(0, self.plant.substrate)
            self.illumination_entry.insert(0, self.plant.required_illumination)
            self.desired_ph_value_entry.insert(0, self.plant.desired_ph_value)
            self.set_image()

    def browse_func(self):
        file_path = filedialog.askopenfilename()
        image = Image.open(file_path)
        image = image.resize((200, 100), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=image)
        self.image_label.image = image
        self.file_path = file_path

    def set_image(self):
        image = Image.open(self.plant.image_path)
        image = image.resize((200, 100), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=image)
        self.image_label.image = image
        self.file_path = self.plant.image_path

    def save_func(self):
        plant_name = self.name_entry.get()
        substrate = self.substrate_entry.get()
        illumination_str = self.illumination_entry.get()
        ph_value_str = self.desired_ph_value_entry.get()

        if not illumination_str.isnumeric():
            messagebox.showerror("Error", "Illumination must be a number")
            return
        elif not ph_value_str.isnumeric():
            messagebox.showerror("Error", "Ph value must be a number")
            return

        illumination = int(illumination_str)
        ph_value = int(ph_value_str)

        
        plant = Plant(plant_name=plant_name, image_path=self.file_path, 
                      desired_ph_value=ph_value,
                      required_illumination=illumination, substrate=substrate,
                        likes_shade=True, days_to_water=0)
        
        if self.plant is None:    
            self.plant_repo.insert_plant(plant)
        else:
            plant.id = self.plant.id
            self.plant_repo.update_plant(plant)
        
        self.clean()
        self.controller.show_frame("PlantList").init_window()

    def clean(self):
        self.name_entry.delete(0, END)
        self.substrate_entry.delete(0, END)
        self.illumination_entry.delete(0, END)
        self.image_label.config(image='')
        self.plant = None
        self.file_path = None

    def set_plant_id(self, plant_id):
        self.plant = self.plant_repo.get_by_id(plant_id)
       
       