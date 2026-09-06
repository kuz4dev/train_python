import pygame
import os

from configuration import (
    WIDTH, HEIGHT,
)

#пока показывает экран проигрыша
def gameover_screen(screen, game_over, over_background_image, showing_game_over):
    while showing_game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x or event.type == pygame.QUIT:
                    showing_game_over = False

        screen.blit(over_background_image, (0, 0))

        #текст
        game_over_text = game_over.render("Игра окончена!", True, (255, 255, 255))
        game_over_X = game_over.render("Нажмите X, чтобы закрыть игру.", True, (255, 255, 255))

        #вывод текста
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        screen.blit(game_over_X, (WIDTH // 2 - game_over_X.get_width() // 2, HEIGHT - game_over_X.get_height() // 2 - 30))

        pygame.display.flip()