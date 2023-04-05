from tkinter import *

from src.db.model.pot import Pot


class PotInput(Frame):

    def __init__(self, pot_repo, parent, controller, user_state):
        Frame.__init__(self, parent)
        self.controller = controller
        self.user_state = user_state
        self.pot_repo = pot_repo
        self.root = Frame(self)
        self.root.grid(row=0, column=0)
        self.pot = None
        self.init_window()

    def init_window(self):
        self.root.configure(bg="light grey")
        self.file_path = None
        button_text = "Save" if self.pot is None else "Edit"


        self.image_label = Label(self.root, bg="light grey")
        self.image_label.grid(row=0, column=1, padx=10, pady=10)

        name_label = Label(self.root, text="Name", bg="light grey", fg="black", font=("Arial", 10))
        name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = Entry(self.root, bg="light grey", fg="black", font=("Arial", 10), width=20)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.save_button = Button(self.root, text=button_text, command=self.save_func)
        self.save_button.grid(row=5, column=0, padx=10, pady=10)

        if self.pot is not None:
            self.name_entry.insert(0, self.pot.name)

    def save_func(self):
        name = self.name_entry.get()

        pot = Pot(name=name, user_id=self.user_state.user_id)

        if self.pot is None:
            self.pot_repo.insert_pot(pot)
        else:
            pot.id = self.pot.id
            self.pot_repo.update_name(pot)

        self.clean()
        self.controller.show_frame("PotList").init_window()

    def clean(self):
        self.name_entry.delete(0, END)
        self.pot = None
        self.file_path = None

    def set_pot_id(self, pot_id):
        self.pot = self.pot_repo.get_by_id(pot_id)
