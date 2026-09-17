import pygame
import os

from configuration import config as cfg

def initial_screen():
    while cfg.initial_window:
        cfg.screen.blit(cfg.start_background_image, (0, 0))
        
        opening_text = cfg.game_over.render(f"R - для начала игры", True, (255,242,97))
        opening_text_rect = opening_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))
        cfg.screen.blit(opening_text, opening_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    cfg.initial_window = False
                    cfg.running = True
                    pygame.mixer.music.load(os.path.join(cfg.ASSETS_DIR, "main_track.mp3"))
                    pygame.mixer.music.set_volume(0.15)
                    pygame.mixer.music.play(-1)

        pygame.display.flip()