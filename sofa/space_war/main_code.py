import pygame
import random
import os

# from config import BASE_DIR, ASSETS_DIR, WIDTH, HEIGHT, screen, spaceship_width, spaceship_height, spaceship_x, spaceship_y, spaceship_speed, meteorit_x, meteorit_y, meteorit_radius, meteorit_speed, bullet_radius, bullet_speed, bullets, meteorits, spawn_timer, spawn_interval, score, lives, font, paused, music, running

pygame.init()

clock = pygame.time.Clock()

# Папка, где лежит сам скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Папка с ассетами
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

#ширина окна
WIDTH = 800
#высота окна
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
#название игры
pygame.display.set_caption("Леталки!")


#широта корабля
confines_width = 800
#высота корабля
confines_height = 500
#широта положения корабля
confines_x = WIDTH
#высота положения корабля
confines_y = HEIGHT // 2

#широта корабля
spaceship_width = 110
#высота корабля
spaceship_height = 100
#широта положения корабля
spaceship_x = WIDTH - 790
#высота положения корабля
spaceship_y = HEIGHT - spaceship_height - 30
#скорость корабля
spaceship_speed = 8

#широта метеорита
meteorit_x = WIDTH - 30
#высота метеорита
meteorit_y = HEIGHT
#радиус метеорита
meteorit_radius = 15 * 4
#скорость метеорита
meteorit_speed = 5

#радиус снаряда
bullet_radius = 25
#скорость снаряда
bullet_speed = 7

bullets = []
meteorits = []
spawn_timer = 0
# Интервал между появлением метеоритов в миллисекундах
spawn_interval = 80  

#cчет
score = 0
#жизни
lives = 3

font = pygame.font.Font(os.path.join(ASSETS_DIR, "pixelmplusbold.ttf"), 14)
game_over = pygame.font.Font(os.path.join(ASSETS_DIR, "pixelmplusbold.ttf"), 27)

paused = False
music = False
running = False
initial_window = True


start_background_image = pygame.image.load(os.path.join(ASSETS_DIR, "start_background.jpg")).convert()
start_background_image = pygame.transform.scale(start_background_image, (WIDTH, HEIGHT))

background_image = pygame.image.load(os.path.join(ASSETS_DIR, "background.png")).convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

over_background_image = pygame.image.load(os.path.join(ASSETS_DIR, "over_background.jpg")).convert()
over_background_image = pygame.transform.scale(over_background_image, (WIDTH, HEIGHT))

spaceship_image = pygame.image.load(os.path.join(ASSETS_DIR, "spaceship.png")).convert_alpha()
spaceship_image = pygame.transform.scale(spaceship_image, (spaceship_width, spaceship_height))

meteorit_image = pygame.image.load(os.path.join(ASSETS_DIR, "meteorit.png")).convert_alpha()
meteorit_image = pygame.transform.scale(meteorit_image, (meteorit_radius, meteorit_radius))

bullet_image = pygame.image.load(os.path.join(ASSETS_DIR, "bullet.png")).convert_alpha()
bullet_image = pygame.transform.scale(bullet_image, (bullet_radius, bullet_radius))

pygame.mixer.music.load(os.path.join(ASSETS_DIR, "main_track.mp3"))
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

while initial_window:
    screen.blit(start_background_image, (0, 0))
    
    opening_text = game_over.render(f"R - для начала игры", True, (255,242,97))
    opening_text_rect = opening_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(opening_text, opening_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                initial_window = False
                running = True

    pygame.display.flip()

while running:
    music = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                bullets.append({"x": spaceship_x + spaceship_width, "y": spaceship_y + (spaceship_height // 2)})
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused
            if event.key == pygame.K_c:
                music = not music
                if music:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                
    if not paused:
        keys = pygame.key.get_pressed()
        
        # Логика передвижения корабля
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            spaceship_y -= spaceship_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            spaceship_y += spaceship_speed
            
            
        if spaceship_y < spaceship_height / 2:
            spaceship_y = spaceship_height / 2
        if spaceship_y > HEIGHT - spaceship_height:
            spaceship_y = HEIGHT - spaceship_height

        # Логика метеоритов
        spawn_timer += 1

        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            meteorit_y = random.randint(150, 600)
            meteorits.append({"x": meteorit_x + 80, "y": meteorit_y})


        for meteorit in meteorits:
            meteorit["x"] -= meteorit_speed

        for bullet in bullets:
            bullet["x"] += bullet_speed
            
        bullets = [b for b in bullets if b["x"] < WIDTH]
        
        spaceship_rect = pygame.Rect(spaceship_x, spaceship_y, spaceship_width, spaceship_height)

        remaining_meteorits = []

        for meteorit in meteorits:
            # Флаг на столкновение
            hit = False
            
            meteorit_rect = pygame.Rect(meteorit["x"] - meteorit_radius, meteorit["y"] - meteorit_radius, meteorit_radius * 2, meteorit_radius * 2)

            if spaceship_rect.colliderect(meteorit_rect):
                lives -= 1
                hit = True

            for bullet in bullets:
                bullet_rect = pygame.Rect(bullet["x"] - bullet_radius // 2, bullet["y"] - bullet_radius // 2, bullet_radius, bullet_radius)
                
                if bullet_rect.colliderect(meteorit_rect):
                    hit = True
                    score += 1
                    if bullet in bullets:
                        bullets.remove(bullet)
                    break
                
            if not hit:
                remaining_meteorits.append(meteorit)


        meteorits = remaining_meteorits

    screen.blit(background_image, (0, 0))

    for meteorit in meteorits:
        screen.blit(meteorit_image, (meteorit["x"] - meteorit_radius, meteorit["y"] - meteorit_radius))
        
    for bullet in bullets:
        screen.blit(bullet_image, (bullet["x"] - bullet_radius // 2, bullet["y"] - bullet_radius // 2))
        
    screen.blit(spaceship_image, (spaceship_x, spaceship_y))
    
    #Счет
    score_text = font.render(f"Метеоритов отбито: {score}", True, (255, 255, 255))
    
    #Жизни
    lives_text = font.render(f"Полная поломка через: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (25, 25))
    screen.blit(lives_text, (WIDTH - 300, 25))

    if paused:
        paused_text = font.render("Пауза!", True, (255, 255, 255))
        control_text = font.render("WS - управление, E - выстрел, TAB - пауза/продолжить, C - включить/выключить музыку", True, (255, 255, 255))
        pause_rect = paused_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        control_rect = control_text.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(paused_text, pause_rect)
        screen.blit(control_text, control_rect)

    pygame.display.flip()

    #фпс
    clock.tick(60)

    #если жизней меньше или равно нулю = экран проигрыша
    if lives <= 0:
        running = False

pygame.mixer.music.stop()

game_over_text = game_over.render("Игра окончена!", True, (255, 255, 255))
game_over_X = game_over.render("Нажмите X, чтобы закрыть игру.", True, (255, 255, 255))

showing_game_over = True

#пока показывает экран проигрыша
while showing_game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                showing_game_over = False
        elif event.type == pygame.QUIT:
            if event.type == pygame.QUIT:
                showing_game_over = False

    screen.blit(over_background_image, (0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    screen.blit(game_over_X, (WIDTH // 2 - game_over_X.get_width() // 2, HEIGHT - game_over_X.get_height() // 2 - 30))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


#TODO:
# 1. Начальный экран
# 2. окно проигрыша/завершение игры
# 3. добавить комментарии