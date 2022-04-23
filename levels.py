import csv

import pygame
from map import *



def resize(img, size=(32, 32)):
    """resize images
    :param img: image to resize
    :type img: im not sure, probably an object
    :param size: default is 32 because that is the tile size
    :type size: tuple
    :return: resized img

    :rtype:object?
    """
    resized = pygame.transform.smoothscale(img, size)
    return resized


#load all images
spike = pygame.image.load("images/spike.png")
spike = resize(spike)

block = pygame.image.load("images/block.png")
block = resize(block)


def create_map(level_number):
    """"
    
    Inputs:
    - level_number: what level to load, the file will be <level>.csv

    opens csv file that contains the input level and loads it in as 
    a list of lists.
    """
    file_location = "levels/" + str(level_number) + ".csv"
    level_list = []

    with open(file_location, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csv_reader:
            level_list.append(row)
            
    return level_list
        


def init_level(map_lists, elements):
    """
    given a list of lists that describes a level, as generated by "create_map", 
    this initializes game objects of correct types in the correct positions of the map.
    
    Example:
    map_lists = 
          0   1   2    3
        [
     0   [-1, -1, -1, -1],
     1   [-1, -1,  S,  S],
     2   [ 0,  0,  0,  0],
        ]

    """
    x = 0
    y = 0

    for row in map_lists:
        for thing in row:
            # for each number, create the correct map element
            current_position = (x, y)

            if thing == "S":
                Spike(spike, current_position, elements)
            if thing == "0":
                Block(block, current_position, elements)
            if thing == "C":
                Coin(block, current_position, elements) #change to coin
            if thing == "E":
                End(block, current_position, elements)

        # when we move to the right, increase x by one
            x += 1
    # when we move down a row, make x 0, make y increase by one
        y += 1
        x = 0

            
            
