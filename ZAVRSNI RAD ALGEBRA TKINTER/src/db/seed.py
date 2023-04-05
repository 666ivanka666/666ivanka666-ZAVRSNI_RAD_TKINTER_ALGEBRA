from datetime import datetime

from src.db.model.plant_in_pot import PlantInPot
from src.db.plant_repo import Plant
from src.db.pot_repo import Pot
from src.db.user_repo import User
from sqlalchemy import func

class Seed:
    def __init__(self, plant_repo, pot_repo, user_repo, plant_in_pot_repo):
        self.plant_repo = plant_repo
        self.user_repo = user_repo
        self.pot_repo = pot_repo
        self.plant_in_pot_repo = plant_in_pot_repo

    def seed_plants(self):
        plants = [
            Plant(id=1, plant_name="Bosiljak", desired_ph_value=6.5, image_path="./slike/bosiljak.jpg", days_to_water=3, likes_shade=False,
                  substrate="soil", required_illumination=0),
            Plant(id=2, plant_name="Crvena Ruza",desired_ph_value=4.2, image_path="./slike/crvena_ruza.jpg", days_to_water=5, likes_shade=True,
                  substrate="soil", required_illumination=1),
            Plant(id=3, plant_name="Bijela Kala", desired_ph_value=8.1,image_path="./slike/kala_bijela.jpg", days_to_water=2, likes_shade=False,
                  substrate="sand", required_illumination=2),
            Plant(id=4, plant_name="Zuta Kala", desired_ph_value=2.0,image_path="./slike/kala_zuta.jpg", days_to_water=1, likes_shade=True,
                  substrate="sand", required_illumination=3),
            Plant(id=5, plant_name="Lavanda", desired_ph_value=1.5,image_path="./slike/lavanda.jpg", days_to_water=0, likes_shade=False,
                  substrate="soil", required_illumination=4),
            Plant(id=6, plant_name="Ljiljan", desired_ph_value=7.2,image_path="./slike/ljiljan.jpg", days_to_water=4, likes_shade=True,
                  substrate="sand", required_illumination=5),
            Plant(id=7, plant_name="Zuta Ruza", desired_ph_value=9.3,image_path="./slike/ruza_zuta.jpg", days_to_water=2, likes_shade=True,
                  substrate="soil", required_illumination=6),
            Plant(id=8, plant_name="Ruzmarin", desired_ph_value=3.4,image_path="./slike/ruzmarin.jpg", days_to_water=3, likes_shade=True,
                  substrate="sand", required_illumination=7),
            Plant(id=9, plant_name="Crveni Tulipan", desired_ph_value=2.7,image_path="./slike/tulipan_crvena.jpg", days_to_water=1,
                  likes_shade=False,
                  substrate="sand", required_illumination=8),
            Plant(id=10, plant_name="Zuti Tulipan", desired_ph_value=1.8,image_path="./slike/tulipan_zuta1.jpg", days_to_water=1,
                  likes_shade=False,
                  substrate="soil", required_illumination=9)
        ]

        for plant in plants:
            self.plant_repo.insert_plant(plant)
        print("All plants have been inserted into the database!")

    def seed_users(self):
        users = [User(first_name="Ivanka", last_name="Budimir", username="ivanka",
                    password="666", admin=False, active=True),
                ]

        for user in users:
            existing_user = self.user_repo.session.query(User).filter(User.username == user.username).first()

            if existing_user is None:
                self.user_repo.insert_user(user)


        print("All users have been inserted into the database!")

    def seed_pots(self):
        pots = [Pot(name="Kockasti", user_id=1),
                Pot(name="Crveni", user_id=1),
                Pot(name="Kokos", user_id=1)
                ]
        for pot in pots:
            self.pot_repo.insert_pot(pot)
        print("All pots have been inserted into the database!")

    def plant_some_plants(self):
        self.plant_in_pot_repo.plant_plant_in_pot(PlantInPot(planted_datetime=datetime.now(), pot_id=1, plant_id=1))

    def init(self):
        self.seed_users()
        self.seed_plants()
        self.seed_pots()
        self.plant_some_plants()

