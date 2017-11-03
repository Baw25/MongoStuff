 # Write a program in the language of your choice
 # that will remove the grade of type "homework"
 # with the lowest score for each student from the dataset in the handout.
 # Since each document is one grade, it should remove one document per student.
 # This will use the same data set as the last problem, but if you don't have it,
 # you can download and re-import

import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)


# def remove_student(student_id):
#
#     # get a handle to the school database
#     db=connection.school
#     scores = db.scores
#
#     try:
#
#         result = scores.delete_many({'student_id':student_id})
#
#         print "num removed: ", result.deleted_count
#
#     except Exception as e:
#         print "Exception: ", type(e), e
#
# def find_student_data(student_id):
#     # get a handle to the school database
#     db=connection.school
#     scores = db.scores
#
#     print "Searching for student data for student with id = ", student_id
#     try:
#         docs = scores.find({'student_id':student_id})
#         for doc in docs:
#             print doc
#
#     except Exception as e:
#         print "Exception: ", type(e), e


def delete_lowest_grade():
    db = connection.mongo_test
    grades = db.grades

    try:
        result = grades.delete_many({'student_id':student_id})

        print("num removed: ", result.deleted_count)

    except Exception as e:
        print("Exception")

def find_all_hw_assignments():
    db = connection.mongo_test
    grades = db.grades

    try:
        homework = grades.find({'type': 'homework'})

        print("num removed: ", result.deleted_count)

    except Exception:
        print("Error")
