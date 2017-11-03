
# What is MongoDB?

Documents ~ equivalent to model in OO programming

Advantages:
Much easier to shard data across multiple servers
Scaling out through sharding feature
Easier to store more than one model within a document through embedding

Overview of MondoDB:

Architecture:
MongoD - database server running out of box
mongo - database

Server:
- python Server
- bottle
- pymongo

front-end:
- UI

Inserting documents:
db.teams.insert({'name': 'Giants'});
db.teams.insert({'name': 'Eagles'});
db.teams.insert({'name': 'Redskins'});
db.teams.insert({'name': 'Cowboys'});
db.teams.insert({'name': 'Saints'});
db.teams.insert({'name': 'Falcons'});
db.teams.insert({'name': 'Panthers'});
db.teams.insert({'name': 'Bucs'});
db.teams.insert({'name': '49ers'});
db.teams.insert({'name': 'Rams'});
db.teams.insert({'name': 'Seahawks'});
db.teams.insert({'name': 'Cardinals'});
db.teams.insert({'name': 'Packers'});
db.teams.insert({'name': 'Vikings'});
db.teams.insert({'name': 'Bears'});
db.teams.insert({'name': 'Lions'});
db.teams.insert({'name': 'Raiders'});
db.teams.insert({'name': 'Chiefs'});
db.teams.insert({'name': 'Chargers'});
db.teams.insert({'name': 'Broncos'});
db.teams.insert({'name': 'Patriots'});
db.teams.insert({'name': 'Dolphins'});
db.teams.insert({'name': 'Bills'});
db.teams.insert({'name': 'Jets'});
db.teams.insert({'name': 'Colts'});
db.teams.insert({'name': 'Titans'});
db.teams.insert({'name': 'Texans'});
db.teams.insert({'name': 'Jaguars'});
db.teams.insert({'name': 'Steelers'});
db.teams.insert({'name': 'Ravens'});
db.teams.insert({'name': 'Browns'});
db.teams.insert({'name': 'Bengals'});


## What about BSON:

  Mongodb drivers send and receive data as BSON
  Stored as BSON
  Traversable
  Efficient --> encoding BSON is quick
  BSON extends the JSON data types to include:
  - binary data
  - integers
  - dates
  - etc

## CRUD Operations with MONGODB:

Reading:

find({}) --> takes param for field and data for that field as values
-- returns a cursor object



## Modeling the blog:

Relational DB design:

Models:
A. Posts
B. Comments
C. Authors
D. Tags
E. Post_comments
F. Post_tags


##Modeling the Blog as a document in MongoDB:
Posts:
{
  "title": "My Post",
  "body": " lafdjlakdsjflksdajflkdsjf",
  "author": "Blake Wills",
  "date": "05251990",
  "comments": [
    {'name': "UserTest1", "email": "me@example.com", "comment": "Hello Blake"}
  ]
}

Tags:
 {
   [
    {name:"cycling"}
  ]
 }

Authors:

{
 _id: kldsjfldksfj,
 "name": "Blake Wills",
 password: "Password1",
 ...
}

.
##Modeling your data:

To embed or to not embed?

Consider embedding if you need to access multiple tables at once while querying as opposed to accessing the different entities independently and at separate times. For the example of a blog and the entities involved, a blog document containing the tags and comments would make sense for this application because all tables are needed to render the blog. There will be few times where just the tags are needed or just the comments are needed. This is what makes the document advantageous as opposed to creating many joins with a relational database to get the data you want for a certain view.

What are scenarios where you can't embed?

16MB is exceeded for the embedded document

Other consideration when thinking about embedding:
- you can index subdocument so you shouldn't worry about having to index subdocs when considering to embed
- duplicating subdocs across the docs is normal and is supported in Mongo
- If you have data that is shaped differently, then this is not a reason to not embed
