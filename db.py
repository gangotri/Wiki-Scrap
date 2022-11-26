import pymongo

mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["TASK"] 
# create database withname "TASK"
collection = db["Scrap"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection.find({})
    return list(response)

def get_one(condition):
    response = collection.find_one({"title": condition})
    return response

def update(title, data):
    response = collection.update_one({"title": title}, {"$set": data})
    return response.modified_count

def delete(title):
    response = collection.delete_one({"title":title})
    return response.deleted_count