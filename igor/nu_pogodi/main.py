import pygame
import random
import os

from game import config

from game.wolf import Wolf

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Нууу, погоди!")

font = pygame.font.SysFont(None, 40)
paused_font = pygame.font.SysFont(None, 80)

paused = False

running = True

wolf = Wolf()

background_image = pygame.image.load(os.path.join(config.ASSETS_DIR_IMG, "background.png")).convert()
background_image = pygame.transform.scale(background_image, (config.WIDTH, config.HEIGHT))

wolf_image = pygame.image.load(os.path.join(config.ASSETS_DIR_IMG, "wolf.png")).convert_alpha()
wolf_image = pygame.transform.scale(wolf_image, (config.wolf_width, config.wolf_height))

egg_image = pygame.image.load(os.path.join(config.ASSETS_DIR_IMG, "egg.png")).convert_alpha()
egg_image = pygame.transform.scale(egg_image, (config.egg_radius * 2, config.egg_radius * 2))


catch_sound = pygame.mixer.Sound(os.path.join(config.ASSETS_DIR_SOUNDS, "catch.wav"))
miss_sound = pygame.mixer.Sound(os.path.join(config.ASSETS_DIR_SOUNDS, "miss.wav"))

pygame.mixer.music.load(os.path.join(config.ASSETS_DIR_SOUNDS, "music.mp3"))
pygame.mixer.music.play(-1)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

    if not paused:
        keys = pygame.key.get_pressed()

        # Логика передвижения волка
        if keys[pygame.K_LEFT]:
            wolf.x -= config.wolf_speed
        if keys[pygame.K_RIGHT]:
            wolf.x += config.wolf_speed

        if wolf.x < 0:
            wolf.x = 0
        if wolf.x > config.WIDTH - config.wolf_width:
            wolf.x = config.WIDTH - config.wolf_width


        # Логика яйца
        config.spawn_timer += 1
        if config.spawn_timer >= config.spawn_interval:
            config.spawn_timer = 0
            egg_x = random.randint(config.egg_radius, config.WIDTH - config.egg_radius)
            config.eggs.append({"x": egg_x, "y": -config.egg_radius})


        for egg in config.eggs:
            egg["y"] += config.egg_speed

        basket_x = config.wolf_x + (config.wolf_width - config.basket_width) // 2
        
        basket_rect = pygame.Rect(basket_x, config.wolf_y, config.basket_width, config.basket_height)
        
        remaining_eggs = []

        for egg in config.eggs:
            egg_rect = pygame.Rect(egg["x"] - config.egg_radius, egg["y"] - config.egg_radius, config.egg_radius * 2, config.egg_radius * 2)

            if basket_rect.colliderect(egg_rect):
                config.score += 1
                catch_sound.play()
            elif egg["y"] - config.egg_radius > config.HEIGHT:
                config.lives -= 1
                miss_sound.play()
            else:
                remaining_eggs.append(egg)

        config.eggs = remaining_eggs

        config.speedup_timer += 1

        if config.speedup_timer >= config.speedup_interval:
            config.speedup_timer = 0
            config.egg_speed += config.speedup_amount

    
    screen.blit(background_image, (0, 0))

    for egg in config.eggs:
        screen.blit(egg_image, (egg["x"] - config.egg_radius, egg["y"] - config.egg_radius))

    wolf.draw(screen, wolf_image)

    # Отображение счета очков и жизней
    score_text = font.render(f"Яиц поймано: {config.score}", True, (0, 0, 0))
    lives_text = font.render(f"Жизней осталось: {config.lives}", True, (0, 0, 0))
    screen.blit(score_text, (25, 25))
    screen.blit(lives_text, (config.WIDTH - 300, 25))

    if paused:
        paused_text = font.render("Пауза!", True, (255, 255, 255))
        pause_rect = paused_text.get_rect(center = (config.WIDTH // 2, config.HEIGHT // 2))
        screen.blit(paused_text, pause_rect)

    pygame.display.flip()

    clock.tick(60)

    if config.lives <= 0:
        running = False

pygame.mixer.music.stop()

game_over_text = font.render("Игра окончена!", True, (0, 0, 0))

showing_game_over = True
while showing_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))
    screen.blit(game_over_text, (config.WIDTH // 2 - 100, config.HEIGHT // 2 - 20))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


# Что доработать:
# Баг - ловим яйца только верхней гранью
# Фича - Поставить на паузу
# Фича - Добавить задний фон и картинки
# Фича - Добавить музыку и звуки
# Фича - Постепенное ускорение яиц
# Фича - Добавить бонусы (например, замедление яиц на 5 секунд)
# Фича - Сделать кнопку перехода к настройкам (менять сложность и так далее)

