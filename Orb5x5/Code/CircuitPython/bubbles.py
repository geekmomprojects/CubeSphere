from adafruit_led_animation.animation import Animation
from coordinates import *
import board, time
import math
import random

#NOTE: Work in progress. Currently doesn't make use of the IMU, but will eventually
# move the bubbles around so they float to the top of the orb

#returns angular distance between two angular positions
def angular_separation(theta1, phi1, theta2, phi2):
    return math.acos(math.cos(phi1)*math.cos(phi2) +
                     math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2))

class Bubble:
    def __init__(self, radius, color, pos):
        # radius is angular in radians
        self.radius = radius
        self.color = color
        #position on the surface of a sphere, theta, phi
        self.pos = pos
        self.velocity = [random.random()/20, random.random()/20]

class Bubbles(Animation):
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
        coord_list,  #Angular coordinates (r, theta, phi)
        imu,
        speed=.03,
        color=(255,0,0),
        name=None
    ):
        super().__init__(pixel_object, speed, color=color, name=name)
        self.imu = imu
        self.coords = coord_list
        self.bubbles = [Bubble(math.pi/4, (255,0,0), [math.pi/5,math.pi/8]),
                        Bubble(math.pi/4, (0,255,0), [math.pi/3, math.pi/9]),
                        Bubble(math.pi/5, (0,0,255), [-math.pi/3, 0])]


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
        self.pixel_object.fill((0,0,0))
        for i in range(npix):
            for b in self.bubbles:
                sep = angular_separation(b.pos[0], b.pos[1], self.coords[i][0], self.coords[i][1])
                if sep < b.radius:
                    v = math.pow((1-sep/b.radius),2)
                    self.pixel_object[i] = [int(self.pixel_object[i][k] + b.color[k]*v) for k in range(3)]

        for b in self.bubbles:
            b.pos[1] += b.velocity[1]
            if b.pos[1] >= math.pi:
                b.pos[1] = math.pi - b.pos[1]
                b.velocity[1] = -b.velocity[1]
            b.pos[0] += b.velocity[0]
            if b.pos[0] >= math.pi:
                b.pos[0] -= 2*math.pi
