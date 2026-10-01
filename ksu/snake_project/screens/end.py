import pygame

from game import config as cfg

def show_end(screen, pause_font, clock):
    # окно конца игры
    while cfg.game_over:

        screen.blit(cfg.bedroom_background, (0, 0))
        screen.blit(cfg.console_image, cfg.console_rect)

        go_show_score = pause_font.render(f"Игра закончена! Ваш счет: {cfg.score}", True, (219,236,250))
        go_score_rect = go_show_score.get_rect(center = (cfg.WIDTH // 2, (cfg.HEIGHT // 2) + 30))
        screen.blit(go_show_score, go_score_rect)

        exit_go_text = pause_font.render("Нажмите X для выхода", True, (219,236,250))
        go_exit_rect = exit_go_text.get_rect(center = (cfg.WIDTH // 2, (cfg.HEIGHT // 2) + 25) )
        screen.blit(exit_go_text, go_exit_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    cfg.game_over = False

        pygame.display.flip()
            
        clock.tick(cfg.speed)