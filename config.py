import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    # or 'a_very_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    # or 'postgresql://user:Zt5wYorpVSKXzV96Y9Y7KssyrwsUQ2yH@dpg-cqsurn5umphs73c49ha0-a.oregon-postgres.render.com/flask_contacts_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') 
    # or 'a_very_secret_jwt_key'


