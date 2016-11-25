import config.config as config
from logger import Logger


class TempSensor:
    logger = Logger(__name__)

    config = config.config['temp-sensor']
    SENSOR_ID_1 = config['sensor-1-id']
    SENSOR_ID_2 = config['sensor-2-id']
    SENSOR_BASE_PATH_TEMPLATE = config['file-path-pattern']
    SENSOR_MAX_DIFF_TOLERANCE = config['max-tolerated-sensors-difference']

    def __init__(self):
        pass

    def value(self):
        temperature = self.__get_value_from_sensors()
        # self.logger.info("Temperature measured is {}".format(temperature))
        return temperature

    def __get_value_from_sensors(self):
        temp_1 = self.__read_sensor(TempSensor.SENSOR_ID_1)
        temp_2 = self.__read_sensor(TempSensor.SENSOR_ID_2)
        temp_sensors_diff = abs(temp_1 - temp_2)

        if temp_sensors_diff > TempSensor.SENSOR_MAX_DIFF_TOLERANCE:
            raise TempSensorException(
                "Temp sensors difference = {}, tolerance = {}".format(temp_sensors_diff,
                                                                      TempSensor.SENSOR_MAX_DIFF_TOLERANCE))

        return (temp_1 + temp_2) / 2;

    def __read_sensor(self, sensor_id):
        file_path = TempSensor.SENSOR_BASE_PATH_TEMPLATE.format(sensor_id)
        with open(file_path, 'r') as sensor_file:
            sensor_file.readline();
            second_line = sensor_file.readline();
        temp_string = second_line.split("=")[1]
        temp_value = int(temp_string)
        return float(temp_value) / 1000.0


class TempSensorException(Exception):
    def __init__(self, message):
        super(TempSensorException, self).__init__(message)
