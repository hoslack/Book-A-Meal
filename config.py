import os


class Config(object):
    SECRET = os.getenv('SECRET')
