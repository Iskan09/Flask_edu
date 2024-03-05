from datetime import datetime

from config import app, db


class Users(db.Model):
    __table_args__ = {'extend_existing': True}

    """Модель описания пользователей."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(30), unique=True)


class Flat(db.Model):
    """Модель описания квартир."""

    __table_args__ = {'extend_existing': True}
    price: int = db.Column(db.String(50), unique=True)
    Square: int = db.Column(db.String(50), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    bathroom: int = db.Column(db.String(50), unique=True)
    period: int = db.Column(db.String(50), unique=True)
    structure_house: str = db.Column(db.String(100), unique=True)
    floor: str = db.Column(db.String(100), unique=True)
    city: str = db.Column(db.String(100), unique=True)
    rooms: str = db.Column(db.String(50), unique=True)
    datatime: str = db.Column(db.String(50), unique=True)
    area: str = db.Column(db.DateTime, default=datetime.utcnow, )
