
# Understanding the performance of the database

## Two options for performance enhancement
- indexing
- sharding

## How do storage engines work?
MongoDb offering pluggable storage engines

MongoDB Server --> Storage Engine --> Computer Disk

Application example

Driver (Pymongo) Reads and writes to Mongo Server
Mongo Server uses the Storage Engine to READ AND WRITE to disk

MongoDB offers pluggable storage engine which greatly determines how the database
will perform
Two main pluggable engines:
1. MMAP
2. WiredTiger

MMAP1:
- MongoDB needs a place to store the documents which are files on Disk

How does the MMAP work?
- MongoDB places documents inside files on disk

Allocation of 100GB File on Disk

MMAP system call maps the 100GB file into 100GB of virtual memory

Each virtual memory has different pages in memory

When reading a document on MongoDB, if it hits a page in memory (as determined by the OS)
then you get it a lot quicker than if it's not in memory. Thus it has to go to disk in order to bring it out

Collection Level Concurrency:
If you have two different operations going on at the same time, both can occur at the same time

In place updates are also allowed for MongoDB. This means a document is either updated in place or they mark it as a whole and move to somewhere else in memory


Power of two sizes when allocating the storage of a document in memory
creating a 3 byte document - will give you 4 bytes
7 --> 8
19 --> 32

Concept --> Database doesn't get to decide what winds up in memory and what winds up on disk

Now how does WiredTiger work?
A. Document level concurrency (MMAP doesn't do this)
B. Compression of data and indexes
C. Wire Tiger can actually manage it's own storage which allows it to compress

MongoDb can not start by using the same data directory as MMAPv1 or the data directory you typically point to when starting a mongod process

## How do indexes work?

Think of collection of documents on disk in arbitrary order

| | | | | | | | | | | | | | | | | |

{ name: "Blake Wills", DOB: "1990-05-20"}

Let's say you want to find the document with the name --> Blake Wills in a collection of 1 million documents

Instead of iterating through all million, let's that the names are indexed alphabetically
where a collection of documents with name starting with A are in the same area on disk and the same for the rest of the alphabet

Concept: Indexes are like ordered pointers for the documents

You want to place indexes on the things you are querying the most

## How does it work when you index on 2 different fields:

ex: name and DOB

(name, DOB) --> this can represent a single index entry

Indexes ABC
- you can search on
A
A & B
A & B & C
- you can't search on
B alone


Indexing slows down your writes because of the placement of the indexes
Reads become much faster however

Effective strategy:
- no indexes on collection at all before insertion
- insert the data
- then add the indexes and build the indexes afterward


## Creating Indexes:

What's a way to identify indexes for a simple query?

db.students.explain().find({student_id: '5'})

- tells you how the index performed
-

Adding a compound index:

db.students.explain(true).find({student_id: 5})
||
db.students.createIndex({student_id:1, class_id: -1})

index on the student_id and class_id
student_id --> ascending
class_id --> descending


## Viewing the existing indexes
db.students.getIndexes() --> gives the existing indexes

##Deleting indexes
db.students.dropIndex({student_id: 1})

## MultiKey Indexes --> Indexes on arrays
- creating indexes on arrays or with tags

ex) db.foo.insert({a:1, b:2})

db.foo.find()
{_id: jdfldsjfdlsfj, "a": 1, "b": 2}


You can add indexes on arrays and have more than one, but you can't index on
two arrays



Covered Queries:
- a query that is satisfied with 0 documents
-


Dot Notation indexing:

db.students.createIndex({'scores.score': 1})
