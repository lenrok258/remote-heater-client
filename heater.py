import RPi.GPIO as GPIO

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
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Heater.GPIOS, GPIO.OUT)
        GPIO.output(Heater.GPIOS, GPIO.HIGH)

    def turn_off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Heater.GPIOS, GPIO.OUT)
        GPIO.output(Heater.GPIOS, GPIO.LOW)
