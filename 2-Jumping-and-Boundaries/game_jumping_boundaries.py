import pygame

# initialize pygame modules
pygame.init()

# set game widow & caption
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First Game')

# set position, height, width, and velocity
x, y = 50, 440
width, height = 40, 60
vel = 5

# set up main loop
run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # get pressed key on the keyboard
    keys = pygame.key.get_pressed()

    # test which key pressed to make moves
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
