from glob import escape
from tkinter import EventType
import pygame
from sqlalchemy import false, true
from util import BLACK, GREEN, WHITE
import pygame
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
        reset_level(level, avatar, player, player_sprite, elements)

    start_text = font.render(f"Welcome to CarterDash", True, WHITE)

    controls = font.render("Controls: jump: Space/Up, exit: Esc", True, GREEN)

    screen.blits([[start_text, (100,100)], [controls, (100, 400)]])
    # screen.blit(font.render(f"Level {level + 1}.", True, (255, 255, 0)), (100, 200))



def show_death_screen(level, avatar, elements, screen, player, player_sprite, seconds):
    
    player_sprite.clear(player.image, screen)
    game_over_text = font.render("Good Try", True, WHITE)
    duration_text = font.render(str(seconds), True, WHITE)

    screen.fill(pygame.Color("sienna1"))
    screen.blits([[game_over_text, (100, 100)], [duration_text, (100, 400)]])

    # wait for a player to make an input because the screen would disappear really fast
    # and would restart without wating for the player's input.
    wait_for_input()
    reset_level(level, avatar, player, player_sprite, elements)

def show_win_screen(level, avatar, elements, screen, player, player_sprite, seconds):
    win_text = "Level Complete!"
    player_sprite.clear(player.image, screen)
    won = font.render(win_text, True, GREEN)
    screen.blits([won, (100, 100)])

    wait_for_input()
    reset_level(level, avatar, player, player_sprite, elements)

# another loop that will wait for a key press from the user
def wait_for_input(infoDAO):
    # start waiting
    # wait until a key gets pressed
    #   - check for key press using pygame.event.get()
    #   - handle the cases of game quit, game restart
    input = False
    while input == False:
        infoDAO.clock.tick(60)

        events = pygame.event.get()
        
        if not infoDAO.is_started():
            infoDAO.set_started(True)
            start_screen(infoDAO.screen, infoDAO.level, infoDAO.avatar,infoDAO.player, infoDAO.player_sprite, infoDAO.elements)

        for event in events:
            if event.type == pygame.KEYDOWN:
                # quit game if escape
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    input = true
    # start = True
    return true


        
