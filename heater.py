from config.config import config
from logger import Logger

if config['dev']['local-development']:
    import GPIO_mock as GPIO
else:
    import RPi.GPIO as GPIO

__logger = Logger(__name__)

__GPIO_1 = config['heater']['gpio-1']
__GPIO_2 = config['heater']['gpio-2']
__GPIOS = [__GPIO_1, __GPIO_2]

current_state = None


def turn_on():
    __setup_gpio(GPIO.HIGH, "on")


def turn_off():
    __setup_gpio(GPIO.LOW, "off")


def __setup_gpio(state, state_label):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(__GPIOS, GPIO.OUT)
    GPIO.output(__GPIOS, state)

    __log_if_changed(state_label)
    global current_state
    current_state = state_label


def __log_if_changed(new_value):
    if new_value != current_state:
        message = "Heater value changed from <<{}>> to <<{}>>".format(current_state, new_value)
        __logger.info(message)
