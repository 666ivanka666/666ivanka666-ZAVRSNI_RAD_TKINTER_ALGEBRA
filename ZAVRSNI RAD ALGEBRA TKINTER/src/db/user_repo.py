from src.db.model.user import User
from sqlalchemy import func


class UserRepo:

    def __init__(self, session):
        self.session = session

    def insert_user(self, user):
        self.session.add(user)
        self.session.commit()

    def check_credentials(self, username, password):
        return self.session.query(User).filter(User.username == username,
                                               User.password == password, 
                                               User.active).one_or_none()