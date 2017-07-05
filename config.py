"""
Blood Glucose Tracker Configuration settings
"""

import os

__author__ = "Ken W. Alger"
__copyright__ = "Copyright 2017, Ken W. Alger"
__maintainer__ = "Ken W. Alger"
__email__ = "ken@kenwalger.com"

# Application Settings
DEBUG = True
HOST = '127.0.0.1'
PORT = 8000
CHARACTER_ENCODING = 'UTF-8'
SECRET_KEY = '209r8odhjvis7q*@)#%&SLJ:uufa;kdj:OIUSruq0ejlkJh:SFUUonl654adfALK3'
ATLAS_PASSWORD = os.environ.get('ATLAS_PASSWORD')
MONGO_DB_NAME = 'bgt_db'

# Database Settings for Atlas Cluster
MONGO_URI = 'mongodb://kenwalger:{}' \
            '@testing-cluster-shard-00-00-xhego.mongodb.net:27017,' \
            'testing-cluster-shard-00-01-xhego.mongodb.net:27017,' \
            'testing-cluster-shard-00-02-xhego.mongodb.net:27017/' \
            '{}?ssl=true&replicaSet=Testing-Cluster-shard-0' \
            '&authSource=admin'.format(ATLAS_PASSWORD, MONGO_DB_NAME)



