from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.mflix
pipline = [
    {'$match': {
        '$and': [
            {'year':{'$type': 'int'}},
            {'$expr': {'$gt':['year', 1990]}},
            ]
        },
    },
    {
    '$project':{'_id':0, 'title':1, 'year':1}
    }]
movies = database.movies.aggregate(pipline)
for movie in movies:
    print(movie)
