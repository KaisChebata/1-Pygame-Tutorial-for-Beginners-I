import sys

import pygame

from settings import Settings
from sprite import Player

class SuperSprite:
    """Overall class to manage game assets and behavoir."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.window = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption('Super Sprite')
        self.sprite = Player(self)
        self.background = pygame.image.load(self.settings.background_path)
    
    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.sprite.update()
            self._update_screen()

    def _check_events(self):
        """Response to Keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.sprite.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.sprite.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.sprite.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.sprite.moving_left = False
    
    def _update_screen(self):
        """Update images on the screen, and flip (update) to the new screen."""
        self.window.blit(self.background, (0, 0))
        self.sprite.draw()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    super_sprite = SuperSprite()
    super_sprite.run_game()

