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

while cfg.new_game:
    initial_screen()
    playng_game()
    gameover_screen()

pygame.display.flip()
pygame.quit()

# TODO:
# Идеи для улучшения игры от Игоря:
# 2. Двигать задний фон - имитацию движения - найти похожие изображения

# Идеи для улучшения игры от Софы:
# 2. эффект полета пуль и метеоритов
# 3. сохранение рекорда в json файл и определение лучшего. мб время игры записывать

# Далекие планы - сохранение в файл
