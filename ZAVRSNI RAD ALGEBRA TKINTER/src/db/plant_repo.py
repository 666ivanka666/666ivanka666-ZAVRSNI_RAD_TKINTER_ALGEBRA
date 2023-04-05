from src.db.model.plant import Plant


class PlantRepo:
    def __init__(self, session):
        self.session = session

    def insert_plant(self, plant):
        self.session.add(plant)
        self.session.commit()

    def get_all_plants(self):
        return self.session.query(Plant).all()

    def get_by_id(self, plant_id):
        return self.session.query(Plant).get(plant_id)
     
    def update_plant(self, plant):
        self.session.merge(plant)
        self.session.commit()
        
