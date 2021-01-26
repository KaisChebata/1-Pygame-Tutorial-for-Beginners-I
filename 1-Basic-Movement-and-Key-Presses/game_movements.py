import pygame

pygame.init()

# set window size
win = pygame.display.set_mode((500, 500))

# set caption
pygame.display.set_caption('First Game')

# initializing attributes values to make a character drawing & move on the screen
# character attributes:
# set position:
x, y = 50, 50

# set width and height
width, height = 40, 60

# set velocity which is how fast the character will moves
vel = 5

# main loop
run = True
while run:
    # set time delay
    pygame.time.delay(100)
    
    # checking for events
    # checking for closing window game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # moving the character (shape)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()