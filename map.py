# Sprite = any object on the screen that can move around

# class Animal():
#     def __init__(self):
#         pass
    
#     def sleep(self):
#         # sleep stuff
#         sleep()

#     make_noise()
#     number_of_feet
#     height


# class Dog(Animal):
#   def  __init__(self, bark_volume):
#         super().__init__()
#         self.bark_vol = bark_volume

#   def bark(self):
#         do something with bark volume
    
#   def sleep(self):
#       eat()
#       wag_tail()
#       super().sleep()
import pygame
"""
Super Class for all sprite objects that are part of the map
"""
class MapSprite(pygame.sprite.Sprite):

    def __init__(self, image, pos, *groups):
        super().__init__(*groups) # initializing the object
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)


class Block(MapSprite):
    def __init__(self, image, pos, *groups):
        super().__init__(image,pos,*groups)
        
class Spike(MapSprite):
    def __init__(self, image, pos, *groups):
        super().__init__(image,pos,*groups)    

class Coin(MapSprite):
    def __init__(self, image, pos, *groups):
       super().__init__(image,pos,*groups)

# placed at end of level
class End(MapSprite):
    def __init__(self, image, pos, *groups):
        super().__init__(image,pos,*groups)
        
