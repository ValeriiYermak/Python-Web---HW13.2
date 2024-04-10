import json
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

CLOUD_MONGO_URI = os.getenv('CLOUD_MONGO_URI')

client = MongoClient(CLOUD_MONGO_URI, server_api=ServerApi('1'))
db = client.hw

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
