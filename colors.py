from random import randint, random
from collections import namedtuple

Color = namedtuple('color', 'red blue green alpha')

def random_color():
    red = randint(0,255)
    blue = randint(0,255)
    green = randint(0,255)
    alpha = round(random(),2)

    return Color(red,blue,green,alpha)