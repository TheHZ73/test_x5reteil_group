import configparser


class Config:
    def __init__(self, path):
        self._config = configparser.ConfigParser()
        self._config.read(path, encoding='utf-8')

    def get(self, key):
        value = self._config.get("Settings", key)
        return value
