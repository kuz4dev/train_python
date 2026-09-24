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
    
    # отображение прямоугольника (размеры) корабля
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    # смотрит жив ли корабль
    @property
    def is_alive(self):
        return self.lives > 0
    
    # отображение корабля
    def draw(self):
        cfg.screen.blit(self.image, (self.x, self.y))
        
    # перемещение верх-вниз
    def move(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
            
        self.clamp_to_screen()

    # ограничение экрана
    def clamp_to_screen(self):
        if self.y < self.height / 2:
            self.y = self.height / 2
        if self.y > cfg.HEIGHT - self.height:
            self.y = cfg.HEIGHT - self.height
            
    # Ведем не полноценную стрельбу, а просто создаем снаряд и возвращаем его координаты
    def shoot(self):
        return {"x": self.x + self.width, "y": self.y + (self.height // 2)}

    # уменьшает жизни при попадании метеорита и возвращает True если корабль жив, False если корабль уничтожен
    def minus_lives(self):
        self.lives -= 1
        return self.is_alive