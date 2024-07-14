from os import getenv


class Config:
    APP_NAME = getenv('APP_NAME')
    APP_VERSION = getenv('APP_VERSION')
    FLASK_APP = getenv('FLASK_APP')
    FLASK_ENV = getenv('FLASK_ENV')
    REDIS_HOST = getenv('REDIS_HOST')
    REDIS_PORT = getenv('REDIS_PORT')
    REDIS_PWD = getenv('REDIS_PASSWORD')
    PG_USERNAME = getenv('DB_USER')
    PG_PASSWORD = getenv('DB_PASSWORD')
    PG_DATABASE = getenv('DB_NAME')
    PG_HOST = getenv('DB_HOST')
