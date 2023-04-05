from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from src.db.session import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    admin = Column(Boolean, nullable=False)
    active = Column(Boolean, nullable=False)


    def valid_password(self, key, password):
        if len(password) < 3:
           return password

    pots = relationship("Pot", uselist=False, backref="user")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.admin} {self.active}"

