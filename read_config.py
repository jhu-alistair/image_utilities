import yaml

class ReadConfig:
    def __init__(self):
        strm = file("config.yaml", 'r')
        try:
            self.config = yaml.safe_load(strm)
        except yaml.YAMLError as exc:
            print(exc)
    def path(self):
        yield(self.config.items['path'])
