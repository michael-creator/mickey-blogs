import os


class Config:

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:mickey22@localhost/mickeypost'

  SECRET_KEY = os.environ.get('SECRET_KEY')
  # SQLALCHEMY_TRACK_MODIFICATION = True


class ProdConfig(Config):
  pass


class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:mickey22@localhost/mickeypost'

  DEBUG = True


config_options = {
  'development': DevConfig,
  'production': ProdConfig,

}
