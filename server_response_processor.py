import emailer
import heater
import temp_sensor
from logger import Logger
from server_response import Command
from server_response import ServerResponse

__MAX_ALLOWED_TEMP = 26

__logger = Logger(__name__)


def __on_turn_heater_off():
    heater.turn_off()


def __on_turn_heater_on(rq_temp):
    current_temp = temp_sensor.value()
    __logger.debug("Current temperature={}".format(current_temp))

    if current_temp > __MAX_ALLOWED_TEMP:
        __on_turn_heater_off()
        message = "Current temperature <<{}>> is bigger then max allowed <<{}>>. Disabling heater" \
            .format(current_temp, __MAX_ALLOWED_TEMP)
        __logger.warn(message)
        emailer.send_email(message)

    elif current_temp > rq_temp:
        __logger.debug("Current temperature <<{}>> is bigger then <<{}>> requested. Turning heater off"
                       .format(current_temp, rq_temp))
        __on_turn_heater_off()

    else:
        __logger.debug("Turning/keeping heater on (requested temperature={}".format(rq_temp))
        heater.turn_on()


def fall_back_to_safety():
    # TODO: check heater state and if it is on - keep it on for some time
    __logger.debug("No server response, falling back to safety");
    heater.turn_off()


def act_on_server_response(response_json):
    server_response = ServerResponse(response_json)

    rq_command = server_response.get_command()
    __logger.debug("Command received from server=<<{}>>".format(rq_command))

    rq_temp = server_response.get_temperature()
    __logger.debug("Requested temperature received from server=<<{}>>".format(rq_temp))

    if rq_command is Command.THON:
        __on_turn_heater_on(rq_temp)
    elif rq_command is Command.THOFF:
        __on_turn_heater_off()
    elif rq_command is Command.LT:
        pass


def process(response_json):
    if response_json is None:
        fall_back_to_safety()
    else:
        act_on_server_response(response_json)
