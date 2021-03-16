import pygame
from pygame.locals import *

"""
The Rect class defines 4 cornerpoints, 4 mid points and 1 centerpoint.
"""

SIZE = 500, 200
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Points of interest')

font = pygame.font.Font(pygame.font.get_default_font(), 15)

def draw_point(text, pos):
    img = font.render(text, True, BLACK)
    pygame.draw.circle(screen, RED, pos, 3)
    screen.blit(img, pos)

rect = Rect(50, 40, 250, 80)
pts = (
    'topleft', 'topright', 'bottomleft', 'bottomright',
    'midtop', 'midright', 'midbottom', 'midleft', 'center'
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect, 3)

    for pt in pts:
        draw_point(pt, eval('rect.' + pt))
        
    pygame.display.flip()

pygame.quit()