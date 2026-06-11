# add(a, b) — возвращает сумму
# subtract(a, b) — возвращает разность
# multiply(a, b) — возвращает произведение
# divide(a, b) — возвращает результат деления (если b == 0, возвращает строку 'Ошибка: деление на ноль')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    if b == 0:
        return 'Ошибка: деление на ноль'