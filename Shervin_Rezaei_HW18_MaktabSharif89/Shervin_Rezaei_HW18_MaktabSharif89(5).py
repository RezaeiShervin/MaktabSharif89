from pymongo import MongoClient, DESCENDING


client = MongoClient('localhost', 27017)
database = client.mflix
films = database.movies.find({},{'_id':0, 'title':1, 'num_mflix_comments':1}).sort('num_mflix_comments', DESCENDING).limit(1)

for film in films:
    print(film)
