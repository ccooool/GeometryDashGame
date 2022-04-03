
import random
import pygame

def select_random_color():
    # pick random rgb value
    # pick 3 random values between 0-255
    
    # this line makes random_int = to a number between 0-255
    random_int = random.randint(0, 255)
    random_int2 = random.randint(0, 255)
    random_int3 = random.randint(0, 255)
    random_color = (random_int, random_int2, random_int3)
    return random_color



"""
COLOR CONSTANTS
"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)




