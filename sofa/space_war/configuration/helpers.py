from configuration import config as cfg
import pygame

def reset_game():
    cfg.score = 0
    cfg.bullets = []
    cfg.meteorits = []
    cfg.spawn_timer = 0
    cfg.paused = False
    cfg.music = False
    pygame.mixer.music.stop()