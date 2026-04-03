from app import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Users(db.Model):
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String(100), unique=True, nullable=False)
    name = db.Column(String(100), nullable=False)
    password = db.Column(String(200), nullable=False)
    phone = db.Column(String(20), nullable=True)
    type = db.Column(String(10), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'User {self.name} ({self.email})'