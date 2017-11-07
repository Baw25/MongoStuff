# How to approach MongoDB schema design:

# Application Drive Schema:
It's most important to design your data in a way that's conducive to how your application works
Thus, there's no correct way to design your schema in MongoDb except that it must meet the business needs of your Application

MongoDB supports Rich Documents:
Advantages of MongoDB in schema design
--> pre-joining data for fast access
--> pre-embed data or storing a document inside a document
--> there's no constraints like in a relational database - no foreign key constraints
--> atomic operations
--> No declared structures (but must think of this ahead of time) (actually this is kind of nice)

3rd Normal Review:
The Third Normal Form is violated when an email of an author within a blog table is updated in one row containing the email
while another row containing the email is not updated

Rules of Normalization for Relational Databases:
1. Free database of modification anomolies
2. Supposed to minimize redesign when expanding - but is this true?
3. Avoid bias toward any particular access pattern

Do MongoDD documents get exposed to the dangers of unnormalization?

- Not necessarily because the fields for a document only appear once

Idea of creating a document for a sample blog application:

Model the data in such a way where a query on a collection will include all the information you need for a single page
within an application.

MongoDB also denormalizes in such a way that does not violate any of the advantages of a relational database


Alternative Schema for Blog:
- embed and pre-join data when you can to take advantage of MongoDB


MongoDB does not have Constraints and thus there will be no concept of a foreign key:
- there's no guarentee the correct post_id will appear in the appropriate comment collection for a comment belonging to a post - there's no guarentee that will be a post collection --> it's up to you keep your data consistent
(thee might be risk in this because there's no guarentee that data can be kept consistent)

- embedding helps when you can't guarentee foreign key constraints in MongoDB; thus it's best practice to embed

##Living without Transaction in MongoDB:

What makes transactions important?
They guarentee an operation will be totally complete or not complete at all - this includes a bank transaction where money is
wired from one person to another, it's either complete or not

How to mimic atomic operations or transactions in MongoDB:
1. Application code that mimics a transaction
2. Implement Locking in software
3. Tolerate some inconsistency

What are the atomic operations in MongoDB:
Atomic operations work differently in MDB than in normal relational databases in that the atomic operations occur on a single
document and people will not see the document until all the updates are made. Thus they will see all updates or no updates.
A write is an atomic operation


## One to One Relations in MongoDB:
The best way to illustrate 1-1 relationships in MongoDB is embed the document

But there are a couple of considerations:
1. Which of the documents is growing all the time? --> If the embedded document is growing all the time, then
2. How often will you access the two documents together
3. Atomicity of data - there's no transactions in MongoDB but atomic operations happen on a single document - thus you can have transactions with two documents if one is embedded within the other

Keep in mind that embedding can become dangerous if one of the two documents becomes too large

##One to Many Relations:

How should they be modeled in MongoDB?

Considerations:
A. If there are many documents for the one document (in a 1-many), then it worth stubbing the use of a foreign key
ex) City document --> _id: "NYC"

City has many people

Person document --> city_id: "NYC" which refers to the id of the city document

B. If your in a 1-few situation (many part is not very many documents)
then you should probably embed the documents - like a comment within a post


##Books to Authors:

Books and Authors collections (use as examples below)

Some many to many relationships are typically few-few

Options:

1. You can embed in both using an array of book_ids on the author and author_ids on the book

2. Another option is embedding within one using ids and embedding within the other using entire documents (not recommended)
This is typical for performance reasons

Considerations:
  Do you want the parent to exist before the child or vice versa (student-teacher)? Thus if you embed students within a teacher, the teacher must exist

##What the benefits of embedding?

A. Improved READ performance

HIGH Latency and HIGH bandwidth example --> it takes a long time for the computer disk to read the first document and then
the rest come quickly - must locate on the disk and then the rest of the information comes quickly afterward

Avoiding round trips to the database by embedding


##How to represent trees:

Ecommerce site:
Home: Outdoors, winter, snow

products and categories collections


Listing the ancestors and children of a certain document



# Gridfs
If your collection becomes larger than 16MB then GRIDFS is used to break up the blob of data into smaller chunks and stores
metadata for each collection
