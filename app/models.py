from sqlalchemy import Column, Integer, String
from app.database import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Integer, unique=True)

    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'<Item {self.name}!r>'


