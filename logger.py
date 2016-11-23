import datetime
import time
import traceback

from enum import Enum

import emailer

SAME_ERROR_EMAIL_INTERVAL_SEC = 60 * 60


class ErrorId(Enum):
    SERVER_CONNECTION_ERROR = 1
    TEMPERATURE_SENSOR_ERROR = 2
    UNKNOWN_COMMAND_ERROR = 3
    UNKNOWN_ERROR = 99999


class Logger:
    __error_timestamps = {}

    def __init__(self, file_name):
        self.file_name = file_name

    def info(self, message):
        self.__print_log_message("INFO", message)

    def warn(self, message):
        self.__print_log_message("WARN", message)

    def error(self, message, error_id, exception=None):
        if exception:
            message += " Exception:" + traceback.format_exc()
        self.__print_log_message("ERROR", message)
        self.__send_email(error_id, message)

    def __print_log_message(self, level, message):
        print "[{}] [{}] {} ({})".format(self.__get_date_string(), level, message, self.__get_file_name())

    def __get_file_name(self):
        return self.file_name

    def __get_date_string(self):
        return datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    def __send_email(self, error_id, message):
        if error_id in self.__error_timestamps.keys():
            error_timestamp = self.__error_timestamps[error_id]
            # wait for an hour
            if (time.time() - error_timestamp) < SAME_ERROR_EMAIL_INTERVAL_SEC:
                return
        emailer.send_email("ERROR: %s" % message)
        self.__error_timestamps[error_id] = time.time()
