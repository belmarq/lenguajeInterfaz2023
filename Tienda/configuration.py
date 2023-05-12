class Config(object):
    TESTING = False
    DEBUG = False
    # "mysql+pymysql://user:password@ip:3306/db_name"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/tiendita"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True