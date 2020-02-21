import pymongo


class Storage(object):

    def __init__(self, db_config):
        self.client = pymongo.MongoClient(db_config['host'], db_config['port'])
        self.db = self.client[db_config['db']]

        self.collection = None

    def set_up_collection(self, collection_name):
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        self.collection.insert_one(document)
