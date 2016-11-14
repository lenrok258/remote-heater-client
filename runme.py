#!./.env/bin/python

import time

import requests

from logger import Logger

REQUEST_INTERVAL_S = 60

logger = Logger(__name__)


def send_request():
    response = requests.get("http://ip.jsontest.com/")
    logger.info(response.status_code)
    response_json = response.json()
    return response_json


while True:
    response = send_request()
    logger.info("About to sleep for {} seconds".format(REQUEST_INTERVAL_S))
    time.sleep(REQUEST_INTERVAL_S)
