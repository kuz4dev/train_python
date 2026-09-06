import pygame
import random
import os

from configuration import (
    ASSETS_DIR, WIDTH, HEIGHT, screen, clock, score, lives,
    spaceship_width, spaceship_height, spaceship_x, spaceship_y, spaceship_speed,
    meteorit_x, meteorit_y, meteorit_radius, meteorit_speed, meteorits, spawn_timer, spawn_interval,
    bullet_radius, bullet_speed, bullets,
    paused, music, running, initial_window, showing_game_over,
)

from game import (
    initial_screen,
    gameover_screen,
)

pygame.init()

#название игры
pygame.display.set_caption("Леталки!")

#шрифты
font = pygame.font.Font(os.path.join(ASSETS_DIR, "pixelmplusbold.ttf"), 16)
game_over = pygame.font.Font(os.path.join(ASSETS_DIR, "pixelmplusbold.ttf"), 25)

#начальный задний фон
start_background_image = pygame.image.load(os.path.join(ASSETS_DIR, "start_background.jpg")).convert()
start_background_image = pygame.transform.scale(start_background_image, (WIDTH, HEIGHT))

#во время игры задний фон
background_image = pygame.image.load(os.path.join(ASSETS_DIR, "background.png")).convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#конечный задний фон
over_background_image = pygame.image.load(os.path.join(ASSETS_DIR, "over_background.jpg")).convert()
over_background_image = pygame.transform.scale(over_background_image, (WIDTH, HEIGHT))

#корабль
spaceship_image = pygame.image.load(os.path.join(ASSETS_DIR, "spaceship.png")).convert_alpha()
spaceship_image = pygame.transform.scale(spaceship_image, (spaceship_width, spaceship_height))

#метеорит
meteorit_image = pygame.image.load(os.path.join(ASSETS_DIR, "meteorit.png")).convert_alpha()
meteorit_image = pygame.transform.scale(meteorit_image, (meteorit_radius, meteorit_radius))

#пуля
bullet_image = pygame.image.load(os.path.join(ASSETS_DIR, "bullet.png")).convert_alpha()
bullet_image = pygame.transform.scale(bullet_image, (bullet_radius, bullet_radius))


running = initial_screen(screen, game_over, start_background_image, initial_window)

while running:
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
        
        #Передвижение корабля
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            spaceship_y -= spaceship_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            spaceship_y += spaceship_speed
        
        #ограничение корабля
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
            #столкновение
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

    #вывод метеоритов
    for meteorit in meteorits:
        screen.blit(meteorit_image, (meteorit["x"] - meteorit_radius, meteorit["y"] - meteorit_radius))
        
    #вывод пуль
    for bullet in bullets:
        screen.blit(bullet_image, (bullet["x"] - bullet_radius // 2, bullet["y"] - bullet_radius // 2))
        
    screen.blit(spaceship_image, (spaceship_x, spaceship_y))
    
    #Счет
    score_text = font.render(f"Метеоритов отбито: {score}", True, (255, 255, 255))
    #Жизни
    lives_text = font.render(f"Полная поломка через: {lives}", True, (255, 255, 255))
    #вывод текстов
    screen.blit(score_text, (25, 25))
    screen.blit(lives_text, (WIDTH - 360, 25))

    #пауза
    if paused:
        #текст
        paused_text = font.render("Пауза!", True, (255, 255, 255))
        control_text = font.render("WS - управление, E - выстрел", True, (255, 255, 255))
        control_text2 = font.render("TAB - пауза/продолжить, C - включить/выключить музыку", True, (255, 255, 255))

        #расположение текста
        pause_rect = paused_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        control_rect = control_text.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 70))
        control_rect2 = control_text2.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 90))

        #вывод текста
        screen.blit(paused_text, pause_rect)
        screen.blit(control_text, control_rect)
        screen.blit(control_text2, control_rect2)

    pygame.display.flip()

    #фпс
    clock.tick(60)

    #если жизней меньше или равно нулю = экран проигрыша
    if lives <= 0:
        running = False
        showing_game_over = True

#выкл музыки
pygame.mixer.music.stop()
pygame.mixer.music.load(os.path.join(ASSETS_DIR, "over_track.mp3"))
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

gameover_screen(screen, game_over, over_background_image, showing_game_over)

pygame.display.flip()

pygame.quit()


#TODO:
# 1. добавить комментарии