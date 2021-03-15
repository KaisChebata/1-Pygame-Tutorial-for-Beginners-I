import pygame
from pygame.locals import *

"""
A Rect object can be created by giving:
Rect(left, top, width, height)
Rect(pos, size)
Rect(obj)
"""

"""
- Virtual attributes:
    - The Rect object has several virtual attributes which can be used 
     to move and align the Rect. 
     Assignment to these attributes just moves the rectangle 
     without changing its size:
     * x, y
     * top, left, bottom, right
     * topleft, bottomleft, topright, bottomright
     * midtop, midleft, midbottom, midright
     * center, centerx, centery.
    - The assignment of these 5 attributes changes the size of the rectangle, 
      by keeping its top left position:
      * size, width, height, w, h
"""

SIZE = 500, 200
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50, 60, 200, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    pygame.display.flip()


pygame.quit()