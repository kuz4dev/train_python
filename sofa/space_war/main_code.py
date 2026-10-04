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



# TODO:
# 1. Окно не закрывается крестиком
