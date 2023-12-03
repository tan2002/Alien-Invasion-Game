import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = (230,230,250)
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def runGame(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_aliens()
            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet1 = Bullet(self,self.settings.bullet1)
        new_bullet2 = Bullet(self,self.settings.bullet2)

        new_bullet1.rect.x -= 25
        new_bullet2.rect.x += 25
        self.bullets.add(new_bullet1,new_bullet2)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.update()
            bullet.draw_bullet()

        self.aliens.update()
        self.aliens.draw(self.screen)

        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        pygame.display.flip()

    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number + 5
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_of_alien = available_space_x//(2*alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height-(3*alien_height) - ship_height)
        number_rows = available_space_y//(2*alien_height)
    
        for row_number in range(number_rows):
            for alien_number in range(number_of_alien):
                self._create_alien(alien_number,row_number) 
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
if __name__=='__main__':
    ai = AlienInvasion()
    ai.runGame()