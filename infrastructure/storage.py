import pymongo


class Storage(object):

    def __init__(self, db_config):
        self.client = pymongo.MongoClient(db_config['host'], db_config['port'])
        self.db = self.client[db_config['db']]

        self.collection = None

    def get_collection(self, collection_name):
        return self.db[collection_name]
