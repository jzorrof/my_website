# -*- coding: utf-8 -*-
__author__ = 'joe_fan'
"""
mongodb module
"""
URL = ''

from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

def dbconnction(url=''):
    client = MongoClient(url)
    return client

def dbqurey():
    db =dbconnction(URL)
    cursor = db.restaurants.find().sort(
    [
        ("borough", ASCENDING),
        ("address.zipcode", DESCENDING)
    ]
    )
    return cursor

cursor = dbqurey()

for i in cursor:
    print i


