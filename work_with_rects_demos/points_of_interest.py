from rect import *

"""
The Rect class defines 4 cornerpoints, 4 mid points and 1 centerpoint.
"""

pygame.display.set_caption('Points of interest')

def draw_point(text, pos):
    img = font.render(text, True, BLACK)
    pygame.draw.circle(screen, RED, pos, 3)
    screen.blit(img, pos)

rect = Rect(50, 40, 250, 80)
pts = (
    'topleft', 'topright', 'bottomleft', 'bottomright',
    'midtop', 'midright', 'midbottom', 'midleft', 'center'
)

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