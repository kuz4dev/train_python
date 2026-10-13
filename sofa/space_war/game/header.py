import pygame
from configuration import config as cfg

class Header:
    def __init__(self):
        # добавить изображение для жизней
        self.live_image = cfg.live_image 
        self.meteor_image = cfg.meteorit_image
        self.lives_count = cfg.lives
        self.score = cfg.score
        self.image_size = 30
        self.indent = 25
        # добавить параметр для цвета текстов

    def draw(self, screen):
        self.draw_lives(screen, self.lives_count)
        self.draw_score(screen, self.score)

        
    # def draw_lives(self, lives):
        
    # def draw_score(self, score):
    
    # #Счет
            # score_text = cfg.font.render(f"Метеоритов отбито: {cfg.score}", True, (255, 255, 255))
            # #Жизни
            # lives_text = cfg.font.render(f"Полная поломка через: {ship.lives}", True, (255, 255, 255))
            # #вывод текстов
            # cfg.screen.blit(score_text, (25, 25))
            # cfg.screen.blit(lives_text, (cfg.WIDTH - 360, 25))
