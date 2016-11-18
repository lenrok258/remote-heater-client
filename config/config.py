import json

__config = None

def read_config():
    if os.path.exists('config.json'):
        with open(path, 'r') as f:
            __config = json.load(f)
    else:
        raise MissingFileException("Missing config.json file")

def get():
    return __config

if not __config:
    read_config

