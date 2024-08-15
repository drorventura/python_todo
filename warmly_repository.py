from bson import ObjectId
from pymongo import MongoClient, DESCENDING

client = MongoClient("mongodb://mongo:27017")
db = client["warmly"]
collection = db["activities"]

'''
Method to retrieve documents from collection
'''


def get_activities():
    return list(collection.find().sort("id", -1))


def get_collection():
    return collection

'''
Method to insert a document into collection
'''


def bulk_insert(activities):
    result = collection.insert_many(activities)
    return result.inserted_ids


def delete_activity(id):
    collection.delete_one({"_id": ObjectId(id)})


def put_activities(activities):
    collection.insert_one(activities)


def get_last_id():
    # Busca o documento com o maior valor de "id"
    last_activity = collection.find_one(sort=[("id", DESCENDING)])
    if last_activity:
        return last_activity["id"]
    return 0
