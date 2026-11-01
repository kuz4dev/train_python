import pygame
import os

from configuration import config as cfg
from .button import Button
from configuration import reset_game
from .record import load, save


# пока показывает экран проигрыша
def gameover_screen(): 
    button_over = Button("Закрыть", 400) 
    button_game = Button("Начать новую игру")
    # музыка геймовера  
    pygame.mixer.music.stop()
    pygame.mixer.music.load(cfg.music_loader["over_track"])
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
    
    # сохранение результата в json файл
    read_record = load()
    print(f"Предыдущий рекорд: {read_record}")
    if cfg.score > read_record:
        print(f"Новый рекорд: {cfg.score}")
        save(cfg.score)

    text1 = cfg.font.render(f"Рекорд игры: {cfg.score}", True, (255, 255, 255))
    control_text1 = text1.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))

    text2 = cfg.font.render(f"Лучший рекорд: {read_record}", True, (255, 255, 255))
    control_text2 = text2.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2 - 20))

    while cfg.showing_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cfg.showing_game_over = False
                cfg.new_game = False
            if button_over.is_clicked(event):
                #закрытие конечного окна
                cfg.showing_game_over = False
                cfg.new_game = False
            if button_game.is_clicked(event):
                #закрытие конечного окна
                cfg.showing_game_over = False
                cfg.initial_window = True
                # надо добавить функцию сброса значений
                reset_game()

        cfg.screen.blit(cfg.over_background_image, (0, 0))
        cfg.screen.blit(text1, control_text1)
        cfg.screen.blit(text2, control_text2)
        button_over.draw()
        button_game.draw()

        pygame.display.flip()
        cfg.clock.tick(60)