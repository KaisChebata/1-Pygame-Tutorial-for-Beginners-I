from rect import *

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

pygame.display.set_caption('Virtual attributes')

rect = Rect(50, 60, 200, 80)
blue_rect = Rect(300, 60, 150, 80)
print(f'Red rect attributes: {rect}')
print(f'x = {rect.x}, y = {rect.y}, w = {rect.w}, h = {rect.h}')
print(f'left = {rect.left}, top = {rect.top}, right = {rect.right}, '
      f'bottom = {rect.bottom}')
print(f'height = {rect.height}, width = {rect.width}')
print(f'center = {rect.center}')

# running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    pygame.draw.rect(screen, (0, 0, 255), blue_rect)
    pygame.display.flip()


pygame.quit()