# Ch2 Notes

## Inserting data

Commands:
- insertOne()
ex) db.teams.insertOne({"name" : "Trojans"})

- insertMany()

db.teams.insertMany(
  [
    {"name" : "Bruins"},
    {"name" : "SunDevils"},
    {"name" : "WildCats"},
    {"name" : "Buffalo"},
    {"name" : "Utes"}   
  ]
)

When inserting, if you don't specify an _id, MongoDB will automatically specify one for you

All _id's must be unique; if not then there will be a "WriteError"


Upserts commands also be used to insert

The _id field:

ObjectId: How is it composed?

Date | Mac Address | PID | Counter --> 12 byte string


## Valid Read queries:

db.teams.find({"team.player": "Test"}) --> You can use dot notation fields

Eqality matches types:
- matches on entire array
- matches based on any element
- matches based on a specific element
- more complex matches using an operator

db.find({"actor": "Jeff Bridges"}) --> find any document containing Jeff Bridges in the array of actors

db.find({"actor.0": "Jeff Bridges"}) --> find any document containing Jeff B. as first element in array of actors

db.collection.find({}) --> returns a cursor with a certain number of documents

Cursors and projection:

db.teams.find({"rated": "PG-13"}, {"title": 1, "_id": 0}) --> returns documents rated PG-13 with only the title without the id

- use 0 to exclude fields at the end
- use 1 to include them

## Comparison Operators examples:

db.movieDetails.find({ runtime: { $gt: 90 } }).count() --> find movies with runtimes greater than 90 minutes

db.movieDetails.find({ runtime: { $gt: 90, $lt: 120 } }).count() --> find movies with runtimes greater than 90 minutes and less than 120 minutes

db.movieDetails.find({ "tomato.meter": { $gte: 95 }, runtime: { $gt: 180 } }) --> find movies with a tomato rating of greater than 95 and a runtime of 180

db.movieDetails.find({ rated: { $ne: "UNRATED" } }).count() --> finding movies that rated because they aren't "UNRATED" and returns count

db.movieDetails.find({ rated: { $in: ["G", "PG"] } }).pretty() --> finding movies that are rated G or PG

db.movieDetails.find({ rated: { $nin: ["PG-13", "R"] } }).pretty() --> finding movies that are NOT rated PG-13 or R

List of comparison operators:
$gte - greater than or equal
$gt - greater than
$lte - less than or equal to
$lt - less than
$eq - equal to these values
$in - in the array
$nin - not in the array

db.teams.find({"tomato.meter": {$exists: true}}) --> retrieve all movie documents containing a tomato meter

db.teams.find({"tomato.meter": {$exists: false}}) --> retrieve all movie documents NOT containing a tomato meter



HW:

db.grades.aggregate([
  {'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}},
  {'$sort':{'average':-1}}, {'$limit':1}
])

db.grades.aggregate([
  {'$match': {'type': 'exam', 'score': {$gte: 65 }}},
  {'$group':{'_id':'$student_id'}},
  {'$sort':{'score':-1}}, {'$limit':1}
])

db.grades.aggregate([
  {'$match': {'type': 'exam', 'score': {$gte: 65 }}},
  {'$group':{'_id':'$student_id'}}
])

 Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest.

 db.grades.aggregate([
   {'$match': {'type': 'exam', 'score': {$gte: 65}}}
   {'$sort':{'score':-1}},
 ])

 db.grades.aggregate([
   {'$match': {'type': 'homework'}},
   {
     $group:
       {
         _id: "$student_id",
         minScore: { $min: "$score" }
       }
   }
])


 Write a program in the language of your choice that will remove the grade of type "homework" with the lowest score for each student from the dataset in the handout. Since each document is one grade, it should remove one document per student. This will use the same data set as the last problem, but if you don't have it, you can download and re-import
