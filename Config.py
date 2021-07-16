from os import getenv
from os.path import isfile, exists
from dotenv import load_dotenv


class Config:
    def __init__(self, env_file=".env"):
        if isfile(env_file) and exists(env_file):
            load_dotenv(dotenv_path=env_file)

        self.ENV = getenv('ENVIRONMENT')
        self.SECRET_KEY = getenv('SECRET_KEY')
        self.SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
        self.SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
