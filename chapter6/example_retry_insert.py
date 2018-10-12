
import pymongo
import sys
import time

c = pymongo.MongoClient(host=["mongodb://localhost:27017",
                              "mongodb://localhost:27018",
                              "mongodb://localhost:27019"],
                        replicaSet="m101")

db = c.m101

things = db.things
things.delete_many({})   # remove all the docs in the collection


for i in range(0,500):
    for retry in range (3):
        try:
            things.insert_one({'_id':i})
            print "Inserted Document: " + str(i)
            time.sleep(.1)
            break
        except pymongo.errors.AutoReconnect as e:
            # This happens during failovers
            print "Exception ",type(e), e
            print "Retrying.."
            time.sleep(5)
        except pymongo.errors.DuplicateKeyError as e:
            # This could happen after a failover when data could be inserted twice 
            print "duplicate..but it worked"
            break
