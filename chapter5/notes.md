# Ch 5. Aggregation methods:

How do we use group by or aggregation methods from SQL in MongoDB?

We use the aggregations!

Ex)

Ex collection:

{
  'name':'iPad 16GB Wifi',
  'manufacturer':"Apple",
	'category':'Tablets',
	'price':499.00
}

Use aggregation framework to calculate number of products manufactured by each
manufacturer

use agg
db.products.aggregate([
    {$group:
     {
	      _id:"$manufacturer",
	       num_products:{$sum:1}
     }
    }
])

- aggregate takes an array of object commands
- $group is one of the commands but there could be more
- the query above groups by manufacturer --> _id is required for the agg queries
  and the thing you group by is used
- adding a field called num_products which calculates the sum or count of each manufacturer

ex)
Finding the number of products by category

db.products.aggregate([
    {$group:
     {
	      _id:"$category",
	       num_products:{$sum:1}
     }
    }
])

Does the same thing as above


## How does the aggregation pipeline work?

A. Query goes through series of stages

ex)

Collection (begin) --> $project --> $match --> $group --> $sort --> result

- stages can appear multiple times

What does each stage do typically?

$project --> reshapes the document --> select out and only include certain fields
- for every document coming into the projection stage, there will be one leaving
- stage is therefore 1 : 1

$match --> filtering out the number of documents based on a criterion
- stage is n : 1

$group - aggregate
- stage is n : 1

$sort - sorts in an order
- stage is 1:1 every document that goes in comes out

$skips --> skips
- n : 1

- $limit --> limits the number of documents being pushed forward
- n : 1

$unwind - flattens the data
- n : 1

$out - taking the output of the aggregation
- 1:1

$redact - limit the documents certain users can see

$geoNear - geoNear performs location based queries



## How does it work?

ex)
Finding the number of products by category

db.products.aggregate([
    {$group:
     {
	      _id:"$category",
	       num_products:{$sum:1}
     }
    }
])

It's looking through all documents and looks at the categories
- first one is tablets
- then creates a resulting document based on the first document viewed
{
 _id: 'tablets',
  num_products: 1
}
- by looking at the first document, it notices that count for category tablets doesn't exist yet so it creates the above. If it did exist, then it would add to the count; it searches by _id to see if it exists

- afterward, you get a collection of resulting documents that can be run into the next stage of the aggregation


#ex problem

db.stuff.find()
{ "_id" : ObjectId("50b26f9d80a78af03b5163c8"), "a" : 1, "b" : 1, "c" : 1 }
{ "_id" : ObjectId("50b26fb480a78af03b5163c9"), "a" : 2, "b" : 2, "c" : 1 }
{ "_id" : ObjectId("50b26fbf80a78af03b5163ca"), "a" : 3, "b" : 3, "c" : 1 }
{ "_id" : ObjectId("50b26fcd80a78af03b5163cb"), "a" : 3, "b" : 3, "c" : 2 }
{ "_id" : ObjectId("50b26fd380a78af03b5163cc"), "a" : 3, "b" : 5, "c" : 3 }

How many documents will be yielded from the query below?

db.stuff.aggregate([{$group:{_id:'$c'}}])

--> 3 because it only grabs the _id of


## What if you want to group by multiple keys?

You can do the following for the products collection:

use agg
db.products.aggregate([
    {$group:
       {
  	      _id: {
            'manufacturer':"$manufacturer",
            "category" : "$category"
            },
  	         num_products:{$sum:1}
       }
    }
])

- the above query groups by manufacturer and category and creates counts for each
Thus the result will be counts for every combination of manufacturer and category

- what you name the key above in the _id is arbitrary

## The _id can be a complex document:

db.foo.insert({_id: {name: Andrew, class: m101}, hometown: NY })

## What are some other functions that exist in the grouping stage of the agg?

$sum - counting
$avg - mean
$min - min
$max - max
$push - encountering a certain value and push into an array
$addtoset - similar to push but only pushes if unique
$first - finding first value of a key in document set
$last - finding last value of a key in a doc set


## What if you want to sum something else?

ex)

use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 sum_prices:{$sum:"$price"}
     }
    }
])

In this case, your grouping by the manufacturer, but instead of counting the total in each
group, you sum the prices into a field called sum_price

Quiz problem zips:

db.zips.aggregate([
    {$group:
     {
	 _id: {
	     "state":"$state"
	 },
	 population:{$sum:"$pop"}
     }
    }
])

db.zips.aggregate([{"$group":{"_id":"$state", "population":{$sum:"$pop"}}}])

In this case you don't need to use the compound _id field; you can just use
"_id": "$state"

Using avg:

use agg
db.zips.aggregate([
    {$group:
     {
    	 _id: {
    	     "state":"$state"
    	 },
    	  average_pop:{$avg:"$pop"}
     }
    }
])

Group Stages OR Double grouping:

ex)
The query below takes the many scores of a student for each class they are in
and first groups performs a compound group of the student's avg score in a certain class. The
student will have more than one score in each class and will be in more than one class.


use agg
db.grades.aggregate([
    {'$group':
      {_id:{
          class_id:"$class_id",
          student_id:"$student_id"
          },
      'average':{
          "$avg":"$score"
        }
      }
    },
    {'$group':
      {_id:"$_id.class_id",
        'average':{
          "$avg":"$average"
          }
      }
    }
])


## How to unwind:

This is what it does:

{a: 1, b: 2, c: ['apple', 'pear', 'orange']}
||
{a: 1, b: 2, c: 'orange'}
{a: 1, b: 2, c: 'apple'}
{a: 1, b: 2, c: 'pear'}

HW 5.1:

use agg
db.posts.aggregate([
    {"$unwind": "$comments"},
    {$group:
     {
    	 _id: {
    	     "author":"$comments.author"
    	 },
    	  comment_count:{$sum:1}
     }
    }
])

db.zips.aggregate([
    {$match: {
      $and: [
      {"state": {
        "$in": ["NY", "CA"]
        }
      },
      {
        "pop": { $gte: 25000 }
      }
      ]
    }
  },
  {'$group':{'_id':'$state', 'average':{$avg:'$pop'}}}
])


HW 5.2  

Please calculate the average population of cities in California (abbreviation CA) and New York (NY) (taken together) with populations over 25,000.


use agg
db.zips.aggregate([{$match: {state: "CA"}}, {$match: {state: "NY"}}])

db.zips.aggregate([
    {$match:
     {
	 state:"NY",
   state: "CA"
     }
    },
    {$group:
     {
	 _id: "$city",
	 population: {$sum:"$pop"},
	 zip_codes: {$addToSet: "$_id"}
     }
    }
])


use agg
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    },
    {$group:
     {
	 _id: "$city",
	 population: {$sum:"$pop"},
	 zip_codes: {$addToSet: "$_id"}
     }
    }
])


Some students have three homework assignments, etc.
Your task is to calculate the class with the best average student performance. This involves calculating an average for each student in each class of all non-quiz assessments and then averaging those numbers to get a class average. To be clear, each student's average includes only exams and homework grades. Don't include their quiz scores in the calculation.

What is the class_id which has the highest average student performance?

You need to group twice to solve this problem. You must figure out the GPA that each student has achieved in a class and then average those numbers to get a class average. After that, you just need to sort. The class with the lowest average is the class with class_id=2. Those students achieved a class average of 37.6

ex) One document

Steps:
- flatten the scores array
- match all documents that are in type exam, homework
- group by student_id and class_id
- Calculate avg for each document
- group again by class_id
- take the avg for all students under class_id
- sort the avg scores for each class_id in descending order

{
	"_id" : ObjectId("50b59cd75bed76f46522c352"),
	"student_id" : 0,
	"class_id" : 24,
	"scores" : [
		{
			"type" : "exam",
			"score" : 4.444435759027499
		},
		{
			"type" : "quiz",
			"score" : 28.63057857803885
		},
		{
			"type" : "homework",
			"score" : 86.79352850434199
		},
		{
			"type" : "homework",
			"score" : 83.9164548767836
		}
	]
}

db.grades.aggregate([
    {"$unwind": "$scores"},
    {$match:{"scores.type":{"$in": ["exam", "homework"]}}},
    {$group:
     {
    	 _id: {
    	     "student_id":"$student_id",
           "class_id":"$class_id"
    	 },
    	  std_class_avg:{$avg:"$scores.score"}
     }
    },
    {$group:
      {
        _id: {
          "class_id":"$_id.class_id"
        },
         class_avg:{$avg:"$std_class_avg"}
      }
    },
    {'$sort':{'class_avg':-1}}  
])


Substring problem:

In this problem you will calculate the number of people who live in a zip code in the US where the city starts with one of the following characthers:

B, D, O, G, N or M .

db.zips.aggregate([
    {$project:
     {
    first_char: {$substr : ["$city",0,1]},
     }
   }
])


Using the aggregation framework, calculate the sum total of people who are living in a zip code where the city starts with one of those possible first characters. Choose the answer below

You will need to probably change your projection to send more info through than just that first character. Also, you will need a filtering step to get rid of all documents where the city does not start with the select set of initial characters.

Steps:
-


db.zips.aggregate([
    {$project:
     {
       first_char: {$substr : ["$city",0,1]},
       pop: "$pop",
       state: "$state"
     }
   },
   {$match:{"first_char":{"$in": ["B", "D", "O", "G", "N", "M"]}}},
   { $group: { _id : null, sum : { $sum: "$pop" } } }
])
