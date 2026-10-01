import pygame

from game import config as cfg

def show_start(screen, pause_font, clock):
    while cfg.start_screen:
        screen.blit(cfg.bedroom_background, (0, 0))
        screen.blit(cfg.console_image, cfg.console_rect)
        
        opening_text = pause_font.render(f"Нажмите пробел для начала игры", True, (219,236,250))
        opening_text_rect = opening_text.get_rect(center = (cfg.WIDTH // 2, (cfg.HEIGHT // 2) + 30))
        screen.blit(opening_text, opening_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cfg.start_screen = False
                    cfg.running = True

        pygame.display.flip()
        
        clock.tick(cfg.speed)