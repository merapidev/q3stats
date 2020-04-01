from repository.rawdata import RawData
from .base import Process as BaseProcess


class Parser(BaseProcess):

    def execute(self):
        raw_data_repository = self.repositories.get(RawData)
