from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from src.db.session import Base


class Plant(Base):
    __tablename__ = "plants"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(Integer, primary_key=True)
    plant_name = Column(String, nullable=False)
    desired_ph_value = Column(Integer, default=7.0)
    image_path = Column(String, nullable=False)
    days_to_water = Column(Integer, nullable=False)
    likes_shade = Column(Boolean, nullable=False)
    substrate = Column(String, nullable=False)
    required_illumination = Column(Integer, nullable=False)
 


    pots = relationship("Pot", secondary="plants_in_pots", back_populates="plants")

