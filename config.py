class Config:
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://michael:joker@localhost/mickeypost'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'True'

class ProConfig(Config):
  pass
    
class DevConfig(Config):
    DEBUG = True
    
# config_options = {
#     'production' : ProdConfig,
#     'development': DevConfig
# }