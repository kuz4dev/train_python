import pygame
import os

from configuration import config as cfg
from .button import Button


# пока показывает начальный экран
def initial_screen():
    while cfg.initial_window:
        #показ заднего фона
        cfg.screen.blit(cfg.start_background_image, (0, 0))

        button = Button
        button_rect = button.rect

        button_rect
        button.draw

        #текст
        opening_text = cfg.game_over.render(f"R - для начала игры", True, (255,242,97))
        opening_text_rect = opening_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))
        cfg.screen.blit(opening_text, opening_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # если r нажата
                if button.is_clicked:
                # if event.scancode == pygame.KSCAN_R:
                    #закрытие начального окна
                    cfg.initial_window = False
                    #открытие игры
                    cfg.running = True
                    
                    #музыка
                    pygame.mixer.music.load(os.path.join(cfg.ASSETS_DIR, "main_track.mp3"))
                    pygame.mixer.music.set_volume(0.15)
                    pygame.mixer.music.play(-1)

        pygame.display.flip()