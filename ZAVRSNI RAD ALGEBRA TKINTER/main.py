from dataclasses import dataclass
from src.db.plant_in_pot_repo import PlantInPotRepo
from src.db.plant_repo import PlantRepo
from src.db.pot_repo import PotRepo
from src.db.session import create_session
from src.db.user_repo import *
from src.gui.gui import Gui

session = create_session()

user_repo = UserRepo(session)
plant_repo = PlantRepo(session)
pot_repo = PotRepo(session)
plant_in_pot_repo = PlantInPotRepo(session)


@dataclass
class UserState:
    user_id: int


user_state = UserState(0)

root = Gui(user_repo, plant_repo, pot_repo, plant_in_pot_repo, user_state)
root.resizable(False, False)

root.mainloop()
