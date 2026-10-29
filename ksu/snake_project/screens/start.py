import pygame
from game import Button
from game import config as cfg

start_button = Button((187, 504), 35)

def show_start(screen, pause_font, clock):
    while cfg.start_screen:
        screen.blit(cfg.bedroom_background, cfg.bedroom_rect)
        screen.blit(cfg.console_image, cfg.console_rect)
        
        opening_text = pause_font.render(f"Нажмите пробел для начала игры", True, (176,176,176))
        opening_text_rect = opening_text.get_rect(center = (cfg.WIDTH // 2, (cfg.HEIGHT // 2) - 30))
        screen.blit(opening_text, opening_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cfg.start_screen = False
                    cfg.running = True
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse button pressed at:", event.pos)
                
            if start_button.is_clicked(event):
                # какие действия 
                # начать игру
                cfg.start_screen = False
                cfg.running = True
                print('наша кнопка нажата')

        pygame.display.flip()
        
        clock.tick(cfg.speed)
        
        
# Mouse button pressed at: (813, 504) - right click
# Mouse button pressed at: (185, 504) - left click