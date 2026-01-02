import pygame
import random

pygame.init()



SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2



BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class SPRITE(pygame.sprite.SPRITE):


  def __init__(self, color, height, width):


    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill(color)

    self.rect = self.image.get_rect

    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1]) ]