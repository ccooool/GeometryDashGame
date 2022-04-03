import os
import pygame

pygame.init()
import random
from player import * 
from screens import *
from levels import *
from pygame.math import Vector2
from pygame.draw import rect
from infoDAO import InfoDAO

# TODO 
# HOMEWORK:
# - pick a font

# screen design:
# what boxes/messages will be displayed on the following screens: 
# - opening screen 
# - win screen
# - death screen
# - level choose
# ... etc ...



# def resize(img, size=(32, 32)):
#     """resize images
#     :param img: image to resize
#     :type img: im not sure, probably an object
#     :param size: default is 32 because that is the tile size
#     :type size: tuple
#     :return: resized img

#     :rtype:object?
#     """
#     resized = pygame.transform.smoothscale(img, size)
#     return resized

"""
all global things will be defined here
"""

# # initializing the pygame module
# pygame.init()

# create screen
screen = pygame.display.set_mode([800, 600])

# main loop condition
done = False

# starting condition for starting from the main menu
start = False

# load main character image
avatar = pygame.image.load("images/player.png")
pygame.display.set_icon(avatar)

# set window title
window_title = 'Carter Dash'
pygame.display.set_caption(window_title)

# play music
music = pygame.mixer_music.load("music/geodash.mp3")
# pygame.mixer_music.play()

# load background image
bg = pygame.image.load("images/background.png")

# #load all images
# spike = pygame.image.load("images/spike.png")
# spike = resize(spike)

# block = pygame.image.load("images/block.png")
# block = resize(block)

# all sprite elements
player_sprite = pygame.sprite.Group()
elements = pygame.sprite.Group()




# class Pig:
#     def __init__(self, numfeet):
#         pass

# # makes cow with four feet
# cow = Cow(4) 


player = Player(avatar, (150, 150), elements, player_sprite)
# init some starting values
cameraX = 0
attempts = 0
coins = 0
cur_level = 0  # will contain players level choice
fill = 0

# initialize levels
# array of all levels
levels = ["levels/1.csv"]
created_map = create_map(cur_level)
init_level(created_map, elements)
level_width = (len(created_map[0]) * 32)
level_width = (len(created_map) * 32)
level = 0

infoDao = InfoDAO(start, screen, level, avatar, player, player_sprite, elements)


# check the player win/death fields to determine
# if the player has won or died
def eval_outcome(win_field, death_field):
    if win_field == True:
        show_win_screen(cur_level, avatar, elements, screen, player, player_sprite)
    elif death_field == True:
        # TODO: update seconds alive with proper time
        show_death_screen(cur_level, avatar, elements, screen, player, player_sprite, 0)


exited_game = False

# main loop, come out of it when player exits game
while exited_game == False:
    print("game is running")

    # collect the user pressed key
    keys = pygame.key.get_pressed()

    # if user presses esc, exit
    if keys[pygame.K_ESCAPE]:
        exited_game = True
        
    # check if game needs to be started
    if not start:
        wait_for_input(infoDao)
        player = reset_level(cur_level, avatar, player, player_sprite, elements)
        start = True

    player.vel.x = 5
    

    """
    keyboard_buttons = {up: False, down: True, left: False, right: False}
    keyboard_buttons["k"] -> 0 -> means it not pressed
    keyboard_buttons["k"] -> 1 -> means it is pressed
    """

    # check if dead or won to show the correct screen
    eval_outcome(player.won, player.dead)

    # check jumping condition
    if keys[pygame.K_UP]:
        player.isJumping = True

    player.update()

    # move all the elements on the screen to the left
    CameraX = player.vel.x
    for element in elements:
        element.rect.x -= CameraX
    
    screen.blit(bg, (0,0))

    # redraw map sprites onto the game screen
    elements.draw(screen)
    player_sprite.draw(screen)
    
    # handle other events
    # 
    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            exited_game = True
        if event.type == pygame.KEYDOWN:
            pass
    
    pygame.display.flip()
    infoDao.clock.tick(60)


# player hit exit game
pygame.quit()



