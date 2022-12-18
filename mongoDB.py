import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://alindulceanu:nbmkn20QHyPWxK1x@cluster0.fewmezy.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection  = db['test']

post1 = {"_id": 1, "name": "Alin"}
post2 = {"_id": 2, "name": "Andrei"}



post_count = collection.count_documents({})
print(post_count)

