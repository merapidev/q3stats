import os

from loguru import logger

from infrastructure.storage import Storage
from repository.repositories import Repositories


class Process(object):

    def __init__(self, config):
        self.config = config
        self.repositories = Repositories(Storage(config.mongodb))

    def run(self):
        logger.info("Process {0} has started. PID:{1}".format(self.__class__, os.getpid()))
        self.execute()
        logger.info("Process {0} has been ended. PID:{1}".format(self.__class__, os.getpid()))

    def execute(self):
        raise NotImplementedError()
