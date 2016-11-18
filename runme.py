#!./.env/bin/python

import time

import requests

from logger import ErrorId
from logger import Logger
from temp_sensor import TempSensor

REQUEST_INTERVAL_SEC = 5

logger = Logger(__name__)
temp_sensor = TempSensor()


def sleep(seconds):
    logger.info("About to sleep for {} seconds".format(seconds))
    time.sleep(seconds)


def send_request(current_temp):
    response = requests.get("http://localhost:8001", params={'current_temp': current_temp})
    return response.json()


while True:
    try:
        current_temp = temp_sensor.value()
        response = send_request(current_temp)
    except Exception as e:
        logger.error("Error while getting response from server={}".format(e), ErrorId.SERVER_CONNECTION_ERROR)

    sleep(REQUEST_INTERVAL_SEC)
