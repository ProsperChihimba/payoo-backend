#application configuration according to the enviroment the application is running on
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ec9439cfc6c796ae2029594d'

#production environment
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:3102001prosper@database-1.cav39szbm4h3.us-east-2.rds.amazonaws.com:3306/walletapp'
    DEBUG = True

#development environment
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:3102001prosper@database-1.cav39szbm4h3.us-east-2.rds.amazonaws.com:3306/walletapp'
    SQLALCHEMY_ECHO = False

#testing environment
class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:3102001prosper@database-1.cav39szbm4h3.us-east-2.rds.amazonaws.com:3306/walletapp'
    SQLALCHEMY_ECHO = False