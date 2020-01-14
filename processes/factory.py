import os

from loguru import logger

from config import Config
from .loader import Loader
from .parser import Parser


class ProcessFactory(object):
    LOADER = 'loader'
    PARSER = 'parser'

    def __init__(self):
        self.config = Config(filename='config.yml')
        self.__init_logger(log_config=self.config.logs)

    def __init_logger(self, log_config):
        log_directory = os.path.abspath(log_config['directory'])
        log_path = os.path.join(log_directory, log_config['filename'])

        logger.configure(
            handlers=[dict(sink=log_path, enqueue=True, rotation="12:00", encoding='UTF-8')]
        )

    def get(self, process_type):
        processes = {
            self.LOADER: Loader,
            self.PARSER: Parser,
        }

        process_class = processes.get(process_type, None)

        if process_class is None:
            raise ModuleNotFoundError()

        return process_class(config=self.config)
