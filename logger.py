import datetime
import os


class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def info(self, message):
        self.__print_log_message("INFO", message)

    def warn(self, message):
        self.__print_log_message("WARN", message)

    def error(self, message):
        self.__print_log_message("ERROR", message)

    def __print_log_message(self, level, message):
        print "[{}] [{}] {} ({})".format(self.__get_date_string(), level, message, self.__get_file_name())

    def __get_file_name(self):
        return os.path.basename(self.file_name)

    def __get_date_string(self):
        return datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
