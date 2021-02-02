import pygame

pygame.init()

# set game clock
clock = pygame.time.Clock()

# set size of window game, caption, and background
screen_width = 500
screen_height = 480
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First Game')
background = pygame.image.load('raw_media/bg.jpg')

# character position, width, height, imgs, and velocity
x, y = 50, 400
width, height = 64, 64
velo = 5

char = pygame.image.load('raw_media/standing.png')

# walk right list imgs 
walk_right = [
    pygame.image.load('raw_media/R1.png'), pygame.image.load('raw_media/R2.png'), 
    pygame.image.load('raw_media/R3.png'), pygame.image.load('raw_media/R4.png'), 
    pygame.image.load('raw_media/R5.png'), pygame.image.load('raw_media/R6.png'), 
    pygame.image.load('raw_media/R7.png'), pygame.image.load('raw_media/R8.png'), 
    pygame.image.load('raw_media/R9.png')
    ]

# walk left list imgs
walk_left = [
    pygame.image.load('raw_media/L1.png'), pygame.image.load('raw_media/L2.png'), 
    pygame.image.load('raw_media/L3.png'), pygame.image.load('raw_media/L4.png'), 
    pygame.image.load('raw_media/L5.png'), pygame.image.load('raw_media/L6.png'), 
    pygame.image.load('raw_media/L7.png'), pygame.image.load('raw_media/L8.png'), 
    pygame.image.load('raw_media/L9.png')
    ]

# jumping state
is_jump = False
jump_volume = 10

# tracking character state
left = False
right = False
walk_counter = 0

# drawing window game
def redraw_game_window():
    global walk_counter
    window.blit(background, (0, 0))
    
    # we will make the max of walk_count is 27 as each list of walk_left 
    # and walk_right has 9 imgs for a list 
    # and we'll display each sprite for 3 frame
    if walk_counter + 1 >= 27:
        walk_counter = 0
        
    if left:
        window.blit(walk_left[walk_counter//3], (x, y))
        walk_counter += 1
    elif right:
        window.blit(walk_right[walk_counter//3], (x, y))
        walk_counter += 1
    else:
        window.blit(char, (x, y))
    
    pygame.display.update()

# set up main loop
run = True
while run:
    # set up frame rate
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # get pressed keys on the keyboard
    keys = pygame.key.get_pressed()

    # test which key pressed to make movements, set character
    # inside window, and add jumping effect
    if keys[pygame.K_LEFT] and x > velo:
        x -= velo
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width - width - velo:
        x += velo
        right = True
        left = False
    else:
        right = False
        left = False
        walk_counter = 0

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_counter = 0
    else:
        if jump_volume >= -10:
            invert = 1
            if jump_volume < 0:
                invert = -1
            y -= (jump_volume ** 2) * 0.5 * invert
            jump_volume -= 1
        else:
            is_jump = False
            jump_volume = 10
    
    # draw window & character
    redraw_game_window()

pygame.quit()