import base64, os


class Config:
    DEBUG = True
    TEST = True
    SECRET_KEY = base64.b64encode(os.urandom(64)).decode('utf-8')
    SERVER_NAME = '127.0.0.1:5000'


class ProductionConfig(Config):
    DEBUG = False
    TEST = False
