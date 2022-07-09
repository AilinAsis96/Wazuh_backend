from decouple import config

##Configs 

class Config: 
    SECRET_KEY= config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}