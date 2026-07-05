import pygame
import random

pygame.init()

clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Нууу, погоди!")

wolf_width = 70
wolf_height = 100
wolf_x = WIDTH // 2 - wolf_width // 2
wolf_y = HEIGHT - wolf_height - 30
wolf_speed = 7

egg_x = WIDTH // 2
egg_y = 50
egg_radius = 15
egg_speed = 5

eggs = []
spawn_timer = 0
spawn_interval = 60  # Интервал между появлением яиц в миллисекундах

score = 0
lives = 3


font = pygame.font.SysFont(None, 40)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    
    wolf_rect = pygame.Rect(wolf_x, wolf_y, wolf_width, wolf_height)
    
    remaining_eggs = []

    for egg in eggs:
        egg_rect = pygame.Rect(egg["x"] - egg_radius, egg["y"] - egg_radius, egg_radius * 2, egg_radius * 2)

        if wolf_rect.colliderect(egg_rect):
            score += 1
        elif egg["y"] - egg_radius > HEIGHT:
            lives -= 1
        else:
            remaining_eggs.append(egg)

    eggs = remaining_eggs

    screen.fill((130, 206, 190))

    for egg in eggs:
        pygame.draw.circle(screen, (255, 255, 255), (egg["x"], egg["y"]), egg_radius)
    pygame.draw.rect(screen, (0, 0, 0), (wolf_x, wolf_y, wolf_width, wolf_height))

    # Отображение счета очков и жизней
    score_text = font.render(f"Яиц поймано: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Жизней осталось: {lives}", True, (0, 0, 0))
    screen.blit(score_text, (25, 25))
    screen.blit(lives_text, (WIDTH - 300, 25))

    pygame.display.flip()

    clock.tick(60)

    if lives <= 0:
        running = False

game_over_text = font.render("Игра окончена!", True, (0, 0, 0))

showing_game_over = True
while showing_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((130, 206, 190))
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

