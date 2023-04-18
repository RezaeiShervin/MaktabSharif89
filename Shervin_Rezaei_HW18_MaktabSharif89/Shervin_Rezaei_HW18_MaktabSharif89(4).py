from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.mflix
pipline = [
    {
    '$unwind':"$languages"
    },
    {'$group':
        { '_id': "$languages",
        'count': { '$sum': 1 }
        }
    }]
films = database.movies.aggregate(pipline)

for film in films:
    print(film)
