import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.mongo_test

teams = db.teams

item = teams.find_one()

print(item['name'])
