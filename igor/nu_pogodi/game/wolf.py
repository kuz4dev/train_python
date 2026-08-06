import pygame

from game import config

# Класс волка
class Wolf:
    def __init__(self):
        self.width = config.wolf_width
        self.height = config.wolf_height
        self.x = config.wolf_x
        self.y = config.wolf_y
        self.speed = config.wolf_speed
        
    def update(self, keys, dt):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * dt
            
        self.x = max(0, min(self.x, config.WIDTH - self.width))
        
    @property
    def basket_left(self):
        return self.x + (self.width - config.basket_width) // 2
    
    @property
    def basket_right(self):
        return self.basket_left + config.basket_width
    
    @property
    def basket_top(self):
        return self.y
    
    def draw(self, screen, asset):
        screen.blit(asset, (self.x, self.y))
