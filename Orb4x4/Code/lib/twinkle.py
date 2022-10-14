from adafruit_led_animation.animation import Animation
from adafruit_led_animation.color import calculate_intensity
from adafruit_led_animation.color import RAINBOW
import random


class Twinkle(Animation):
    """
    Twinkle Animation
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
        speed,
        color,
        twinklechance=None,
        name=None
    ):
        super().__init__(pixel_object, speed, color, name=name)
        if twinklechance==None:
            self.twinklechance = 0.01
        else:
            self.twinklechance = twinklechance
        self.reset()
        self.pix_state = [-1]*self.pixel_object.n



    def reset(self):
        self.pixel_object.fill((0,0,0))

    def draw(self):
        for i in range(self.pixel_object.n):
            if self.pix_state[i] < 0:
                if random.random() < self.twinklechance:
                    self.pix_state[i] = 0
            else:
                self.pix_state[i] = self.pix_state[i] + 1
                if self.pix_state[i] >= self.nsteps:
                    self.pixel_object[i] = (0,0,0)
                    self.pix_state[i] = -1
                else:
                    self.pixel_object[i] = calculate_intensity(self.color, self.brightsteps[self.pix_state[i]])


class RainbowTwinkle(Twinkle):
    """
    Twinkle Animation
    :param pixel_object: The initialised LED object.
    :param float speed: Animation speed in seconds, e.g. ``0.1``.
    :param color: Animation color in ``(r, g, b)`` tuple, or ``0x000000`` hex format.
    :param twinklechance: chance of turning on at any moment
    """

    def __init__(
        self,
        pixel_object,
        speed,
        color=None,
        twinklechance=None,
        name=None
    ):
        super().__init__(pixel_object, speed, color, twinklechance, name=name)
        self.pix_color = [(0,0,0)]*self.pixel_object.n

    def draw(self):
        for i in range(self.pixel_object.n):
            if self.pix_state[i] < 0:
                if random.random() < self.twinklechance:
                    self.pix_state[i] = 0
                    self.pix_color[i] = random.choice(RAINBOW)
            else:
                self.pix_state[i] = self.pix_state[i] + 1
                if self.pix_state[i] >= self.nsteps:
                    self.pixel_object[i] = (0,0,0)
                    self.pix_state[i] = -1
                    self.pix_color[i] = (0,0,0)
                else:
                    self.pixel_object[i] = calculate_intensity(self.pix_color[i], self.brightsteps[self.pix_state[i]])

