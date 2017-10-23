import pymongo
import bottle

# from pymongo import MongoClient
# from bottle import route, run, template

@bottle.route('/home')

def index():
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.mongo_test
    teams = db.teams

    team = teams.find_one()

    return "<b>The %s is the best team in the NFL</b>" % team['name']

bottle.run(host='localhost', port=8082)
