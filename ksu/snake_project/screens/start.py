import pygame
from game import (

)

def show_start(screen, pause_font, clock):
    while start_screen:
        screen.fill((161,241,247))
        
        opening_text = pause_font.render(f"Нажмите пробел для начала игры", True, (82,87,91))
        opening_text_rect = opening_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(opening_text, opening_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_screen = False
                    running = True

        pygame.display.flip()
        
        clock.tick(speed)