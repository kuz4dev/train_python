import pygame
import os

from configuration import (
    WIDTH,
    HEIGHT,
    ASSETS_DIR,
    running,
)

def initial_screen(screen, game_over, start_background_image, initial_window):
    started = False
    
    while initial_window:
        screen.blit(start_background_image, (0, 0))
        
        opening_text = game_over.render(f"R - для начала игры", True, (255,242,97))
        opening_text_rect = opening_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(opening_text, opening_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    initial_window = False
                    started = True
                    pygame.mixer.music.load(os.path.join(ASSETS_DIR, "main_track.mp3"))
                    pygame.mixer.music.set_volume(0.15)
                    pygame.mixer.music.play(-1)

        pygame.display.flip()
        
    return started