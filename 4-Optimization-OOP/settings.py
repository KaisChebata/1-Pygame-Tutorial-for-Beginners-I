
class Settings:
    """A Class to store all settings for Super Sprite Game."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen Settings
        self.screen_width = 500
        self.screen_height = 480
        self.background_path = 'raw_media/bg.jpg'

        # Sprite settings
        self.sprite_speed = 5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)