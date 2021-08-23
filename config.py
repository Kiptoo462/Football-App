class Config:
    
    SECRET_KEY = 'global_football'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:123456789@localhost/global_football'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):

    DEBUG = True


class ProdConfig(Config):
    pass


config_options = {'development': DevConfig, 'production': ProdConfig}