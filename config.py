import os

class Config:

    
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://michael:mickey22@localhost/mickeypost'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  
class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://michael:mickey22@localhost/mickeypost'

class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    

   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://michael:mickey22@localhost/mickeypost'

DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}