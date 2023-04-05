from datetime import datetime
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from src.api.weather_api import WeatherForecast
from src.db.model.plant_in_pot import PlantInPot
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PotDetails(Frame):
    def __init__(self, pot_repo, plant_repo, plant_in_pot_repo, parent, controller, pot_id, user_id):
        Frame.__init__(self, parent)
        self.controller = controller
        self.plant_repo = plant_repo
        self.pot_repo = pot_repo
        self.plant_in_pot_repo = plant_in_pot_repo
        self.pot_id = pot_id
        self.user_id = user_id
        self.root = Frame(self, width=1000, height=1000)
       

        self.init_window()

        
    def init_window(self):
        if self.root:
            self.root.destroy()

        self.root = Frame(self, width=1000, height=1000)
        self.root.pack(side="top", fill="both", expand=True)
        self.selected_plant_id = StringVar()

        (pot, pot_in_plant, plant) = self.pot_repo.get_by_id(self.pot_id, self.user_id)
        if pot_in_plant and pot_in_plant.exhumed_datetime is None:
            self.init_window2(pot, pot_in_plant, plant)
        else:
            self.init_window2(pot, None, None)
        
        if plant:
            self.plant_data = {
                "name": plant.plant_name,
                "days_to_water": plant.days_to_water,
                "likes_shade": plant.likes_shade,
                "substrate": plant.substrate,
                "required_illumination": plant.required_illumination,
                "image_path": plant.image_path
            }

    def draw_no_plant_info(self):
        self.plants = self.plant_repo.get_all_plants()
        self.plant_id_in_plants = [plant.id for plant in self.plants]
        if self.plant_id_in_plants:
            self.plant_selection = ttk.Combobox(self.root, values=self.plant_id_in_plants,
                                                textvariable=self.selected_plant_id)
            self.plant_selection.grid(row=21, column=10, padx=10, pady=10, sticky="w")
            self.plant_selection.place(x=10, y=350, anchor="w")
            self.plant_selection.current(0)
        plant_a_plant_button = Button(self.root, text="Plant a Plant", bg="light grey", fg="black",
                                      font=("Arial", 10),
                                      command=self.plant_a_plant)
        plant_a_plant_button.grid(row=22, column=10, padx=10, pady=10, sticky="w")
        plant_a_plant_button.place(x=10, y=400, anchor="w")

        image_label = Label(self.root, text="No image found", bg="light grey")
        image_label.grid(row=15, column=35, rowspan=5, padx=10, pady=10, sticky="n")
        image_label.place(x=350, y=350, anchor="w")

    def draw_plant_info(self, plant, plant_in_pot_id):

       

        back_to_pots_list_button = Button(self.root, text="Back to Pots", bg="light grey", fg="black",
                                  font=("Arial", 10),
                                  command=self.redirect_to_pot_list)
        back_to_pots_list_button.place(x=950, y=650, anchor="w")

        sync_button = Button(self.root, text="Sync", bg="light grey", fg="black",font=("Arial", 10),
                                  command=lambda: self.init_window())
        sync_button.place(x=850, y=650, anchor="w")


        name_label = Label(self.root, text="Plant name: " + plant.plant_name, bg="light grey", fg="black",
                           font=("Arial", 10))
        name_label.grid(row=15, column=10, padx=10, pady=10, sticky="w")
        name_label.place(x=10, y=50, anchor="w")

        days_to_water_label = Label(self.root, text="Days to water: " + str(plant.days_to_water), bg="light grey",
                                    fg="black", font=("Arial", 10))
        days_to_water_label.grid(row=16, column=10, padx=10, pady=10, sticky="w")
        days_to_water_label.place(x=10, y=90, anchor="w")

        likes_shade_label = Label(self.root, text="Likes shade: " + str(plant.likes_shade), bg="light grey",
                                  fg="black",
                                  font=("Arial", 10))
        likes_shade_label.grid(row=17, column=10, padx=10, pady=10, sticky="w")
        likes_shade_label.place(x=10, y=140, anchor="w")

        substrate_label = Label(self.root, text="Substrate: " + plant.substrate, bg="light grey", fg="black",
                                font=("Arial", 10))
        substrate_label.grid(row=18, column=10, padx=10, pady=10, sticky="w")
        substrate_label.place(x=10, y=180, anchor="w")

        required_illumination_label = Label(self.root,
                                           text="Required_illumination: " + str(plant.required_illumination),
                                           bg="light grey", fg="black", font=("Arial", 10))
        required_illumination_label.grid(row=19, column=10, padx=10, pady=10, sticky="w")
        required_illumination_label.place(x=10, y=220, anchor="w")

     
        desired_ph_value_label = Label(self.root,
                                           text="Desired_ph_value: " + str(plant. desired_ph_value),
                                           bg="light grey", fg="black", font=("Arial", 10))
        desired_ph_value_label.grid(row=21, column=10, padx=10, pady=10, sticky="w")
        desired_ph_value_label.place(x=10, y=260, anchor="w")

        exhume_a_plant_button = Button(self.root, text="Exhume a Plant", bg="light grey", fg="black",
                                       font=("Arial", 10),
                                       command=lambda: self.exhume_a_plant(plant_in_pot_id))
        exhume_a_plant_button.grid(row=23, column=10, padx=10, pady=10, sticky="w")
        exhume_a_plant_button.place(x=10, y=400, anchor="w")


        img = Image.open(plant.image_path)
        resized = img.resize((700, 500))
        new_picture = ImageTk.PhotoImage(resized)
        image_label = Label(self.root, image=new_picture, bg="light grey")
        image_label.grid(row=15, column=35, rowspan=5, padx=10, pady=10, sticky="n")
        image_label.place(x=350, y=350, anchor="w")
        image_label.image = new_picture

    def init_window2(self, pot, pot_in_plant, plant):
        self.root.configure(bg="light grey")
        if not plant:
            self.draw_no_plant_info()
        if plant and pot_in_plant:
            self.draw_plant_info(plant, pot_in_plant.id)

        edit_pot_label = Button(self.root, text="Edit pot", bg="light grey", fg="black", font=("Arial", 10),
                                command=lambda: self.edit_pot(pot))
        edit_pot_label.grid(row=21, column=10, padx=10, pady=10, sticky="w")
        edit_pot_label.place(x=10, y=300, anchor="w")


        air_temperature_and_humidity_labelframe = LabelFrame(self.root, width=300, height=300,
                                                             text="Air temperature and humidity:", bg="light grey",
                                                             fg="black", font=("Arial", 10))
        air_temperature_and_humidity_labelframe.grid(column=1, row=30, padx=10, pady=10, sticky="w")
        air_temperature_and_humidity_labelframe.place(x=10, y=650, anchor="w")

        lux_and_ph_labelframe = LabelFrame(self.root, width=400, height=200, text="PH value and LUX value:",
                                           bg="light grey", fg="black", font=("Arial", 10))
        lux_and_ph_labelframe.grid(column=10, row=2, padx=10, pady=10)
        lux_and_ph_labelframe.place(x=10, y=550, anchor="w")

        graphs_label_frame = LabelFrame(self.root, width=250, height=300, text="Graphs:", bg="light grey", fg="black",
                                        font=("Arial", 10))
        graphs_label_frame.place(x=340, y=650, anchor="w")

        def create_weather_frame():
            weather_frame = Frame(
                air_temperature_and_humidity_labelframe, width=200, height=100, bg="light grey"
            )
            weather_frame.grid(row=0, column=2, padx=10, pady=10)

            ph_lux_frame = Frame(
                lux_and_ph_labelframe, width=400, height=200, bg="light grey"
            )
            ph_lux_frame.grid(row=2, column=2, padx=10, pady=10)

            def refresh_temperature():
                zagreb_forecast = WeatherForecast("zagreb")
                temperature_data = zagreb_forecast.get_formatted_weather_data()

                temperature_label.configure(text=f'{temperature_data["current_temperature"]} °C ({temperature_data["description"]})')
                
                humidity_label.configure(text=temperature_data["humidity"])


            def random_ph_label():
                return f"PH vrijednost: {np.random.randint(1, 14)} "

            def random_lux_label():
                return f"Razina svjetla: {np.random.randint(200, 1200)} "

            temperature_label = Label(
                weather_frame, bg="light grey", fg="black", text="", font=("Arial", 10)
            )
            temperature_label.grid(row=2, column=3, padx=5, pady=5)

            humidity_label = Label(
                weather_frame, bg="light grey", fg="black", text="", font=("Arial", 10)
            )
            humidity_label.grid(row=2, column=4, padx=5, pady=5)

            ph_label = Label(
                ph_lux_frame, bg="light grey", fg="black", text=random_ph_label(), font=("Arial", 10)
            )
            ph_label.grid(row=1, column=5, padx=5, pady=5)

            lux_label = Label(
                ph_lux_frame, bg="light grey", fg="black", text=random_lux_label(), font=("Arial", 10)
            )
            lux_label.grid(row=2, column=5, padx=5, pady=5)

            last_refresh_label = Label(
                weather_frame, bg="light grey", fg="black", text="", font=("Arial", 10)
            )
            last_refresh_label.grid(row=2, column=5, padx=5, pady=5)

            refresh_temperature()

            ph_label = Label(
                weather_frame, bg="light grey", fg="black", text="", font=("Arial", 10)
            )
            ph_label.grid(row=2, column=5, padx=5, pady=5)

            lux_label = Label(
                weather_frame, bg="light grey", fg="black", text="", font=("Arial", 10)
            )
            lux_label.grid(row=2, column=5, padx=5, pady=5)

        
                
        # def graph_line():
        #     plt.close()

        #     temp_values = np.random.uniform(0, 30, 24)
        #     humid_values = np.random.uniform(30, 70, 24)
        #     ph_values = np.random.uniform(1, 14, 24)
        #     lux_values = np.random.uniform(500, 1000, 24)

        #     time_values = np.arange(0, 24, 1)  

        #     plt.plot(time_values, temp_values, label="Temperature", linestyle="dashed")
        #     plt.plot(time_values, humid_values, label="Humidity", linestyle="solid")
        #     plt.plot(time_values, ph_values, label="PH", linestyle="dotted")
        #     plt.plot(time_values, lux_values, label="Lux", linestyle="solid")

        #     plt.xlabel("Time (hours)")
        #     plt.ylabel("Sensor Value")
        #     plt.title("Sensor Values Every 24 Hours")

        #     plt.legend()
        #     plt.show()

        # graf1 = Button(graphs_label_frame, text="Line", bg="grey", fg="white", font=("Arial", 10), command=graph_line)
        # graf1.grid(column=0, row=2, columnspan=15, padx=15, pady=15)

        # def graph_hist():
        #     plt.close()

        #     temp_values = np.random.uniform(0, 30, 24)
        #     humid_values = np.random.uniform(30, 70, 24)
        #     ph_values = np.random.uniform(1, 14, 24)
        #     lux_values = np.random.uniform(500, 1000, 24)

        #     plt.hist(temp_values, bins=20, alpha=0.5, label="Temperature", range=(0, 24))
        #     plt.hist(humid_values, bins=5, alpha=0.5, label="Humidity", range=(0, 24))
        #     plt.hist(ph_values, bins=10, alpha=0.5, label="PH", range=(0, 24))
        #     plt.hist(lux_values, bins=5, alpha=0.5, label="Lux", range=(0, 24))

        #     plt.xlabel("Time (hours)")
        #     plt.ylabel("Sensor Value")
        #     plt.title("Sensor Values Every 24 Hours")

        #     plt.legend()
        #     plt.show()


        # graf2 = Button(graphs_label_frame, text="Histogram", bg="grey", fg="white", font=("Arial", 10),
        #                command=graph_hist)
        # graf2.grid(column=24, row=2, columnspan=15, padx=15, pady=15)

        # def graph_pie():
        #     plt.close()

        #     temp_values = np.random.uniform(-10, 40, 24)
        #     humid_values = np.random.uniform(0, 100, 24)
        #     ph_values = np.random.uniform(1, 14, 24)
        #     lux_values = np.random.uniform(500, 1000, 24)

        #     total = sum(temp_values) + sum(humid_values) + sum(ph_values) + sum(lux_values)

        #     y1_proportion = sum(temp_values) / total
        #     y2_proportion = sum(humid_values) / total
        #     y3_proportion = sum(ph_values) / total
        #     y4_proportion = sum(lux_values) / total

        #     labels = ["Temperature", "Humidity", "PH", "LUX"]
        #     sizes = [y1_proportion, y2_proportion, y3_proportion, y4_proportion]

        #     _, ax = plt.subplots()
        #     ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        #     ax.axis("equal")
        #     ax.legend(loc="lower right")

        #     plt.title("Sensor value every 24 hours")
        #     plt.show()

            

        # graf3 = Button(graphs_label_frame, text="Pie", bg="grey", fg="white", font=("Arial", 10), command=graph_pie)
        # graf3.grid(column=48, row=2, columnspan=15, padx=15, pady=15)


        def graph_line():
            plt.close()

            fig = plt.Figure(figsize=(2, 1), dpi=100)
            ax = fig.add_subplot(111)

            temp_values = np.random.uniform(0, 30, 24)
            humid_values = np.random.uniform(30, 70, 24)
            ph_values = np.random.uniform(1, 14, 24)
            lux_values = np.random.uniform(500, 1000, 24)

            time_values = np.arange(0, 24, 1)  

            ax.plot(time_values, temp_values, label="Temperature", linestyle="dashed")
            ax.plot(time_values, humid_values, label="Humidity", linestyle="solid")
            ax.plot(time_values, ph_values, label="PH", linestyle="dotted")
            ax.plot(time_values, lux_values, label="Lux", linestyle="solid")

            ax.set_xlabel("Time (hours)", fontsize=6)
            ax.set_ylabel("Sensor Value", fontsize=6)
            ax.set_title("Sensor Values Every 24 Hours", fontsize=6)

            ax.tick_params(axis='both', which='major', labelsize=6)
            ax.legend(fontsize = 5, loc='lower left')
            fig.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8, wspace=0.2, hspace=0.2)

            canvas = FigureCanvasTkAgg(fig, master=graphs_label_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=0)
                
        graf1 = Button(graphs_label_frame, text="Line", bg="grey", fg="white", font=("Arial", 10), command=graph_line)
        graf1.grid(column=0, row=2, columnspan=15, padx=15, pady=15)

        def graph_hist():
            plt.close()

            fig = plt.Figure(figsize=(2, 1), dpi=100)
            ax = fig.add_subplot(111)

            temp_values = np.random.uniform(0, 30, 24)
            humid_values = np.random.uniform(30, 70, 24)
            ph_values = np.random.uniform(1, 14, 24)
            lux_values = np.random.uniform(500, 1000, 24)


            ax.hist(temp_values, bins=20, alpha=0.5, label="Temperature", range=(0, 24))
            ax.hist(humid_values, bins=5, alpha=0.5, label="Humidity", range=(0, 24))
            ax.hist(ph_values, bins=10, alpha=0.5, label="PH", range=(0, 24))
            ax.hist(lux_values, bins=5, alpha=0.5, label="Lux", range=(0, 24))

            ax.set_xlabel("Time (hours)", fontsize=6)
            ax.set_ylabel("Sensor Value",fontsize=6)
            ax.set_title("Sensor Values Every 24 Hours",fontsize=6)

            ax.tick_params(axis='both', which='major', labelsize=6)
            ax.legend(fontsize = 5, loc='lower left')
            fig.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8)

            canvas = FigureCanvasTkAgg(fig, master=graphs_label_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(column=24, row=0)

        graf2 = Button(graphs_label_frame, text="Histogram", bg="grey", fg="white", font=("Arial", 10),
                       command=graph_hist)
        graf2.grid(column=24, row=2, columnspan=15, padx=15, pady=15)

        def graph_pie():

            temp_values = np.random.uniform(-10, 40, 24)
            humid_values = np.random.uniform(0, 100, 24)
            ph_values = np.random.uniform(1, 14, 24)
            lux_values = np.random.uniform(500, 1000, 24)

            total = sum(temp_values) + sum(humid_values) + sum(ph_values) + sum(lux_values)

            y1_proportion = sum(temp_values) / total
            y2_proportion = sum(humid_values) / total
            y3_proportion = sum(ph_values) / total
            y4_proportion = sum(lux_values) / total

            labels = ["Temperature", "Humidity", "PH", "LUX"]
            sizes = [y1_proportion, y2_proportion, y3_proportion, y4_proportion]

            fig = plt.Figure(figsize=(2, 1), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_position([0.2, 0.2, 0.6, 0.6])

            ax.pie(sizes, labels=labels, autopct="%1.1f%%", textprops={'fontsize': 6})
            ax.axis("equal")
            ax.legend(loc="lower right", fontsize=5)
            plt.title("Sensor value every 24 hours", fontsize=6)

            
            plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8)
            
            canvas = FigureCanvasTkAgg(fig, master=graphs_label_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        graf3 = Button(graphs_label_frame, text="Pie", bg="grey", fg="white", font=("Arial", 10), command=graph_pie)
        graf3.grid(column=48, row=2, columnspan=15, padx=15, pady=15)

        create_weather_frame()

    def edit_pot(self, pot):

        for widget in self.root.winfo_children():
            widget.destroy()

        pot_label = Label(self.root, text="Pot name:", bg="light grey", fg="black", font=("Arial", 10))
        pot_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        pot_label.place(x=10, y=50, anchor="w")

        self.pot_entry = Entry(self.root, textvariable=pot.name, bg="white", fg="black", font=("Arial", 10))
        self.pot_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.pot_entry.place(x=10, y=100, anchor="w")

        save_button = Button(self.root, text="Save", bg="light grey", fg="black", font=("Arial", 10),
                             command=lambda: self.save_pot(pot))
        save_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        save_button.place(x=10, y=150, anchor="w")

    def save_pot(self, pot):
        if pot:
            pot.name = self.pot_entry.get()
            self.pot_repo.update_name(pot.id, pot.name)
        self.controller.show_frame("PotList").init_window()

    def plant_a_plant(self):

        plant_in_pot = PlantInPot(plant_id=self.selected_plant_id.get(), pot_id=self.pot_id,
                                  planted_datetime=datetime.now())
        self.plant_in_pot_repo.plant_plant_in_pot(plant_in_pot)
        self.init_window()

    def exhume_a_plant(self, plant_in_pot_id):
        self.plant_in_pot_repo.exhume_plant_from_pot(plant_in_pot_id, datetime.now())
        self.init_window()
    
    def redirect_to_pot_list(self):
        self.controller.show_frame("PotList").init_window()
