import pygame

class Player:
    """A Class to manage the sprite (character)"""

    def __init__(self, sprite_game):
        """Initialize the sprite and set its starting position"""
        self.screen = sprite_game.screen
        self.screen_rect = sprite_game.screen.get_rect()
        self.settings = sprite_game.settings

        # load the sprite image and get its rect
        self.image = pygame.image.load('raw_media/standing.png')
        self.rect = self.image.get_rect()

        # start each new sprite at left bottom of the screen
        self.rect.bottomleft = self.screen_rect.bottomleft

        # Store a decimal values for the sprite's horizontal 
        # and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movements flags, and walk counter
        self.moving_right = False
        self.moving_left = False
        self.walk_counter = 0

        # Jumping attributes
        self.is_jump = False
        self.jump_volume = 10

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

        # animation list length
        self.anim_length = len(self.walk_right)
    
    def update(self):
        """Update the sprite position, based on the movement flag"""
        # Update the sprite's x  and y values, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.sprite_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.sprite_speed
        if self.is_jump:
            self.jump()
        
        # update rect object from self.x, and self.y
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self):
        """Draw sprite at its current location."""
        # if self.walk_counter + 1 >= 27:
        #     self.walk_counter = 0
        
        # if self.moving_right:
        #     self.screen.blit(self.walk_right[self.walk_counter//3], self.rect)
        #     self.walk_counter += 1
        # elif self.moving_left:
        #     self.screen.blit(self.walk_left[self.walk_counter//3], self.rect)
        #     self.walk_counter += 1
        # else:
        #     self.screen.blit(self.image, self.rect)
        
        if self.walk_counter >= self.anim_length:
            self.walk_counter = 0
        
        if self.moving_right:
            self.screen.blit(
                self.walk_right[self.walk_counter % self.anim_length],
                self.rect
            )
            self.walk_counter += 1
        elif self.moving_left:
            self.screen.blit(
                self.walk_left[self.walk_counter % self.anim_length],
                self.rect
            )
            self.walk_counter += 1
        else:
            self.screen.blit(self.image, self.rect)
    
    def jump(self):
        inverter = 1
        if self.jump_volume >= -10:
            if self.jump_volume < 0:
                inverter = -1
            self.y -= (self.jump_volume ** 2) * 0.5 * inverter
            self.jump_volume -= 1
        else:
            self.is_jump = False
            self.jump_volume = 10
    
