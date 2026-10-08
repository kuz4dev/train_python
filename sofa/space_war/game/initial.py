import pygame
import os

from configuration import config as cfg
from .button import Button


# пока показывает начальный экран
def initial_screen():
    button = Button("Играть")
    
    while cfg.initial_window:
        #показ заднего фона
        cfg.screen.blit(cfg.start_background_image, (0, 0))

        button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cfg.initial_window = False
                
            if button.is_clicked(event):
                #закрытие начального окна
                cfg.initial_window = False
                #открытие игры
                cfg.running = True
                
                #музыка
                pygame.mixer.music.load(os.path.join(cfg.ASSETS_DIR, "main_track.mp3"))
                pygame.mixer.music.set_volume(0.15)
                pygame.mixer.music.play(-1)

        pygame.display.flip()
        cfg.clock.tick(60)