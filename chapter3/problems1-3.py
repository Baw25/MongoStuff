
# {
#     "_id" : 137,
#     "name" : "Tamika Schildgen",
#     "scores" : [
#         {
#             "type" : "exam",
#             "score" : 4.433956226109692
#         },
#         {
#             "type" : "quiz",
#             "score" : 65.50313785402548
#         },
#         {
#             "type" : "homework",
#             "score" : 89.5950384993947
#         }
#     ]
# }

# Answer query
# db.students.aggregate([{ '$unwind': '$scores' }, { '$match' : { 'scores.type' : "homework" } }, {"$group": {'_id': '$_id', 'minHW': {"$min": "$scores.score"}}}])

import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)


def find_all_hw_assignments():
    db = connection.school
    students = db.students

    try:
        lowest_hw_scores = students.aggregate([{ '$unwind': '$scores' }, { '$match' : { 'scores.type' : "homework" } }, {"$group": {'_id': '$_id', 'minHW': {"$min": "$scores.score"}}}])
        for hw in lowest_hw_scores:
            print(hw['minHW'])
            students.update({"_id": hw['_id']}, {"$pull": {'scores': {'score': hw['minHW'] } } }, False, True)


    except Exception as e:
        print("Error", e)


find_all_hw_assignments()
