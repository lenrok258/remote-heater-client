import config.config as __config
from logger import Logger

__logger = Logger(__name__)

__config = __config.config['temp-sensor']
__SENSOR_ID_1 = __config['sensor-1-id']
__SENSOR_ID_2 = __config['sensor-2-id']
__SENSOR_BASE_PATH_TEMPLATE = __config['file-path-pattern']
__SENSOR_MAX_DIFF_TOLERANCE = __config['max-tolerated-sensors-difference']


def __read_sensor(sensor_id):
    file_path = __SENSOR_BASE_PATH_TEMPLATE.format(sensor_id)
    with open(file_path, 'r') as sensor_file:
        sensor_file.readline()
        second_line = sensor_file.readline()
    temp_string = second_line.split("=")[1]
    temp_value = int(temp_string)
    __logger.debug("Raw temperature value read from sensor {}={}".format(sensor_id, temp_value))
    return float(temp_value) / 1000.0


def __get_value_from_sensors():
    temp_1 = __read_sensor(__SENSOR_ID_1)
    temp_2 = __read_sensor(__SENSOR_ID_2)
    temp_sensors_diff = abs(temp_1 - temp_2)

    if temp_sensors_diff > __SENSOR_MAX_DIFF_TOLERANCE:
        raise TempSensorException(
            "Temp sensors difference = {}, tolerance = {}".format(temp_sensors_diff, __SENSOR_MAX_DIFF_TOLERANCE))

    return (temp_1 + temp_2) / 2;


def value():
    temperature = __get_value_from_sensors()
    # self.logger.info("Temperature measured is {}".format(temperature))
    return temperature


class TempSensorException(Exception):
    def __init__(self, message):
        super(TempSensorException, self).__init__(message)
