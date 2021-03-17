from rect import *

"""
- The function rect.collidepoint(pos) returns True 
  if the point collides with the rectangle.
- we move the rectangle by the relative motion of the mouse event.rel.

- The boolean variable `moving` is set when the mouse button 
  goes down inside the rectangle. 
  It remains True until the button goes up again. 
  The rectangle is only moved when the mouse click has happened 
  inside the rectangle. 
  While the rectangle is moving, we add a blue outline.
"""

pygame.display.set_caption('Move rect with mouse')

rect = Rect(50, 60, 200, 80)
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        
        elif event.type == MOUSEBUTTONUP:
            moving = False
        
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    if moving:
        pygame.draw.rect(screen, BLUE, rect, 4)
    pygame.display.flip()

pygame.quit()