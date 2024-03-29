import os
import pymongo


class Database(object):
    URI = os.environ.get("MONGO_URI")
    DATABASE = None

    @staticmethod
    def initialise():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["full-stack"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
