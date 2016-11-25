import emailer
from heater import Heater
from logger import Logger
from server_response import Command
from server_response import ServerResponse
from temp_sensor import TempSensor

heater = Heater()
logger = Logger(__name__)
temp_sensor = TempSensor()


class ServerResponseProcessor:
    MAX_ALLOWED_TEMP = 26

    def __init__(self, response_json):
        self.server_response = ServerResponse(response_json)

    def process(self):
        rq_command = self.server_response.get_command()
        rq_temp = self.server_response.get_temperature();

        if rq_command is Command.THON:
            self.on_turn_heater_on(rq_temp)
        elif rq_command is Command.THOFF:
            self.on_turn_heater_off()
        elif rq_command is Command.LT:
            pass

    def on_turn_heater_on(self, rq_temp):
        current_temp = temp_sensor.value()

        if current_temp > ServerResponseProcessor.MAX_ALLOWED_TEMP:
            self.on_turn_heater_off()
            message = "Current temperature <<{}>> is bigger then max allowed <<{}>>. Disabling heater" \
                .format(current_temp, ServerResponseProcessor.MAX_ALLOWED_TEMP)
            logger.warn(message)
            emailer.send_email(message)

        elif current_temp > rq_temp:
            self.on_turn_heater_off()

        else:
            heater.turn_on()

    def on_turn_heater_off(self):
        heater.turn_off()
