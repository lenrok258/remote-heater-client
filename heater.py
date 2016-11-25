import emailer
from config.config import config
from logger import Logger

if config['dev']['local-development']:
    import GPIO_mock as GPIO
else:
    import RPi.GPIO as GPIO

logger = Logger(__name__)


class Heater:
    logger = Logger(__name__)
    GPIO_1 = config['heater']['gpio-1']
    GPIO_2 = config['heater']['gpio-2']
    GPIOS = [GPIO_1, GPIO_2]

    def __init__(self):
        self.previous_value = None
        pass

    def turn_on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Heater.GPIOS, GPIO.OUT)
        GPIO.output(Heater.GPIOS, GPIO.HIGH)
        self.log_if_changed("on")

    def turn_off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Heater.GPIOS, GPIO.OUT)
        GPIO.output(Heater.GPIOS, GPIO.LOW)
        self.log_if_changed("off")

    def log_if_changed(self, new_value):
        if new_value != self.previous_value:
            message = "Heater value changed from <<{}>> to <<{}>>".format(self.previous_value, new_value)
            logger.info(message)
            emailer.send_email(message)
