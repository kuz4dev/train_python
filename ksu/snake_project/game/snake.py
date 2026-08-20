from game import config as cfg
import pygame

class Snake:
    def __init__(self):
        self.position = cfg.snake_position
        self.body = cfg.snake_body
        self.direction = cfg.direction
        
    # меняем направление движения змейки
    def change_direction(self, new_direction):
        opposite_directions = {
            'UP': 'DOWN',
            'DOWN': 'UP',
            'LEFT': 'RIGHT',
            'RIGHT': 'LEFT'
        }
        
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    # добавление новой части тела змейки и удаление хвоста, если змейка не ест
    # def update_body(self, grow):
        
    # проверка столкновений с границами и самим собой True - столкновение, False - нет
    def check_collision(self):
        return (self.position[0] == cfg.FIELD_RIGHT - cfg.BLOCK and 
            self.direction == "RIGHT") or (self.position[0] == cfg.FIELD_LEFT and 
            self.direction == "LEFT") or (self.position[1] == cfg.FIELD_UP and 
            self.direction == "UP") or (self.position[1] == cfg.FIELD_DOWN - cfg.BLOCK and 
            self.direction == "DOWN")
            
    def self_collision(self):
        return self.position in self.body[1:]
        
    # отрисовка змейки на экране    
    def draw(self, screen):
        
# snake.update_body(True)

# if not paused:

#     #изменение направления змейки
#     if event.key == pygame.K_w:
#         snake.change_direction('UP')
#     elif event.key == pygame.K_s:
#         snake.change_direction('DOWN')
#     elif event.key == pygame.K_a:
#         snake.change_direction('LEFT')
#     elif event.key == pygame.K_d:
#         snake.change_direction('RIGHT')
        