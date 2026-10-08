import pygame
import os

from configuration import config as cfg
from .button import Button


# пока показывает экран проигрыша
def gameover_screen(): 
    button = Button("Закрыть") 
    # музыка геймовера  
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(cfg.ASSETS_DIR, "over_track.mp3"))
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
    
    while cfg.showing_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cfg.showing_game_over = False
            if button.is_clicked(event):
                #закрытие конечного окна
                cfg.showing_game_over = False


        cfg.screen.blit(cfg.over_background_image, (0, 0))
        button.draw()

        pygame.display.flip()
        cfg.clock.tick(60)