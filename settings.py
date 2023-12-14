class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 250)
        self.ship_speed = 1.5
        self.ship_limit = 3

        self.bullet1 = (1.0, (255, 0, 0))
        self.bullet2 = (1.0, (255, 0, 0))
        self.bullet1_speed = 1.5
        self.bullet2_speed = 1.5

        self.alien_speed = 1.0
        self.fleet_drop_speed = 8
        self.fleet_direction = 1
        self.score_scale = 1.5
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet1_speed = 3.0
        self.bullet2_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet1_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
