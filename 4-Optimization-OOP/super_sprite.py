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
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        # Running game in full screen mode
        # self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.window.get_rect().width
        # self.settings.screen_height = self.window.get_rect().height
        pygame.display.set_caption('Super Sprite')
        self.sprite = Player(self)
        self.background = pygame.image.load(self.settings.background_path)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self.clock.tick(27)
            self._check_events()
            self.sprite.update()
            self._update_screen()

    def _check_events(self):
        """Response to Keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to Keypresses"""
        if event.key == pygame.K_RIGHT:
            self.sprite.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.sprite.moving_left = True
        elif event.key == pygame.K_SPACE and not self.sprite.is_jump:
            self.sprite.is_jump = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Respond to Keypresses"""
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

