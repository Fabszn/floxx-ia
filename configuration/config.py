import json
import os


class CellarConfig:
    key = None
    user = None
    url = None

    def __init__(self, _key: str, _user: str, _url: str):
        self.key = _key
        self.user = _user
        self.url = _url


class LocalConfig:
    path: str = None

    def __init__(self, _path: str):
        self.path = _path


class AppConfig:
    config = None

    def __init__(self, path):
        with open(path, 'r') as json_file:
            self.config = json.load(json_file)

    def environment(self) -> str:
        var_environment: str = os.environ.get("FLOXX_IA_ENVIRONMENT")
        if var_environment is not None:
            return var_environment
        else:
            return self.config['environment']

    def cellarconfig(self) -> CellarConfig:
        return CellarConfig(self.config['cellar']['key'],
                            self.config['cellar']['user'],
                            self.config['cellar']['url'])

    def localconfig(self) -> LocalConfig:
        return LocalConfig(self.config['local']['path'])
