from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['mflix']
collection = database['movies']
films = database.movies.aggregate([
    {'$unwind': '$cast'},
    {'$group': {
        '_id': '$cast',
        'genres': {'$addToSet': '$genres'}
    }},
])
for film in films:
    actorName = film['_id']
    genres = []
    for genre in film['genres']:
        genres.extend(genre)
    if genres:
        genres_str = ', '.join(set(genres))
    else:
        genres_str = 'Nothing'
    print(f"{actorName}: {genres_str}")
