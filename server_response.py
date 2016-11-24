from enum import Enum, unique

from logger import Logger

logger = Logger(__name__)


@unique
class Command(Enum):
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
        if command_string not in Command.__members__:
            raise UnknownCommandException("Given command={} is not known".format(command_string))

        command = Command[command_string]
        self.__log_received_command(command)

        return command

    def __log_received_command(self, command):
        if command is not Command.LEISURE_TIME:
            logger.info("Command received from server={}".format(command.name))


class UnknownCommandException(Exception):
    def __init__(self, message):
        super(UnknownCommandException, self).__init__(message)
