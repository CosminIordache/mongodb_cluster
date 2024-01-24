from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError

#Try connection
try:
    client = MongoClient('mongodb URL connection', serverSelectionTimeoutMS=5000)
    db = client['testDB']
    collection = db['testCollection']
    collection.insert_one({"name": "Example1", "value": 1234})

except ConnectionFailure:
    print("FFail connecting to MongoDB.")
except PyMongoError as e:
    print(f"PyMongo Error: {e}")
finally:
    client.close()
