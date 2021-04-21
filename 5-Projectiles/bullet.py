import pygame
from pygame.sprite import Sprite

class Projectile(Sprite):
    """A Class to manage projectiles fired from the Character (Sprite)"""

    def __init__(self, sprite_game):
        """Create a Bullet object at Sprite's current position."""
        super.__init__()
        self.window = sprite_game.window
        self.settings = sprite_game.settings
        self.color = self.settings.bullet_color

        # Create a Bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = sprite_game.sprite.rect.midtop

        # store the bullet's as a decimal value.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move Bullet up the screen."""
        # Update the decimal postion of the bullet.
        self.y -= self.settings.bullet_speed

        # update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the Bullet to the screen"""
        pygame.draw.rect(self.window, self.color, self.rect)