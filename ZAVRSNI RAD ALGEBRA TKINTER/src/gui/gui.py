import tkinter as tk
from tkinter import font as tkfont

from src.gui.header import Header
from src.gui.login_screen import LoginForm
from src.gui.plant_input import PlantInput
from src.gui.plant_list import PlantList
from src.gui.pot_input import PotInput
from src.gui.pot_list import PotList


class Gui(tk.Tk):

    def __init__(self, user_repo, plant_repo, pot_repo, plant_in_pot_repo, user_state):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold", slant="italic")
        self.title("PyPosuda | Biljke")
        self.geometry("1200x800")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.configure(bg="light grey")
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        header = Header(container, self, user_state)
        plant_frame = PlantList(plant_repo, container, self)
        pot_frame = PotList(pot_repo, plant_repo, plant_in_pot_repo, container, self, user_state)
        plant_input_frame = PlantInput(plant_repo, container, self)
        pot_input_frame = PotInput(pot_repo, container, self, user_state)
        login_frame = LoginForm(user_repo, container, self, user_state)

        self.frames["Login"] = login_frame
        self.frames["Header"] = header
        self.frames["PlantList"] = plant_frame
        self.frames["PotList"] = pot_frame
        self.frames["PlantInput"] = plant_input_frame
        self.frames["PotInput"] = pot_input_frame

        login_frame.grid(rowspan=2, column=0, sticky="nsew")
        header.grid(row=0, column=0, sticky="nsew")
        plant_frame.grid(row=1, column=0, sticky="nsew")
        pot_frame.grid(row=1, column=0, sticky="nsew")
        plant_input_frame.grid(row=1, column=0, sticky="nsew")
        pot_input_frame.grid(row=1, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.init_window()
        frame.tkraise()
        return frame
