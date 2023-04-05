from src.db.plant_in_pot_repo import PlantInPotRepo
from src.db.plant_repo import PlantRepo
from src.db.pot_repo import PotRepo
from src.db.seed import Seed
from src.db.session import init
from src.db.user_repo import *

session = init()

user_repo = UserRepo(session)
plant_repo = PlantRepo(session)
pot_repo = PotRepo(session)
plant_in_pot_repo = PlantInPotRepo(session)

seed = Seed(plant_repo, pot_repo, user_repo, plant_in_pot_repo)
seed.init()
