#!./.env/bin/python

import time

import requests
from requests.exceptions import ConnectionError

import heater
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
    logger.debug("Sleeping for {} seconds".format(REQUEST_INTERVAL_SEC))
    time.sleep(seconds)


def get_current_temp():
    try:
        current_temp = temp_sensor.value()
        return current_temp
    except Exception as e:
        logger.error("Cannot read sensor temperature={}".format(e), ErrorId.TEMPERATURE_SENSOR_ERROR, e)
        return None


def gather_rq_params():
    params = {
        'current_temp': get_current_temp(),
        'heater_status': heater.current_state
    }
    logger.debug("About to request with params={}".format(params))
    return params


def send_request(rq_params):
    try:
        response = requests.get(SERVER_URL, params=rq_params)
        logger.debug("Server response received={}, status={}".format(response.content, response.status_code))
        return response.json()
    except ConnectionError as e:
        logger.error("Connection error={}".format(e), ErrorId.SERVER_CONNECTION_ERROR, e)
        return None
    except UnknownCommandException as e:
        logger.error("Unknown command received from server={}".format(e), ErrorId.UNKNOWN_COMMAND_ERROR, e)
        return None
    except Exception as e:
        logger.error("Unknown error while sending pooling request={}".format(e), ErrorId.UNKNOWN_CONNECTION_ERROR, e)


def start_looper():
    while True:
        try:
            rq_params = gather_rq_params()
            response_json = send_request(rq_params)
            server_response_processor.process(response_json)
        except Exception as e:
            logger.error("Unknown error while doing important stuff={}".format(e), ErrorId.UNKNOWN_ERROR, e)

        sleep(REQUEST_INTERVAL_SEC)


if __name__ == '__main__':
    start_looper()
