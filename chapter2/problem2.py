 # Write a program in the language of your choice
 # that will remove the grade of type "homework"
 # with the lowest score for each student from the dataset in the handout.
 # Since each document is one grade, it should remove one document per student.
 # This will use the same data set as the last problem, but if you don't have it,
 # you can download and re-import

import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)


def find_all_hw_assignments():
    db = connection.students
    grades = db.grades

    try:
        for i in range(0,200,1):
            homework = grades.find({'type': 'homework', 'student_id': i})
            if homework:
                array = []
                for hw in homework:
                    array.append(hw)

                if array[0]['score'] < array[1]['score']:
                    grades.delete_one({'_id':  array[0]['_id']})
                else:
                    grades.delete_one({'_id': array[1]['_id']})

    except Exception as e:
        print("Error", e)


find_all_hw_assignments()
