import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Enable debug mode.
    DEBUG = True



# Development environment settings
class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')

# Development environment settings
class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL', None)
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', None)