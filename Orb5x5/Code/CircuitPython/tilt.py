from adafruit_led_animation.animation import Animation
from coordinates import *
import board, time
import math
import random

def clamp(n, mn, mx):
    return min(max(n,mn),mx)


class Tilt(Animation):
    """
    Tilt Animation
    :param pixel_object: The initialised LED object.
    :param float speed: Animation speed in seconds, e.g. ``0.1``.
    :param color: Animation color in ``(r, g, b)`` tuple, or ``0x000000`` hex format.
    :param twinklechance: chance of turning on at any moment
    """

    def __init__(
        self,
        pixel_object,
        coord_list,
        imu,
        speed=.05,
        color=(255,0,0),
        name=None
    ):
        super().__init__(pixel_object, speed, color=color, name=name)
        self.imu = imu
        self.coords = coord_list
        self.reset()


    def reset(self):
        self.pixel_object.fill((0,0,0))

    # Base color on pitch, position on roll
    def draw(self):
        x,y,z = self.imu.acceleration
        pitch = math.atan2(x,z)
        roll = math.atan2(y, math.sqrt(z*z + x*x))
        #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (self.imu.acceleration))
        #print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (imu.gyro))
        #print("Pitch:%.2f, Roll:%.2f" % (pitch, roll))
        #droll = math.degrees(roll)
        #dpitch = math.degrees(pitch)
        #print(" roll ",droll, " pitch ", dpitch)
        npix = self.pixel_object.n
        rvals = rotateCartesianPtsX(self.coords, -pitch)
        rvals = rotateCartesianPtsY(rvals, -roll)
        for i in range(npix):
            vert = rvals[i][2]
            if (vert > 0.04):
                self.pixel_object[i] = (int(255*(vert)),0,int(255*(1-vert)))
            else:
                self.pixel_object[i] = (0,0,0)