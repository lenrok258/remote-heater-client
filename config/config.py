import json
import os.path

__CONFIG_FILE_PATH = 'config.json'

config = None
DEBUG_ENABLED = True


def __read_config():
    base_path = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(base_path, __CONFIG_FILE_PATH))

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            global config
            config = json.load(f)
    else:
        raise Exception("Missing %s file" % __CONFIG_FILE_PATH)


if config is None:
    __read_config()
