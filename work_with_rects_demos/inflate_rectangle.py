from rect import *

pygame.display.set_caption('Inflate a rectangle')

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.inflate_ip(v)
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect0, 1)
    pygame.draw.rect(screen, RED, rect, 4)
    pygame.display.flip()

pygame.quit()