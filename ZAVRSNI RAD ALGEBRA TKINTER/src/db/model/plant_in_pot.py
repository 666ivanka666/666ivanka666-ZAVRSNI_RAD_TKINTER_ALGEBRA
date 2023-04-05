from sqlalchemy import Column, Integer, DateTime, ForeignKey

from src.db.session import Base


class PlantInPot(Base):
    __tablename__ = "plants_in_pots"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(Integer, primary_key=True)
    planted_datetime = Column(DateTime, nullable=False)
    exhumed_datetime = Column(DateTime, nullable=True)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    pot_id = Column(Integer, ForeignKey("pots.id"))

    def __str__(self):
        return f"{self.id} {self.plant_id} {self.pot_id} {self.exhumed_datetime}"
