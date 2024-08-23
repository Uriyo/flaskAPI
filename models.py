from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    _email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contact = db.relationship('Contact', backref='owner', lazy=True)

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value.lower()

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    _email = db.Column(db.String(120))
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200))
    country = db.Column(db.String(50))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)
    deleted_at = db.Column(db.DateTime)

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value.lower()

    def delete(self):
        self.deleted_at = datetime.utcnow()
        db.session.commit()