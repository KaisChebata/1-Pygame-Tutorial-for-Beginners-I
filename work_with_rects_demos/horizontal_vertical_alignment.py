from rect import *

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

pygame.display.set_caption('Horizontal and vertical alignment')

rect = Rect(50, 60, 200, 80)

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