import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    global bullets
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bullet1 = pygame.Rect(12,0,3,10)
        self.bullet2 = pygame.Rect(35,0,3,10)

        self.bullet1.midleft = ai_game.ship.rect.midleft
        self.bullet2.midright = ai_game.ship.rect.midright

        self.y1 = float(self.bullet1.y)
        self.y2 = float(self.bullet2.y)
    
    def update(self):
        self.y1 -= self.settings.bullet_speed1
        self.bullet1.y = self.y1
        self.y2 -= self.settings.bullet_speed2
        self.bullet2.y = self.y2

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.settings.bullet_color1,self.bullet1)
        pygame.draw.rect(self.screen, self.settings.bullet_color2, self.bullet2)

