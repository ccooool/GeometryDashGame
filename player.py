import pygame
from pygame.math import Vector2
from pygame.draw import rect
from map import * 
from screens import * 
from levels import *
import os


GRAVITY = Vector2(0, 0.86)

class Player(pygame.sprite.Sprite):
    
    def __init__(self, avatar, pos, platforms, *groups): 
        super().__init__(*groups)
        self.isJumping = False
        self.platforms = platforms
        self.onGround = True
        self.dead = False
        self.won = False
        image = pygame.image.load(os.path.join("images", "player.png"))
        self.image = pygame.transform.smoothscale(image, (32, 32))
        print("here:", self.image)
        self.rect = self.image.get_rect(center=pos)
        self.jump_height = 10
        self.velocity = Vector2(0, 0) # velocity starts at 0

    def collide(self, going_down, map_blocks):
        for block in map_blocks:
            if pygame.sprite.collide_rect(self, block):

                if isinstance(block, Spike):
                    self.dead = True

                # if we are colliding with a platform block
                if isinstance(block, Block):
                    if going_down > 0:
                        # when you land on top of a block
                        self.rect.bottom = block.rect.top
                        self.velocity.y = 0
                        self.onGround = True #player now on ground after landing
                        self.isJumping = False # reset jump

                    # collision from the top
                    if going_down < 0:
                        self.rect.top = block.rect.bottom
                        self.dead = True

                    # collision from the side
                    else:
                        self.velocity.x = 0
                        self.rect.right = block.rect.left
                        self.dead = True

                if isinstance(block, End):
                    self.won = True

    def jump(self):
        self.velocity.y -= self.jump_height

    def update(self):

        # start the jump if necessary
        if self.isJumping == True:
            if self.onGround == True:
                self.jump()
        
        # middle of jump
        if self.onGround == False:
            self.velocity = self.velocity + GRAVITY

        # x direction collisions
        self.collide(0, self.platforms)

        self.rect.top = self.rect.top + self.velocity.y

        # assuming player is in air
        self.onGround = False
        # y direction collisions
        self.collide(self.velocity.y, self.platforms)
        
        # evaluate outcomes
        if self.won == True:
            show_win_screen()
        elif self.dead == True:
            show_death_screen()


"""
called after player death or level finish to reset level, or hits restart button
"""
def reset_level(cur_level, avatar, player, player_sprite, elements):
    player_sprite = pygame.sprite.Group()
    elements = pygame.sprite.Group()
    player = Player(avatar,  (150, 150), elements, player_sprite)
    init_level(create_map(cur_level), elements)
    return player
    