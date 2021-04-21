
class Settings:
    """A class to store all settings for Super Sprite."""

    def __init__(self):
        """Initialize game's settings."""

        # Screen settings
        self.screen_width = 500
        self.screen_height = 480
        self.screen_size = (self.screen_width, self.screen_height)
        self.background_path = 'raw_media/bg.jpg'

        # Player Settings
        self.sprite_speed = 5
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)