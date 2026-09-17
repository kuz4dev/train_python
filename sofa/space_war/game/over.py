import pygame
import os

from configuration import config as cfg

#пока показывает экран проигрыша
def gameover_screen():  
    #музыка геймовера  
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(cfg.ASSETS_DIR, "over_track.mp3"))
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
    
    while cfg.showing_game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x or event.type == pygame.QUIT:
                    cfg.showing_game_over = False

        

        cfg.screen.blit(cfg.over_background_image, (0, 0))

        #текст
        game_over_text = cfg.game_over.render("Игра окончена!", True, (255, 255, 255))
        game_over_X = cfg.game_over.render("Нажмите X, чтобы закрыть игру.", True, (255, 255, 255))

        #вывод текста
        cfg.screen.blit(game_over_text, (cfg.WIDTH // 2 - game_over_text.get_width() // 2, cfg.HEIGHT // 2 - game_over_text.get_height() // 2))
        cfg.screen.blit(game_over_X, (cfg.WIDTH // 2 - game_over_X.get_width() // 2, cfg.HEIGHT - game_over_X.get_height() // 2 - 30))

        pygame.display.flip()