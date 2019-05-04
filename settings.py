import os
from os.path import join, dirname, abspath
from configparser import ConfigParser

current_dir = dirname(__file__)

config = ConfigParser()
config.read('utility.cfg')

mode = os.getenv('MODE')

if mode:
    MONGO_HOST = config[mode]['MONGO_HOST']
    MONGO_PORT = int(config[mode]['MONGO_PORT'])
else:
    MONGO_HOST = config['DEV']['MONGO_HOST']
    MONGO_PORT = int(config['DEV']['MONGO_PORT'])

MAP_API_KEY = config['APIKEYS']['MAP_API_KEY']

DATA_DIR = config["PATH"]["DATA_DIR"]
CALIFORNICATION = config["PATH"]["CALIFORNIA_LOCATION"]

data_dir = abspath(join(current_dir, DATA_DIR))
CALIFORNICATION = join(data_dir, CALIFORNICATION)