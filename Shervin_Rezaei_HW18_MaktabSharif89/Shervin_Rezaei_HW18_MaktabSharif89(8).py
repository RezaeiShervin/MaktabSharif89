from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mflix']
collection = db['movies']
movies = db.movies.aggregate([
    { '$unwind': '$languages' },
    { '$group': { '_id': '$languages', 'average_rating': { '$avg': '$imdb.rating' } } },
])
for movie in movies:
    print(movie)
