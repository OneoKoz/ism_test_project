import configparser

class ConfigReader:
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(ConfigReader, self).__new__(self)
        return self.instance

    def __init__(self, path='./config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(path)

config = ConfigReader().config
