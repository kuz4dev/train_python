import pygame

from configuration import config as cfg

from game import (
    initial_screen,
    gameover_screen,
    playng_game,
)

pygame.init()

#название игры
pygame.display.set_caption("Леталки!")

initial_screen()

playng_game()

gameover_screen()

pygame.display.flip()

pygame.quit()


#TODO:
# 1. метеориты слишком большие по прямоугольнику.
# 2. во время паузы можно выпустить пулю

# BUGS:
#  Метеориты спаунятся некорректно по оси Y, сделать ближе к правому краю экрана -- можно взять как домашку
#  Пули проходят сквозь метеориты, нужно сделать проверку на столкновение пули и метеорита