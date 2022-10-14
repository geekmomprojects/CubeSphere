from adafruit_led_animation.animation import Animation
from adafruit_led_animation.color import calculate_intensity
from adafruit_led_animation.color import RAINBOW
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3
import board, time, digitalio, busio
from math import atan2, sqrt
import random

def clamp(n, mn, mx):
    return min(max(n,mn),mx)

# Copied from https://forum.seeedstudio.com/t/imu-i2c-error-with-circuitpython-using-xiao-ble-sense/265020
class IMU(LSM6DS3):
    def __init__(self):
        dpwr = digitalio.DigitalInOut(board.IMU_PWR)
        dpwr.direction = digitalio.Direction.OUTPUT
        dpwr.value = 1
        time.sleep(1)
        i2c = busio.I2C(board.IMU_SCL, board.IMU_SDA)
        super().__init__(i2c)


class Tilt(Animation):
    """
    Tilt Animation
    :param pixel_object: The initialised LED object.
    :param float speed: Animation speed in seconds, e.g. ``0.1``.
    :param color: Animation color in ``(r, g, b)`` tuple, or ``0x000000`` hex format.
    :param twinklechance: chance of turning on at any moment
    """
    brightsteps = [x/10 for x in range(0,10)] + [x/10 for x in range(10,0,-1)]
    nsteps = len(brightsteps)

    def __init__(
        self,
        pixel_object,
        imu,
        speed=.05,
        name=None
    ):
        super().__init__(pixel_object, speed, color=(0,0,0), name=name)
        self.imu = imu
        self.reset()


    def reset(self):
        self.pixel_object.fill((0,0,0))

    # Base color on pitch, position on roll
    def draw(self):
        x,y,z = self.imu.acceleration
        NRAINBOW = len(RAINBOW)
        roll = atan2(x,z)*57.3
        pitch = atan2(-y, sqrt(z*z + x*x))*57.3
        #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (self.imu.acceleration))
        #print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (imu.gyro))
        #print("Pitch:%.2f, Roll:%.2f" % (pitch, roll))
        npix = self.pixel_object.n
        middle = int(round(npix/2))
        degperpix = 100/middle
        tilt = clamp(abs(pitch)/90.0,0,1.0)
        index = int(tilt*NRAINBOW)
        color = RAINBOW[index]
        #spread = 1+int(tilt*middle)
        spread = 2

        #for i in range(npix):
        self.pixel_object.fill((0,0,0))
        if roll < 0:
            roll += 360
        #Constrain to
        pix = clamp(middle + int((roll - 120)/degperpix),0,npix-1)
        self.pixel_object[pix] = RAINBOW[(index + NRAINBOW//2) % NRAINBOW]
        #self.pixel_object[pix] = color
        idrop = 0.8/spread
        for i in range(1,spread):
            #color = RAINBOW[int(i*len(RAINBOW)/spread)]
            softcolor = calculate_intensity(color, 1-i*idrop)
            lo = pix - i
            hi = pix + i
            if hi < npix - 1:
                self.pixel_object[hi] = softcolor
            if lo > 0:
                self.pixel_object[lo] = softcolor
