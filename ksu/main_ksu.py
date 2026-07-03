

# Опишите базовый класс `Shape` с методом `area()`, который возвращает 0. От него унаследуйте классы `Rectangle` (хранит ширину и высоту),
#  `Circle` (хранит радиус) и `Triangle` (хранит основание и высоту). Каждый дочерний класс должен переопределить метод `area()` и считать свою площадь.

# Напишите функцию `total_area(shapes)`, которая принимает список фигур и возвращает сумму их площадей.

# Пример:

# ```python
# shapes = [
#     Rectangle(3, 4),
#     Circle(5),
#     Triangle(6, 4),
# ]
# print(total_area(shapes))
# ```

import math

class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius **2 )
    
class Triangle(Shape):
    def __init__(self, hight, base):
        self.hight = hight
        self.base = base

    def area(self):
        return (self.hight * self.base) / 2
    

shapes = [
    Rectangle(3, 4),
    Circle(5),
    Triangle(6, 4),
]

def total_area(shapes):
    summ = 0
    for figure in shapes:
        summ += figure.area()

    return summ


print(total_area(shapes))
        
        
        

