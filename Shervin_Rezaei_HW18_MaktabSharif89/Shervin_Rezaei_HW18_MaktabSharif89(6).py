from pymongo import MongoClient


client = MongoClient('localhost', 27017)
database = client.mflix
pelham = database.movies.find_one({'title':'The Taking of Pelham 1 2 3'})
pipline = [
    {'$match':
     {
    'movie_id' : pelham['_id']
    }},
    {
    '$group':
            {
            '_id':'$name'
            }},
    {
    '$project':{'_id':1}
    }]
writers = database.comments.aggregate(pipline)

for writer in writers:
    print(writer)
