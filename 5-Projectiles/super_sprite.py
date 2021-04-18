import sys

import pygame
from pygame.locals import *

from settings import Settings
from sprite import Player

class SuperSprite:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initializing the game, and create game's resources."""

        pygame.init()
        self.settings = Settings()

        self.clock = pygame.time.Clock()

        # full mode screen setting
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # # update settings from
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.background = pygame.image.load(self.settings.background_path)
        pygame.display.set_caption('Super Sprite')

        self.sprite = Player(self)
    
    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self.clock.tick(27)
            self._check_events()
            self.sprite.update()
            self._update_screen()
    
    def _check_events(self):
        """Response to keypresses and mouse event."""
        jumping_flag = pygame.key.get_pressed()[K_SPACE]

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == KEYUP:
                self._check_keyup_events(event)
        
        # detect jumping movement and make it continuous using 
        # pygame.key.get_pressed() function
        if jumping_flag and not self.sprite.is_jump:
            self.sprite.is_jump = True

    def _check_keydown_events(self, event):
        """Response to Keypresses."""
        if event.key == K_RIGHT:
            self.sprite.moving_right = True
        elif event.key == K_LEFT:
            self.sprite.moving_left = True
        elif event.key == K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Response to key releases."""
        if event.key == K_RIGHT:
            self.sprite.moving_right = False
        elif event.key == K_LEFT:
            self.sprite.moving_left = False
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.background, (0, 0))
        self.sprite.draw()
        
        pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game
    super_sprite = SuperSprite()
    super_sprite.run_game()