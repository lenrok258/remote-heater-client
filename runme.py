#!./.env/bin/python

import time

import requests

from logger import Logger

REQUEST_INTERVAL_S = 5

logger = Logger(__name__)

def sleep(seconds):
    logger.info("About to sleep for {} seconds".format(REQUEST_INTERVAL_S))
    time.sleep(REQUEST_INTERVAL_S)

def send_request():
    response = requests.get("http://localhost:8001")
    logger.info(response.status_code)
    response_json = response.json()
    return response_json


while True:
    try:
        response = send_request()
        logger.info(response)
    except Exception as e:
        logger.error("Error while getting response from server={}".format(e))

    sleep(REQUEST_INTERVAL_S)
