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
                    print("touched spike! \n")
                    self.dead = True

                # if we are colliding with a platform block
                if isinstance(block, Block):
                    if going_down > 0:
                        print("in first case")
                        # when you land on top of a block
                        self.rect.bottom = block.rect.top
                        self.velocity.y = 0
                        self.onGround = True #player now on ground after landing
                        self.isJumping = False # reset jump

                    # collision from the top
                    elif going_down < 0:
                        self.rect.top = block.rect.bottom

                    # collision from the side
                    else:
                        print("collision with block from side")
                        self.velocity.x = 0
                        self.rect.right = block.rect.left
                        self.dead = True

                if isinstance(block, End):
                    self.won = True

    def jump(self):
        self.velocity.y -= self.jump_height

    def update(self, jumping_status, elements, screen, player_sprite, infoDAO):
        print("update jumping status: " ,jumping_status)
        # start the jump if necessary
        if jumping_status:
            print("update jumping\n\n")
            if self.onGround:
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
        print("dead status after collision: ", self.dead)
        
        if self.dead == True:
            infoDAO.dead = True
            # show_death_screen(elements, screen, player_sprite, infoDAO) 
        elif self.won == True:
            infoDAO.won = True
            # show_win_screen(elements, screen, player_sprite, infoDAO)




        
"""
called after player death or level finish to reset level, or hits restart button
"""
def reset_level(cur_level, avatar, player_sprite, elements, infoDAO):
    # restart music
    music = pygame.mixer_music.load("music/geodash.mp3")
    pygame.mixer_music.set_volume(0.10)
    pygame.mixer_music.play()

    infoDAO.player_sprite = pygame.sprite.Group()
    infoDAO.elements = pygame.sprite.Group()
    infoDAO.player = Player(avatar, (150, 150), elements, player_sprite)
    init_level(create_map(cur_level), infoDAO.elements)
    infoDAO.dead = False
    infoDAO.won = False

    return infoDAO.player
    
    

# another loop that will wait for a key press from the user
def wait_for_input(infoDAO):
    # start waiting
    # wait until a key gets pressed
    #   - check for key press using pygame.event.get()
    #   - handle the cases of game quit, game restart
    input = False
    while input == False:
        print("waiting for input")

        infoDAO.clock.tick(60)
        pygame.display.flip()
        
        if not infoDAO.is_started():
            print("triggering start screen")
            start_screen(infoDAO.screen, infoDAO.level, infoDAO.avatar,infoDAO.player, infoDAO.player_sprite, infoDAO.elements)
            print("after start screen in wait function\n")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                # quit game if escape
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    input = True
                    infoDAO.set_started(True)

    # start = True
    return True

def show_death_screen(elements, screen, player_sprite, infoDAO):
    print("entering death screen! \n===============")
    player_sprite.empty()
    game_over_text = font.render("Good Try", True, WHITE)

    screen.fill(pygame.Color("sienna1"))
    screen.blits([[game_over_text, (100, 100)]])

    # wait for a player to make an input because the screen would disappear really fast
    # and would restart without wating for the player's input.
    wait_for_input(infoDAO)
    reset_level(infoDAO.level, infoDAO.avatar, player_sprite, elements, infoDAO)

def show_win_screen(elements, screen, player_sprite, infoDAO):
    win_text = "Level Complete!"
    player_sprite.empty()
    won = font.render(win_text, True, GREEN)
    screen.blits([won, (100, 100)])

    wait_for_input(infoDAO)
    reset_level(infoDAO.level, infoDAO.avatar, player_sprite, elements, infoDAO)

