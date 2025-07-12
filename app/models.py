from app import database as db

class Professional(db.Base):
    __tablename__ = 'professional'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(128), unique=True)
    items = db.relationship('Item', backref='professional')
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<Professional {self.name}!r>'

class Item(db.Base):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.Integer, unique=True)
    professional_id = db.Column(db.Integer, db.ForeignKey('professional.id'))
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'<Item {self.name}!r>'


