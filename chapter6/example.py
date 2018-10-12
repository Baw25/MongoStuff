import pymongo
import sys

# Below you are connecting to 3 instances of Mongo using the replicaSet database m101
# You then set w=1 j=True guarenteeing that the insert has been written to disk
c = pymongo.MongoClient(host=["mongodb://localhost:27017",
                              "mongodb://localhost:27018",
                              "mongodb://localhost:27019"],
                               replicaSet="m101",
                              w=1,
                              j=True)

db = c.m101
people = db.people

try:
    print "inserting"
    people.insert_one({"name":"Andrew Erlichson", "favorite_color":"blue"})
    print "inserting"
    people.insert_one({"name":"Richard Krueter", "favorite_color":"red"})
    print "inserting"
    people.insert_one({"name":"Dwight Merriman", "favorite_color":"green"})
except Exception as e:
    print "Unexpected error:", type(e), e
print "completed the inserts"
