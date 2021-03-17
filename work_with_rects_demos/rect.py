"""Helper module contains all necessary imports and declarations"""

import pygame
from pygame.locals import *


width, height = 500, 200
SIZE = (width, height)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE =(0, 0, 255)

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

pygame.init()

screen = pygame.display.set_mode(SIZE)
font = pygame.font.Font(None, 24)

running = True