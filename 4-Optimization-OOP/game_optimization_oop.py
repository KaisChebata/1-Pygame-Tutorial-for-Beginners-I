import pygame

# initializing pygame modules
pygame.init()

# set up game clock
clock = pygame.time.Clock()

# set game window, caption, img background
screen_width = 500
screen_height = 480
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First Game')
background = pygame.image.load('raw_media/bg.jpg')

# character class
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velo = 5
        self.is_jump = False
        self.jump_volume = 10
        self.left = False
        self.right = False
        self.walk_counter = 0
    
    def draw(self, window):
        if self.walk_counter + 1 >= 27:
            self.walk_counter = 0
        
        if self.left:
            window.blit(walk_left[self.walk_counter//3], (self.x, self.y))
            self.walk_counter += 1
        elif self.right:
            window.blit(walk_right[self.walk_counter//3], (self.x, self.y))
            self.walk_counter += 1
        else:
            window.blit(char, (self.x, self.y))


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

# initializing player character
sprite = Player(50, 400, 64, 64)

# drawing window game
def redraw_game_window():
    window.blit(background, (0, 0))
    sprite.draw(window)
    pygame.display.update()

# set up main loop
run = True
while run:
    # set up FPS
    clock.tick(27)

    # get exit event when Quit button clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # get pressed keys on the keyboard
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and sprite.x > sprite.velo:
        sprite.x -= sprite.velo
        sprite.left = True
        sprite.right = False
    elif keys[pygame.K_RIGHT] and sprite.x < screen_width - sprite.width - sprite.velo:
        sprite.x += sprite.velo
        sprite.right = True
        sprite.left = False
    else:
        sprite.right = False
        sprite.left = False
        sprite.walk_counter = 0
    
    if not sprite.is_jump:
        if keys[pygame.K_SPACE]:
            sprite.is_jump = True
            sprite.right = False
            sprite.left = False
            sprite.walk_counter = 0
    else:
        if sprite.jump_volume >= -10:
            invert = 1
            if sprite.jump_volume < 0:
                invert = -1
            sprite.y -= (sprite.jump_volume ** 2) * 0.5 * invert
            sprite.jump_volume -= 1
        else:
            sprite.is_jump = False
            sprite.jump_volume = 10

    # draw window & character
    redraw_game_window()
    
pygame.quit()