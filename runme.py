#!./.env/bin/python

import time

import requests
from enum import Enum

from logger import ErrorId
from logger import Logger
from temp_sensor import TempSensor

REQUEST_INTERVAL_SEC = 60

logger = Logger(__name__)
temp_sensor = TempSensor()


class Actions(Enum):
    TURN_ON_HEATER = 'TURN_ON_HEATER'
    TURN_OFF_HEATER = 'TURN_OFF_HEATER'


def sleep(seconds):
    logger.info("About to sleep for {} seconds".format(seconds))
    time.sleep(seconds)


def send_request(current_temp):
    response = requests.get("http://localhost:8001", params={'current_temp': current_temp})
    return response.json()


def start_looper():
    while True:
        try:
            current_temp = temp_sensor.value()
            response = send_request(current_temp)
        except Exception as e:
            logger.error("Error while getting response from server={}".format(e), ErrorId.SERVER_CONNECTION_ERROR)

        sleep(REQUEST_INTERVAL_SEC)


if __name__ == '__main__':
    start_looper()
