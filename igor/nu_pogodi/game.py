import pygame
import random
import os

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Нууу, погоди!")

wolf_width = 100
wolf_height = 150
wolf_x = WIDTH // 2 - wolf_width // 2
wolf_y = HEIGHT - wolf_height - 30
wolf_speed = 7

# папки - пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

egg_x = WIDTH // 2
egg_y = 50
egg_radius = 15
egg_speed = 5

eggs = []
spawn_timer = 0
spawn_interval = 60  # Интервал между появлением яиц в миллисекундах

score = 0
lives = 3

speedup_timer = 0
speedup_interval = 300
speedup_amount = 0.5

font = pygame.font.SysFont(None, 40)
paused_font = pygame.font.SysFont(None, 80)

paused = False

running = True

background_image = pygame.image.load(os.path.join(ASSETS_DIR, "background.png")).convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

wolf_image = pygame.image.load(os.path.join(ASSETS_DIR, "wolf.png")).convert_alpha()
wolf_image = pygame.transform.scale(wolf_image, (wolf_width, wolf_height))

egg_image = pygame.image.load(os.path.join(ASSETS_DIR, "egg.png")).convert_alpha()
egg_image = pygame.transform.scale(egg_image, (egg_radius * 2, egg_radius * 2))


catch_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "catch.wav"))
miss_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "miss.wav"))

pygame.mixer.music.load(os.path.join(ASSETS_DIR, "music.mp3"))
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
            wolf_x -= wolf_speed
        if keys[pygame.K_RIGHT]:
            wolf_x += wolf_speed

        if wolf_x < 0:
            wolf_x = 0
        if wolf_x > WIDTH - wolf_width:
            wolf_x = WIDTH - wolf_width


        # Логика яйца
        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            egg_x = random.randint(egg_radius, WIDTH - egg_radius)
            eggs.append({"x": egg_x, "y": -egg_radius})


        for egg in eggs:
            egg["y"] += egg_speed

        basket_width = 60
        basket_height = 20
        basket_x = wolf_x + (wolf_width - basket_width) // 2
        
        basket_rect = pygame.Rect(basket_x, wolf_y, basket_width, basket_height)
        
        remaining_eggs = []

        for egg in eggs:
            egg_rect = pygame.Rect(egg["x"] - egg_radius, egg["y"] - egg_radius, egg_radius * 2, egg_radius * 2)

            if basket_rect.colliderect(egg_rect):
                score += 1
                catch_sound.play()
            elif egg["y"] - egg_radius > HEIGHT:
                lives -= 1
                miss_sound.play()
            else:
                remaining_eggs.append(egg)

        eggs = remaining_eggs

        speedup_timer += 1

        if speedup_timer >= speedup_interval:
            speedup_timer = 0
            egg_speed += speedup_amount

    
    screen.blit(background_image, (0, 0))

    for egg in eggs:
        screen.blit(egg_image, (egg["x"] - egg_radius, egg["y"] - egg_radius))

    screen.blit(wolf_image, (wolf_x, wolf_y))

    # Отображение счета очков и жизней
    score_text = font.render(f"Яиц поймано: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Жизней осталось: {lives}", True, (0, 0, 0))
    screen.blit(score_text, (25, 25))
    screen.blit(lives_text, (WIDTH - 300, 25))

    if paused:
        paused_text = font.render("Пауза!", True, (255, 255, 255))
        pause_rect = paused_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(paused_text, pause_rect)

    pygame.display.flip()

    clock.tick(60)

    if lives <= 0:
        running = False

pygame.mixer.music.stop()

game_over_text = font.render("Игра окончена!", True, (0, 0, 0))

showing_game_over = True
while showing_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
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

