# Challenge problem 1

# Suppose our movie details documents are structured so that rather than contain an
# awards field that looks like this:

# "awards" : {
#     "wins" : 56,
#     "nominations" : 86,
#     "text" : "Won 2 Oscars. Another 56 wins and 86 nominations."
# }
# they are structured with an awards field as follows:
#
# "awards" : {
#     "oscars" : [
#         {"award": "bestAnimatedFeature", "result": "won"},
#         {"award": "bestMusic", "result": "won"},
#         {"award": "bestPicture", "result": "nominated"},
#         {"award": "bestSoundEditing", "result": "nominated"},
#         {"award": "bestScreenplay", "result": "nominated"}
#     ],
#     "wins" : 56,
#     "nominations" : 86,
#     "text" : "Won 2 Oscars. Another 56 wins and 86 nominations."
# }

# What query would we use in the Mongo shell to return all movies in the video.movieDetails
# collection that either won or were nominated for a best picture Oscar? You may assume that
# an award will appear in the oscars array only if the movie won or was nominated. You will probably
# want to create a little sample data for yourself in order to work this problem.

# Answer 1
db.movieDetails.find({"awards.oscars": {"$in": [{"award": "bestPicture", "result": "won"}, {"award": "bestPicture", "result": "nominated"}]} })

            # {"award": "bestPicture", "result": "nominated"},
                        # {"award": "bestSoundEditing", "result": "nominated"},
#
#

# sample data:

import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.video
movies = db.movieDetails

test = {
	"title" : "Movie 3",
	"year" : 2005,
	"rated" : "R",
	"runtime" : 175,
	"countries" : [
		"Sout Africa",
		"USA",
		"Spain"
	],
	"genres" : [
		"Western"
	],
	"director" : "Sergio Leone",
	"writers" : [
		"Sergio Donati",
		"Sergio Leone",
		"Dario Argento",
		"Bernardo Bertolucci",
		"Sergio Leone"
	],
	"actors" : [
		"Claudia Cardinale",
		"Henry Fonda",
		"Jason Robards",
		"Charles Bronson"
	],
	"plot" : "Epic story of working for the railroad.",
	"poster" : "http://ia.media-imdb.com/images/M/MV5BMTEyODQzNDkzNjVeQTJeQWpwZ15BbWU4MDgyODk1NDEx._V1_SX300.jpg",
	"imdb" : {
		"id" : "tt0064116",
		"rating" : 8.6,
		"votes" : 201283
	},
	"tomato" : {
		"meter" : 98,
		"image" : "certified",
		"rating" : 9,
		"reviews" : 54,
		"fresh" : 53,
		"consensus" : "A landmark Sergio Leone spaghetti western masterpiece featuring a classic Morricone score.",
		"userMeter" : 95,
		"userRating" : 4.3,
		"userReviews" : 64006
	},
	"metacritic" : 80,
    "awards" : {
        "oscars" : [
            {"award": "bestAnimatedFeature", "result": "won"},
            {"award": "bestPicture", "result": "nominated"},
            {"award": "bestMusic", "result": "won"},
            {"award": "bestScreenplay", "result": "nominated"}
        ],
        "wins" : 23,
        "nominations" : 32,
        "text" : "Won 2 Oscars. Another 23 wins and 32 nominations."
    },
	"type" : "movie"
}

movies.insert(test)

print('done')
