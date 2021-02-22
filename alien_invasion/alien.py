import pygame
from pygame.sprite import Sprite

from _utils import resource_path


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(resource_path('images/alien.bmp'))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.settings.fleet_direction_x > 0:
            self.x += self.settings.fleet_speed_x
        elif self.settings.fleet_direction_x < 0:
            self.x -= self.settings.fleet_speed_x
        self.rect.x = self.x

    def check_edges(self):
        """check if the alien is touching the left or right edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
            return True
        return False
