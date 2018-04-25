import os


class Config(object):
    SECRET = os.getenv('SECRET')
    SESSION_TYPE = os.getenv('SESSION_TYPE')

