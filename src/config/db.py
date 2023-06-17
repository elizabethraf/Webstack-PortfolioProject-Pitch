#!/usr/bin/env python3
"""Configuring database access"""
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
from os import getenv

load_dotenv()
DBSERVER = getenv('DBSERVER')
DBUSER = quote_plus(str(getenv('DBUSER')))
DBPASS = quote_plus(str(getenv('DBPASSWORD')))

conn_string = 'mongodb+srv://{}:{}@{}/?retryWrites=true&w=majority'.format(DBUSER, DBPASS, DBSERVER)
client = MongoClient(conn_string)
db = client['streetvendors']
vendor_coll = db['vendors']
product_coll = db['products']

