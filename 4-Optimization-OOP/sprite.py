import pygame

class Player:
    """A Class to manage the (Sprite Character) Player"""

    # def __init__(self, sprite_game, x, y, width, height):
    def __init__(self, sprite_game):
        """Initializing the Sprite character (player) and 
            sets its position, height, width, velocity, 
            image, jumping state, and walk state."""
        self.window = sprite_game.window
        self.window_rect = sprite_game.window.get_rect()
        self.image = pygame.image.load('raw_media/standing.png')
        self.rect = self.image.get_rect()
        # self.x = x
        # self.y = y
        # self.width = width
        # self.height = height
        self.vel = 5
        self.is_jump = False
        self.left = False
        self.right = False
        self.jump_volume = 10
        self.walk_counter = 0

        # walk right list imgs
        self.walk_right = [
            pygame.image.load('raw_media/R1.png'), 
            pygame.image.load('raw_media/R2.png'), 
            pygame.image.load('raw_media/R3.png'), 
            pygame.image.load('raw_media/R4.png'), 
            pygame.image.load('raw_media/R5.png'), 
            pygame.image.load('raw_media/R6.png'), 
            pygame.image.load('raw_media/R7.png'), 
            pygame.image.load('raw_media/R8.png'), 
            pygame.image.load('raw_media/R9.png')
        ]

        # walk left list imgs
        self.walk_left = [
            pygame.image.load('raw_media/L1.png'), 
            pygame.image.load('raw_media/L2.png'), 
            pygame.image.load('raw_media/L3.png'), 
            pygame.image.load('raw_media/L4.png'), 
            pygame.image.load('raw_media/L5.png'), 
            pygame.image.load('raw_media/L6.png'), 
            pygame.image.load('raw_media/L7.png'), 
            pygame.image.load('raw_media/L8.png'), 
            pygame.image.load('raw_media/L9.png')
        ]
        
        self.rect.bottomleft = self.window_rect.bottomleft

    def draw(self):
        """Draw the Character at its current location"""
        self.window.blit(self.image, self.rect)