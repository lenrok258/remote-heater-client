#!./.env/bin/python

import time

import requests
from requests.exceptions import ConnectionError

import server_response_processor
import temp_sensor
from config.config import config
from logger import ErrorId
from logger import Logger
from server_response import UnknownCommandException

REQUEST_INTERVAL_SEC = 60
SERVER_URL = config['server']['url']

logger = Logger(__name__)


def sleep(seconds):
    time.sleep(seconds)


def get_current_temp():
    try:
        return temp_sensor.value()
    except Exception as e:
        logger.error("Cannot read sensor temperature={}".format(e), ErrorId.TEMPERATURE_SENSOR_ERROR, e)
        return None


def send_request(current_temp):
    response = requests.get(SERVER_URL, params={'current_temp': current_temp})
    return response.json()


def start_looper():
    while True:
        try:
            current_temp = get_current_temp()
            response_json = send_request(current_temp)
            server_response_processor.process(response_json)
        except ConnectionError as e:
            logger.error("Connection error={}".format(e), ErrorId.SERVER_CONNECTION_ERROR, e)
        except UnknownCommandException as e:
            logger.error("Unknown command received from server={}".format(e), ErrorId.UNKNOWN_COMMAND_ERROR, e)
        except Exception as e:
            logger.error("Unknown error while doing important stuff={}".format(e), ErrorId.UNKNOWN_ERROR, e)

        sleep(REQUEST_INTERVAL_SEC)


if __name__ == '__main__':
    start_looper()
