import pygame
import os

from configuration import config as cfg
from .button import Button
from configuration import reset_game


# пока показывает экран проигрыша
def gameover_screen(): 
    button_over = Button("Закрыть", 400) 
    button_game = Button("Начать новую игру")
    # музыка геймовера  
    pygame.mixer.music.stop()
    pygame.mixer.music.load(cfg.music_loader["over_track"])
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
    
    while cfg.showing_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cfg.showing_game_over = False
                cfg.new_game = False
            if button_over.is_clicked(event):
                #закрытие конечного окна
                cfg.showing_game_over = False
                cfg.new_game = False
            if button_game.is_clicked(event):
                #закрытие конечного окна
                cfg.showing_game_over = False
                cfg.initial_window = True
                # надо добавить функцию сброса значений
                reset_game()

        cfg.screen.blit(cfg.over_background_image, (0, 0))
        button_over.draw()
        button_game.draw()

        pygame.display.flip()
        cfg.clock.tick(60)