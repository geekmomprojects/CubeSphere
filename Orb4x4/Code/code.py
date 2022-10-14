# Write your code here :-)
from tilt import Tilt
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.color import RAINBOW
from bubbles import Bubbles
from orb import *
import imu
import board
import neopixel
import time, random

RED = (255,0,0)
BLACK = (0,0,0)

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D4
# Update to match the number of NeoPixels you have connected
pixel_num = 96

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.3, auto_write=False)
pixels.fill((0,0,0))

def orb4x4():
    width = 4
    gap = 0.25
    X = Matrix.X
    Y = Matrix.Y
    Z = Matrix.Z
    npix = width*width
    maxv = width-1 #largest coordinate valhe
    #definition of matrix defaults to alternating rows
    #The reference coodrinate frame for the orb is the one in which the
    #XIAO X-axis is along the short board axis, the positive Y axis is along
    #the long axis with positive direction pointed towards the USB connector
    #and positive Z axis is above the top of the board

    #Standard matrix with alternating row directions
    front = Matrix([0, -gap, 0], X, Z, 0, width)
    right = Matrix([maxv + gap, 0, maxv], -Z, Y, 1*npix, width)
    bottom = Matrix([maxv, 0, -gap], -X, Y, 2*npix, width)
    left = Matrix([-gap, 0, 0], Z, Y, 3*npix, width)
    top = Matrix([maxv, 0, maxv+gap], Y, -X, 4*npix, width)
    back = Matrix([maxv, maxv+gap, maxv], -Z, -X, 5*npix, width)
    """
    # This is my weird cube with some alternating, some non-alternating matrices
    front = Matrix([0, -gap, 0], X, Z, 0, width, alternating=False)
    right = Matrix([maxv + gap, 0, maxv], -Z, Y, 1*npix, width, alternating=False)
    bottom = Matrix([maxv, maxv, -gap], -X, -Y, 2*npix, width, alternating=True)
    left = Matrix([-gap, maxv, 0], Z, -Y, 3*npix, width, alternating=True)
    top = Matrix([maxv, 0, maxv+gap], Y, -X, 4*npix, width, alternating=False)
    back = Matrix([maxv, maxv+gap, maxv], -Z, -X, 5*npix, width, alternating=False)
    """
    orb = Orb(width,[front, right, bottom, left, top, back],
                ["front", "right", "bottom", "left", "top", "back"], pixels)
    return orb

#Create orb object
orb=orb4x4()

#useful when mapping the layout of the pixels in each matrix
def do_pixel(color=RED):
    for i in range(pixel_num):
        pixels[i] = color
        pixels.show()
        pixels[i] = BLACK
        time.sleep(0.1)

def do_matrix(color=RED):
    for i in range(6):
        name = orb.matrix_name(i)
        orb.fill_matrix(i,color)
        time.sleep(.5)
        orb.fill_matrix(i, BLACK)

def fill_half(coord=0, color=RED):
    for i in range(pixel_num):
        if orb.cart[i][coord] > 0.05:
            pixels[i] = color
        else:
            pixels[i] = BLACK


imu = imu.IMU()
tilt = Tilt(orb.pixels, orb.cart, imu)
bubbles = Bubbles(orb.pixels, orb.spher, imu, color=RED)
rainbow_sparkle = RainbowSparkle(pixels, speed = 0.075, step=10, period=20, num_sparkles = 30, background_brightness = 0)

while True:
    #do_pixel()
    tilt.animate()
    #rainbow_sparkle.animate()
    #bubbles.animate()
