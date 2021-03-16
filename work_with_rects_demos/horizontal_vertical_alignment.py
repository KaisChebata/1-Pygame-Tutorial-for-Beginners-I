import pygame
from pygame.locals import *
from pygame.rect import *

"""
In the following example we use 3 keys to align a rectangle horizontally:

    L - left
    C - center
    R - right

and 3 other keys to align the rectangle vertically:

    T - top
    M - middle
    B - bottom
"""
SIZE = (500, 200)
width, height = SIZE
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Horizontal and vertical alignment')

rect = Rect(50, 60, 200, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_l:
                rect.left = 0
            if event.key == K_c:
                rect.centerx = width // 2
            if event.key == K_r:
                rect.right = width
            
            if event.key == K_t:
                rect.top = 0
            if event.key == K_m:
                rect.centery = height // 2
            if event.key == K_b:
                rect.bottom = height
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect)
    pygame.display.flip()

pygame.quit()