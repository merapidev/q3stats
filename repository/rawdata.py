from .base import Repository


class RawData(Repository):
    COLLECTION = 'rawdata'

    def insert_one(self, document):
        self.collection.insert_one(document)
