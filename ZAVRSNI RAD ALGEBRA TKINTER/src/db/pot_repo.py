from src.db.model.plant import Plant
from src.db.model.plant_in_pot import PlantInPot
from src.db.model.pot import Pot


class PotRepo:
    def __init__(self, session):
        self.session = session

    def insert_pot(self, pot):
        self.session.add(pot)
        self.session.commit()

    def get_all_pots(self, user_id):
        return self.session.query(Pot, Plant) \
            .outerjoin(PlantInPot, PlantInPot.pot_id == Pot.id) \
            .outerjoin(Plant, Plant.id == PlantInPot.plant_id) \
            .filter(Pot.user_id == user_id) \
            .all()

    def get_by_id(self, pot_id, user_id):
        return self.session.query(Pot, PlantInPot, Plant) \
            .outerjoin(PlantInPot, Pot.id == PlantInPot.pot_id) \
            .outerjoin(Plant, Plant.id == PlantInPot.plant_id) \
            .order_by(PlantInPot.planted_datetime.desc()) \
            .filter(Pot.id == pot_id).filter(Pot.user_id == user_id) \
            .first()

    def update_name(self, pot_id, new_name):
        pot = self.session.query(Pot).get(pot_id)
        pot.name = new_name
        self.session.commit()

   
  
