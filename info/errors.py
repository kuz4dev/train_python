# 1. Что такое исключения
# В Python ошибки не прерывают программу мгновенно, а сигнализируются через исключения (exceptions). 
# Это специальный код, который выполняется, когда происходит ошибка 
# (например, деление на ноль или обращение к несуществующему элементу списка).

# 2. Базовая конструкция: try и except
# Чтобы программа не завершалась аварийно, потенциально опасный код помещают в блок try, а обработку ошибки — в блок except.

#     try: Здесь размещается код, который может вызвать ошибку.
#     except: Если в блоке try возникает ошибка, управление передается сюда. Если ошибок нет, этот блок пропускается.

# Пример:

# short_list = [1, 2, 3, 5, 6]

# try:
#     short_list[10]  # Код, который может вызвать ошибку
# except:
#     print('Произошла ошибка')  # Обработка

# 3. Обработка конкретных типов ошибок
# Хотя можно использовать общий except без аргументов (ловит всё), лучше указывать конкретный тип исключения. Это делает обработку более точной.

#     Можно использовать несколько блоков except для разных ошибок.
#     Чтобы получить детали ошибки, используют конструкцию as:

# try:
#     short_list[10]  # Код, который может вызвать ошибку
#     # print(10 / 0)
# except IndexError as err:
#     print('Плохой индекс:', err)
# except Exception as other:
#     print('Что-то другое сломалось:')

# 4. Создание собственных исключений
# Вы можете определять свои типы исключений для особых ситуаций в программе. 
# Любое исключение — это класс, который должен быть потомком класса Exception.
# Пример создания и вызова:

# class UppercaseException(Exception):
#     pass

# # Где-то в коде
# if word.isupper():
#     raise UppercaseException(word)  # Генерация исключения

# # Также можно поймать свое исключение:

# try:
#     raise OopsException('panic')
# except OopsException as exc:
#     print(exc)

# 5. Журналирование ошибок (Logging)
# Вместо простого вывода ошибок через print(), в профессиональной разработке рекомендуется использовать модуль logging. 
# Это позволяет записывать сообщения об ошибках в файл или журнал с указанием времени, уровня важности и номера строки.
# Уровни приоритета сообщений:

#     debug(), info() — отладочная информация.
#     warn(), error(), critical() — предупреждения и ошибки.

# Пример настройки:

# import logging

# logging.basicConfig(level='DEBUG', filename='error.log')
# logger = logging.getLogger('my_app')
# logger.error('Произошла ошибка')  # Запись в журнал

# Главное правило!!!
# Не стоит замалчивать ошибки. 
# Если исключение возникло, его нужно либо корректно обработать, 
# чтобы программа могла продолжить работу, 
# либо зафиксировать в журнале для последующего анализа.

import logging
from datetime import datetime

short_list = [1, 2, 3, 5, 6]

# Настройка логгирования
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s', filename='error.log')

try:
    x = 10
    y = 0
    # result = x / y

    short_list[10]
except ZeroDivisionError as error:
    logging.error(f'Произошло деление на ноль, ошибка: {error}, время: {datetime.now()}')
except IndexError as error:
    logging.error(f'Такого индекса нет, ошибка: {error}, время: {datetime.now()}')


import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt, filename='blue_ox.log')

logger = logging.getLogger('bunyan')
logger.error("Где моя другая клетчатая рубашка?")