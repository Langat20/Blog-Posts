from distutils.debug import DEBUG
import os

class Config:
    SQLALCHEMY_DATABASE_URI ='postgres://pnrobfjltapagu:e8922689e3080afad5c58191c70dae74e4003a7911375b5e0baba6a71c3f0cd9@ec2-54-86-224-85.compute-1.amazonaws.com:5432/db4auqgv9jj3an'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/blogs'
    SECRET_KEY='qwertyqwerty'

    # email configurations
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kipkuruie7.lang@gmail.com'
    MAIL_PASSWORD = 'evanskip2015'
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
        '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

        uri = os.getenv("DATABASE_URL")  # or other relevant config var
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)

        SQLALCHEMY_DATABASE_URI=uri
    
DEBUG = True
   

class DevConfig(Config):
    
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:langat20@localhost/blogs'

    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}