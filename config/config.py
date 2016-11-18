import json
import os.path

CONFIG_FILE_PATH = 'config.json'

config = None


def __read_config():
    base_path = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(base_path, CONFIG_FILE_PATH))

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            global config
            config = json.load(f)
    else:
        raise Exception("Missing %s file" % CONFIG_FILE_PATH)


if config is None:
    __read_config()
