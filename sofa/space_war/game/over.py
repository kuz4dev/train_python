import pygame
import os

from configuration import config as cfg
from .button import Button


# пока показывает экран проигрыша
def gameover_screen(): 
    button_over = Button("Закрыть") 
    button_game = Button("Начать новую игру")
    # музыка геймовера  
    pygame.mixer.music.stop()
    pygame.mixer.music.load(cfg.music["over_track"])
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
    
    while cfg.showing_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cfg.showing_game_over = False
            if button_over.is_clicked(event):
                #закрытие конечного окна
                cfg.showing_game_over = False
            if button_game.is_clicked(event):
                main_game()

        cfg.screen.blit(cfg.over_background_image, (0, 0))
        button_over.draw()
        button_game.draw()

        pygame.display.flip()
        cfg.clock.tick(60)