import os

class Config:
    
    SECRET_KEY = 'global_football'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:123456789@localhost/global_football'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_URL ='https://apiv3.apifootball.com/?action=get_countries&APIkey={}'
    FOOTBALL_API_KEY ='306537220f31131e7ffaa395a0a1f6869677028939925eaa1c8eb7532dfddcc8'

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