from adafruit_lsm6ds.lsm6ds3 import LSM6DS3
import board, time, digitalio, busio

# Copied from https://forum.seeedstudio.com/t/imu-i2c-error-with-circuitpython-using-xiao-ble-sense/265020
class IMU(LSM6DS3):
    def __init__(self):
        dpwr = digitalio.DigitalInOut(board.IMU_PWR)
        dpwr.direction = digitalio.Direction.OUTPUT
        dpwr.value = 1
        time.sleep(1)
        i2c = busio.I2C(board.IMU_SCL, board.IMU_SDA)
        super().__init__(i2c)