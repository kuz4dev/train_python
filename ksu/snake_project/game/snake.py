from game import config as cfg
import pygame

class Snake:
    def __init__(self):
        self.position = cfg.snake_position
        self.body = cfg.snake_body
        self.direction = "RIGHT"
        
    def set_position(self, new_position):
        self.position = new_position
        
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
    def update_body(self):
        self.body.insert(0, list(self.position))
        
        ate = False

        #проверка на столкновение с едой
        for food in cfg.current_food:
            if food == self.position:
                cfg.current_food.remove(food)
                ate = True
                cfg.score += 5000
                break
        
        #удаление хвоста
        if not ate:
            self.body.pop()

    # проверка столкновений с границами и самим собой True - столкновение, False - нет
    def check_collision_border(self):
        return (self.position[0] == cfg.FIELD_RIGHT - cfg.BLOCK and 
            self.direction == "RIGHT") or (self.position[0] == cfg.FIELD_LEFT and 
            self.direction == "LEFT") or (self.position[1] == cfg.FIELD_UP and 
            self.direction == "UP") or (self.position[1] == cfg.FIELD_DOWN - cfg.BLOCK and 
            self.direction == "DOWN")
            
    def self_collision(self):
        return self.position in self.body[1:]

    def draw_body(self, screen):
        for one in self.body:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(one[0], one[1], cfg.BLOCK, cfg.BLOCK))

    def get_boost(self):
        # врезание в змейку и ускорение-возвращение
        for boost in cfg.current_boost:
            if boost == self.position:
                cfg.current_boost.remove(boost)
                cfg.speed += cfg.SPEED_BOOST

                cfg.boost_end_time = pygame.time.get_ticks() + 10000
                break
    
        