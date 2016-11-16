from logger import Logger

logger = Logger(__name__)


class TempSensor:
    def __init__(self):
        pass

    @property
    def value(self):
        temp_mock = 20.1;
        logger.info("Temperature measured is {}".format(temp_mock))
        return temp_mock
