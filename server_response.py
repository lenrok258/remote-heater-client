from enum import Enum, unique

from logger import Logger

logger = Logger(__name__)


@unique
class Actions(Enum):
    TURN_ON_HEATER = 1
    TURN_OFF_HEATER = 2
    LEISURE_TIME = 3


class ServerResponse:
    def __init__(self, jsonResponse):
        self.jsonResponse = jsonResponse

    def get_command(self):
        command = self.jsonResponse['command']
        return self.__map_command_string_to_command_enum(command)

    def __map_command_string_to_command_enum(self, command_string):
        if command_string not in Actions.__members__:
            raise UnknownCommandException("Given command={} is not known".format(command_string))

        if command_string is not Actions.LEISURE_TIME:
            logger.info("Action recieved from server={}".format(command_string))
            
        return Actions[command_string]


class UnknownCommandException(Exception):
    def __init__(self, message):
        super(UnknownCommandException, self).__init__(message)
