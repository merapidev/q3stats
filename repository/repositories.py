from .base import Repository


class Repositories(object):

    def __init__(self, storage):
        self.storage = storage
        self.repositories = {}

    def get(self, repository_class):
        assert issubclass(repository_class, Repository)

        if not repository_class.COLLECTION in self.repositories:
            self.repositories.setdefault(
                repository_class.COLLECTION,
                repository_class(
                    collection=self.storage.get_collection(collection_name=repository_class.COLLECTION)
                )
            )

        return self.repositories.get(repository_class.COLLECTION)
