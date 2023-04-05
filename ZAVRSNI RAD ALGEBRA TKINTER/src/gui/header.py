from tkinter import *


class Header(Frame):

    def __init__(self, parent, controller, user_state):
        Frame.__init__(self, parent)
        self.controller = controller
        self.user_state = user_state
        self.top_frame = Frame(self, bg="cyan", width=450, height=50, pady=3)
        self.init_window()

    def init_window(self):
        self.top_frame.destroy()
        self.top_frame = Frame(self, bg="cyan", width=450, height=50, pady=3)
        self.top_frame.grid(row=0, sticky="e", padx=5, pady=5)

       
        pots = Button(self.top_frame, text="Pots", width="10",
                      command=lambda: self.pot_list())
        pots.grid(row=0, column=4)
      

        plants = Button(self.top_frame, text="Plants", width="10",
                        command=lambda: self.plant_list())
        plants.grid(row=0, column=6)

        logout_button = Button(self.top_frame, text="Logout", width="10",
                               command=lambda: self.on_click_logout())
        logout_button.grid(row=0, column=8, sticky="e")

    def pot_list(self):
        self.controller.show_frame("PotList").init_window()

    def plant_list(self):
        self.controller.show_frame("PlantList").init_window()


    def on_click_logout(self):
        self.controller.show_frame("Login")
