from glob import escape
import pygame
from util import BLACK, GREEN, WHITE
# from main import all_events
from levels import *


font = pygame.font.Font("futura/futur.ttf", 20)

def start_screen(screen, level, avatar, player, player_sprite, elements):
    """
    start menu: options to select level, controls guide
        stretch goals: icon select
    """
    level = 0
    screen.fill(BLACK)
    if pygame.key.get_pressed()[pygame.K_1]:
        level = 0 # TODO: change hardcode
        # reset_level(level, avatar, player, player_sprite, elements)
    if pygame.key.get_pressed()[pygame.K_2]:
        level = 1


    start_text = font.render(f"Welcome to CarterDash", True, GREEN)
    controls = font.render("Controls: jump: Space/Up, exit: Esc", True, GREEN)
    
    screen.blits([[start_text, (100,100)], [controls, (100, 400)]])
    screen.blit(font.render(f"Level {level + 1}.", True, (255, 255, 0)), (100, 200))
    print("after screen blits in start")



        