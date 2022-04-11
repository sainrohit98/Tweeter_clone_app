import os
from dotenv import load_dotenv

load_dotenv('.env')


class Config(object):
    DEBUG = False
    ENV = os.getenv('ENV', 'development')


class ProductionConfig(Config):
    API_KEY = os.getenv('API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')


class DevelopmentConfig(Config):
    DEBUG = True
    API_KEY = os.getenv('API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')


class TestingConfig(Config):
    DEBUG = True
    API_KEY = os.getenv('API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')

