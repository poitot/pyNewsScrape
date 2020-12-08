from pymongo import MongoClient
import json

db_url = 'mongodb://localhost:27017/'

def saveObjToDB(coll, obj):
    """
    Saves an object to local Mongodb
    """
    collName = coll.title()
    try:
        client = MongoClient(db_url)
        db = client.test
        coll = db[coll]
        id_ = coll.insert_one(obj.__dict__).inserted_id
        str = "Object added successfull to test.{}. \n id: {} \n {}".format(collName, id_, obj)
        print(str)
    except:
        msg = 'EXCEPTION! \n Unable to add Object to test.{}. \n {}'.format(collName, obj)
        print(msg)

def getById(coll, id_):
    """
        Retrieves & returns an item from collection by id
    """
    collName = coll.title()
    try:
        client = MongoClient(db_url)
        db = client.test
        coll = db[coll]
        obj = coll.find_one(id_)
        print('Successfully got obj with id: {}'.format(id_))
        return obj
    except:
        msg = 'EXCEPTION! \n Unable to find Object with id: {} in test.{}.'.format(id_, collName)
        print(msg)
        
#item = getById('test_article', '5f9e1f246cf5e9967c4f9d82')
#print(item)
#saveToDB('test_articles', article)
