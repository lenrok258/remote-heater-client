#!./.env/bin/python

import time

import requests
from requests.exceptions import ConnectionError

from config.config import config
from logger import ErrorId
from logger import Logger
from temp_sensor import TempSensor

REQUEST_INTERVAL_SEC = 60
SERVER_URL = config['server']['url']

logger = Logger(__name__)
temp_sensor = TempSensor()


def sleep(seconds):
    logger.info("About to sleep for {} seconds".format(seconds))
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
            response = send_request(current_temp)
            process_response(response)
        except ConnectionError as e:
            logger.error("Error while getting response from server={}".format(e), ErrorId.SERVER_CONNECTION_ERROR, e)
        except Exception as e:
            logger.error("Unknown error while doing important stuff={}".format(e), ErrorId.SERVER_CONNECTION_ERROR, e)

        sleep(REQUEST_INTERVAL_SEC)


if __name__ == '__main__':
    start_looper()
