import os

class Config:
    
    SECRET_KEY = 'global_football'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:123456789@localhost/global_football'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_URL ='http://api.football-data.org/v2/competitions/'
    FOOTBALL_API_KEY ='060161c1c7814b35b3f438c8580388a2'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='test.user.python3.6@gmail.com'
    MAIL_PASSWORD='codingstudent001'


class DevConfig(Config):

    DEBUG = True
    ENV = 'development'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")




config_options = {'development': DevConfig, 'production': ProdConfig}