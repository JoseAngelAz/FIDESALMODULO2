class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'ClaveMasDificil'
    DEBUG = True
    TESTING = False
class ProductionConfig(BaseConfig):
    #Produccion configuracion
    DEBUG = False
    ENV = "production"
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    # DEBUG = True
    TESTING = True
    ENV = "development"
    SECRET_KEY = '123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ADA2021@localhost/aereolinea"
    # SQLALCHEMY_DATABASE_URI = "mssql+pymssql://user:password@192.168.1.20:1433/aerolinea"
