import datetime


def info(message):
    __print_log_message("INFO", message)


def warn(message):
    __print_log_message("WARN", message)


def error(message):
    __print_log_message("ERROR", message)


def __print_log_message(level, message):
    print "[{}] [{}] {}".format(__get_date_string(), level, message);


def __get_date_string():
    return datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
