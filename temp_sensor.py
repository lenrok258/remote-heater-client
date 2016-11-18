from logger import Logger


class TempSensor:
    logger = Logger(__name__)

    def __init__(self):
        pass

    def value(self):
        temp_mock = 20.1;
        self.logger.info("Temperature measured is {}".format(temp_mock))
        return temp_mock
