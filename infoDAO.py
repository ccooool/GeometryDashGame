
# Data Access Object
# 
import pygame

class InfoDAO:
    def __init__(self, start, screen, level, avatar, player, player_sprite, elements):
        self.started = start
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.level = level
        self.avatar = avatar
        self.player = player
        self.player_sprite = player_sprite
        self.elements = elements

    def is_started(self):
        return self.started
    
    def set_started(self, start_set):
        self.started = start_set

