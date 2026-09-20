from configuration import config as cfg
import pygame

class Spaceship:
    def __init__(self):
        self.width = cfg.spaceship_width
        self.height = cfg.spaceship_height
        self.x = cfg.spaceship_x
        self.y = cfg.spaceship_y
        self.image = cfg.spaceship_image
        self.speed = cfg.spaceship_speed
        self.lives = cfg.lives
        
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    @property
    def is_alive(self):
        return self.lives > 0
    # Boolean - True или False - or and == != > < >= <=
        
    def draw(self):
        cfg.screen.blit(self.image, (self.x, self.y))
        
    def move(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
            
        self.clamp_to_screen()
            
    def clamp_to_screen(self):
        if self.y < self.height / 2:
            self.y = self.height / 2
        if self.y > cfg.HEIGHT - self.height:
            self.y = cfg.HEIGHT - self.height
            
    # Ведем не полноценную стрельбу, а просто создаем снаряд и возвращаем его координаты
    def shoot(self):
        
    #уменьшает жизни при попадании метеорита и возвращает True если корабль жив, False если корабль уничтожен
    def minus_lives(self):
