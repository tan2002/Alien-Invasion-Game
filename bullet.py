import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game,bullet_type):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.speed, self.color = bullet_type

        self.rect = pygame.Rect(0, 0,3,15)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
