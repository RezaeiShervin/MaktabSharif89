from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['mflix']
collection = database['movies']
films = database.movies.aggregate([
    {'$unwind': '$cast'},
    {'$unwind': '$genres'},
    {'$group': {
        '_id': '$cast',
        'genres': {'$addToSet': '$genres'}
    }},
])

for film in films:
    print(film)

