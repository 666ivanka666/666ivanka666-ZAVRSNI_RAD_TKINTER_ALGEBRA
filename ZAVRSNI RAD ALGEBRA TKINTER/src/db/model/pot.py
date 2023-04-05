from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.session import Base


class Pot(Base):
    __tablename__ = "pots"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
  

    plants = relationship("Plant", secondary="plants_in_pots", back_populates="pots")

    def __str__(self):
        return f"{self.id} {self.user_id} {self.name}"
    
 
