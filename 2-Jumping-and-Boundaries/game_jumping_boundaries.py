import pygame

# initialize pygame modules
pygame.init()

# set game widow & caption
screen_width = 500
screen_height = 500
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First Game')

# set position, height, width, and velocity
x, y = 50, 425
width, height = 40, 60
vel = 5

# set jumping state
is_jump = False
jump_count = 10

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
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel
    if not is_jump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_height - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
