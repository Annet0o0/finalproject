import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///films.db'
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # os.getenv('SQLALCHEMY_DATABASE_URI')