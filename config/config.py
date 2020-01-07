import yaml


class Config(object):
    """Configuration"""

    def __init__(self, filename):
        self.configuration = self.load_configuration(filename=filename)

    def load_configuration(self, filename):
        with open(filename, "r") as stream:
            return yaml.load(stream, loader=yaml.FullLoader)
