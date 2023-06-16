#!/usr/bin/env python3
"""Configuring database access"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
from os import getenv

DBSERVER = quote_plus(str(getenv('DBSERVER')))
DBUSER = quote_plus(str(getenv('USERNAME')))
DBPASS = quote_plus(str(getenv('PASSWORD')))

conn_string = 'mongodb://{}:{}@{}/?retryWrites=true&w=majority'.format(DBUSER, DBPASS, DBSERVER)
client = MongoClient(conn_string, server_api=ServerApi('1'))
db = client['streetvendors']
vendor_coll = db['vendors']
product_coll = db['products']

