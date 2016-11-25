import json
from unittest import TestCase

from  server_response import Command
from  server_response import ServerResponse
from server_response import UnknownCommandException


class ServerResponseTest(TestCase):
    JSON_RESPONSE_OK_COMMAND_TURN_ON = json.loads('{"command": "THON"}')
    JSON_RESPONSE_OK_COMMAND_TURN_OFF = json.loads('{"command": "THOFF"}')
    JSON_RESPONSE_OK_COMMAND_LEISURE = json.loads('{"command": "LT"}')
    JSON_RESPONSE_FAIL_COMMAND_UNKNOWN = json.loads('{"command": "DO_SOME_AMAZING_STUFF"}')

    def test_should_return_turn_on_command(self):
        server_response = ServerResponse(ServerResponseTest.JSON_RESPONSE_OK_COMMAND_TURN_ON)
        command = server_response.get_command()
        self.assertEqual(Command.THON, command)

    def test_should_return_turn_off_command(self):
        server_response = ServerResponse(ServerResponseTest.JSON_RESPONSE_OK_COMMAND_TURN_OFF)
        command = server_response.get_command()
        self.assertEqual(Command.THOFF, command)

    def test_should_return_leisure_time_command(self):
        server_response = ServerResponse(ServerResponseTest.JSON_RESPONSE_OK_COMMAND_LEISURE)
        command = server_response.get_command()
        self.assertEqual(Command.LT, command)

    def test_raise_exception_on_command_unknown(self):
        server_response = ServerResponse(ServerResponseTest.JSON_RESPONSE_FAIL_COMMAND_UNKNOWN)
        with self.assertRaises(UnknownCommandException):
            server_response.get_command()
