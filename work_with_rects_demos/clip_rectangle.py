import pygame
from pygame.locals import *

"""
The method r0.clip(r1) returns a new rectangle which is the intersection 
of the two rectangles. 
The method r0.union(r1) returns a new rectangle which is the union 
of the two rectangles.

The program belows shows two rectangles in red and blue outline. 
The green rectangle is the clipped area (intersection). 
The yellow rectangle is the union of the two rectangles.
"""

width = 500
heigth = 200
SIZE = (width, heigth)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
GRAY = (150, 150, 150)

dir = {
    K_LEFT: (-5, 0), K_RIGHT: (5, 0), 
    K_UP: (0, -5), K_DOWN: (0, 5)}

pygame.init()
screen = pygame.display.set_mode(SIZE)

r0 = Rect(50, 60, 200, 80)
r1 = Rect(100, 20, 100, 140)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key in dir:
                r1.move_ip(dir[event.key])
    
    clip = r0.clip(r1)
    union = r0.union(r1)

    screen.fill(GRAY)
    pygame.draw.rect(screen, YELLOW, union, 0)
    pygame.draw.rect(screen, GREEN, clip, 0)
    pygame.draw.rect(screen, RED, r1, 4)
    pygame.draw.rect(screen, BLUE, r0, 4)
    pygame.display.flip()

pygame.quit()