# from pymongo import MongoClient
# from pymongo.server_api import ServerApi
# from notes import CLOUD_MONGO_URI
# # uri = "mongodb+srv://Valerii:Peremoga2024@cluster1.3egn3sy.mongodb.net/?retryWrites=true&w=majority"

# def get_mongodb():
#     client = MongoClient(uri, server_api=ServerApi('1'))
#     db = client.hw
#     return db


from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

CLOUD_MONGO_URI = os.getenv('CLOUD_MONGO_URI')


def get_mongodb():
    client = MongoClient(CLOUD_MONGO_URI, server_api=ServerApi('1'))
    db = client.hw
    return db
