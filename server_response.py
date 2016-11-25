from enum import Enum, unique

from logger import Logger

logger = Logger(__name__)


@unique
class Command(Enum):
    THON = 'TURN_HEATER_ON'
    THOFF = 'TURN_HEATER_OFF'
    LT = 'LEISURE_TIME'


class ServerResponse:
    def __init__(self, json_response):
        self.jsonResponse = json_response

    def get_command(self):
        command = self.jsonResponse['command']
        return self.__map_command_string_to_command_enum(command)

    def get_temperature(self):
        return self.jsonResponse['temp']

    def __map_command_string_to_command_enum(self, command_string):
        if command_string not in Command.__members__:
            raise UnknownCommandException("Given command={} is not known".format(command_string))
        return Command[command_string]


class UnknownCommandException(Exception):
    def __init__(self, message):
        super(UnknownCommandException, self).__init__(message)
