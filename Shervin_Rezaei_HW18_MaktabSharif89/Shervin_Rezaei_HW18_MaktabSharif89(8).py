from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['mflix']
collection = database['movies']
films = database.movies.aggregate([
    { '$unwind': '$languages' },
    { '$group': { '_id': '$languages', 'average_rating': { '$avg': '$imdb.rating' } } },
])
for film in films:
    print(film)
