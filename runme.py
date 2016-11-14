import time

import requests

import logger

REQUEST_INTERVAL_S = 1

print __name__


def send_request():
    response = requests.get("http://ip.jsontest.com/")
    logger.info(response.status_code)
    response_json = response.json()
    return response_json


while True:
    response = send_request()
    time.sleep(REQUEST_INTERVAL_S)
