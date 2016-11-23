from config.config import config
from logger import Logger


class Heater:
    logger = Logger(__name__)
    GPIO_1 = config['heater']['gpio-1']
    GPIO_2 = config['heater']['gpio-2']
    GPIOS = [GPIO_1, GPIO_2]

    def __init__(self):
        pass

    def turn_on(self):
        pass

    def turn_off(self):
        pass
