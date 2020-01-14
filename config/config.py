import yaml


class Config(object):
    """Configuration"""

    def __init__(self, filename):
        self.configuration = self.load_configuration(filename=filename)

    def load_configuration(self, filename):
        with open(filename, "r") as stream:
            return yaml.load(stream, Loader=yaml.FullLoader)

    @property
    def files_directory(self):
        return self.configuration['files_directory']

    @property
    def logs(self):
        return self.configuration['logs']

    @property
    def mongodb(self):
        return self.configuration['mongodb']
