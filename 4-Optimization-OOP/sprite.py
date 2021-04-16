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
        self.rect.bottomleft = self.window_rect.bottomleft
        self.settings = sprite_game.settings
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # self.width = width
        # self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_volume = 10
        self.inverter = 1
        # movement flags
        self.moving_right = False
        self.moving_left = False
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
    
    def update(self):
        """Update the sprite's position based on the movement flags"""
        if self.moving_right and self.rect.right < self.window_rect.right:
            self.x += self.settings.sprite_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.sprite_speed
        if self.is_jump:
            self.jump()
        
        # update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self):
        """Draw the Character at its current location"""
        if self.walk_counter + 1 >= 27:
            self.walk_counter = 0
        
        if self.moving_right:
            self.window.blit(self.walk_right[self.walk_counter//3], self.rect)
            self.walk_counter += 1
        elif self.moving_left:
            self.window.blit(self.walk_left[self.walk_counter//3], self.rect)
            self.walk_counter += 1
        else:
            self.window.blit(self.image, self.rect)

    def jump(self):
        if self.jump_volume >= -10:
            inverter = 1
            if self.jump_volume < 0:
                inverter = -1
            self.y -= (self.jump_volume ** 2) * 0.5 * inverter
            self.jump_volume -= 1
        else:
            self.is_jump = False
            self.jump_volume = 10
    
