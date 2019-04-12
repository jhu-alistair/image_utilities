import yaml

configs = []
with open("config.yaml", 'r') as stream:
    try:
        configs = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


print(configs['path'])
