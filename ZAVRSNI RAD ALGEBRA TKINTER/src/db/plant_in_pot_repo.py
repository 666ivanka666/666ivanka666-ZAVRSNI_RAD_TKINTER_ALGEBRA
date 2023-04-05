from src.db.model.plant_in_pot import PlantInPot


class PlantInPotRepo:
    def __init__(self, session):
        self.session = session

    def plant_plant_in_pot(self, plant_in_pot):
        self.session.query(PlantInPot).filter_by(pot_id=plant_in_pot.pot_id).delete()
        self.session.add(plant_in_pot)
        self.session.commit()
    
    def exhume_plant_from_pot(self, plant_in_pot, exhume_datetime):
        pip = self.session.query(PlantInPot).get(plant_in_pot)
        pip.exhumed_datetime = exhume_datetime
        self.session.commit()


    
