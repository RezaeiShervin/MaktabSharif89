from pymongo import MongoClient


client = MongoClient('localhost', 27017)

database = client.mflix
films = database.movies.find({'genres': 'History'}, {'_id': 0, 'title': 1})
for film in films:
    print(film)






