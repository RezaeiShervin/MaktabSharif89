from pymongo import MongoClient

client = MongoClient('localhost', 27017)

database = client.mflix
pipline = [
    {'$unwind':'$cast'},
    {'$group':
        {
        '_id':'$cast',
        'count':{'$sum':1}
        }},
        {
        '$sort':{'count':-1}
        }]
actors = database.movies.aggregate(pipline)
for actor in actors:
    print(actor)
