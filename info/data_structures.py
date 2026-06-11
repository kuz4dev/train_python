#  Структуры данных в Python
#  Темы: Списки · Кортежи · Словари · Множества

# Раздел 1: Списки (list)

# Список — упорядоченная изменяемая последовательность объектов любого типа.
# Создаётся через [] или list().
# Элементы нумеруются с 0. Отрицательные индексы — с конца (-1 = последний).
#
# Основные операции:
#   список[i]           — получить элемент по индексу
#   список[a:b]         — срез (от a включительно до b не включительно)
#   .append(x)          — добавить x в конец
#   .insert(i, x)       — вставить x в позицию i
#   .extend([...])      — объединить с другим списком
#   .remove(x)          — удалить первое вхождение x по значению
#   del список[i]       — удалить элемент по индексу
#   .pop()              — извлечь и вернуть последний элемент
#   .sort()             — сортировка на месте
#   .index(x)           — найти позицию значения x
#   .count(x)           — посчитать вхождения x
#   len(список)         — длина списка
#   x in список         — проверка наличия (True/False)
# срез - список[начало:конец:шаг]
# список[::2]
# city = 'Moscow'
# chars = list(city)
# print(chars)


# city = ['Moscow', 'Saint Peterburg', 'Kolomna']
# city.append('Kaliningrad')
# city.insert(2, 'Kaliningrad')
# city.remove('Kaliningrad')

# print('Kaliningrad' in city)

# print(city[0])
# print(city[0:2])
# print(city)

# number = [1, 10, 5, 7, 43, 48294]
# number.sort()
# print(len(number))

#--------------------------------------------------------------------------

# Раздел 2: Кортежи (tuple) топл
#
# Кортеж — неизменяемая последовательность. После создания нельзя добавить,
# удалить или изменить элементы — Python выбросит TypeError.
#
# Когда использовать кортеж:
#   • Данные не должны меняться (координаты, цвета RGB, константы)
#   • Нужен ключ для словаря (список ключом быть не может)
#   • Обмен переменных без временной переменной
#   • Распаковка нескольких значений за один раз
#
# Синтаксис:
#   t = ()                          — пустой кортеж
#   t = (42,)                       — кортеж из одного элемента (запятая обязательна!)
#   t = (1, 2, 3)                   — кортеж из трёх элементов
#   a, b, c = t                     — распаковка

# ksu = ('Ksenia', 'Samoshkina', 2010)
# name_k, surname_k, year_k = ksu
# print(name_k, surname_k, year_k)

# print(f"Имя - {name_k}, Фамилия - {surname_k}, Год рождения - {year_k}")

# sophi = ("Sophia", "Samoshckina", 2012)
# name_s, lastname, year = sophi
# print (name_s, lastname, year)

# print(f"Имя - {name_s}, Фамилия - {lastname}, Год рождения - {year}")

# Распаковка — каждому элементу сопоставляется переменная
# a, b, c = marx_tuple
# print(f"a={a}, b={b}, c={c}")

# Обмен значений через кортеж (без временной переменной!)
# print(f"До обмена: Имя={name_s}, Фамилия={lastname}")
# name_s, lastname = lastname, name_s
# print(f"После обмена: Имя={name_s}, Фамилия={lastname}")


# МЕТОД 1: count()
# Подсчитывает количество вхождений элемента

# numbers = (1, 1, 1, 1, 1, 2, 3, 4, 5, 6)
# print(numbers.count(1))
# print(numbers.count(6))

# print(numbers.index(1))
# print(numbers.index(4))

# marx = ('Groucho', 'Chico', 'Harpo', 'Chico', 'Chico')
# print(marx.count('Chico'))  # 3
# print(marx.count('Harpo'))  # 1
# print(marx.count('Zeppo'))  # 0


# # МЕТОД 2: index()
# # Возвращает индекс первого вхождения элемента

# marx = ('Groucho', 'Chico', 'Harpo', 'Chico')
# print(marx.index('Chico'))   # 1
# print(marx.index('Harpo'))   # 2
# print(marx.index('Groucho')) # 0

# # С указанием диапазона поиска
# colors = ('red', 'green', 'blue', 'red', 'yellow')
# print(colors.index('red'))      # 0 — первое вхождение
# print(colors.index('red', 1))   # 3 — ищем начиная с индекса 1


# Принимает список чисел, возвращает список кортежей (число, квадрат)
# Имя функции - squares_list, аргумент - numbers

# Ввод:  [1, 2, 3, 4, 5]
# Вывод: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#-----------------------------------------------
# Словари (dict)
# Словарь — изменяемая коллекция пар «ключ: значение».
# Создание
# something = {'Chapman': 'Graham', 'Cleese': 'John'}
# d = {}  # пустой словарь
# Ключи и значения

# something = {'Chapman': 'Graham', 'Cleese': 'John'}

# something['Sophi'] = 'Samoshkina'
# something['Ksusha'] = 'Samoshkina'

# Ключи — уникальны, должны быть неизменяемыми (строки, числа, кортежи)
# Значения — любые объекты

# Основные операции
# something['Cleese']          # получить значение (KeyError если нет)
# d.get('key', default) # безопасно, без ошибки
# d['key'] = value     # добавить / изменить
# del d['key']         # удалить
# 'key' in d           # проверить наличие

# d.update(d2)         # слить два словаря
# Итерирование
# something.keys()    # все ключи
# d.values()  # все значения
# d.items()   # пары (ключ, значение)

# kortez = (6, "a")

# list_numbers = [3, 18, 1799]

# dictionary = { "name": "Sophi", "age": 14 }
# print(dictionary["name"])
# print(dictionary.get("surname"))

# dictionary["name"] = 'Ksenia'
# print(dictionary["name"])
# dictionary["age"] = 21
# print(dictionary["age"])

# dictionary['age'] = 16
# print(dictionary["age"])

# dictionary['surname'] = 'Samoschkina'

# grades = {'name': 'Ksu', 'grade': 'University'}

# something.keys()    # все ключи
# d.values()  # все значения
# d.items()   # пары (ключ, значение)
# for grade in grades.values():
#     print(grade)
# Словарные включения
# pythonf2e = {v: k for k, v in e2f.items()}  # обратный словарь
# Вложенные словари
# pythonlife = {
#     'animals': {
#         'cats': ['Henri', 'Grumpy'],
#     }
# }
# life['animals']['cats'][0]  # → 'Henri'
# Практический паттерн — подсчёт частоты
# pythonfreq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# Ключевые отличия от списка: нет порядка по индексу — доступ по ключу. 

#----------------------------------------------------------------------------------

# Множества (set)
#
# Множество — изменяемая коллекция УНИКАЛЬНЫХ значений.
# Порядок не гарантирован. Дублирующиеся значения автоматически отбрасываются.
#
# СОЗДАНИЕ:
#   s = {1, 2, 3}           — через фигурные скобки (НЕ пустое!)
#   s = set()               — пустое множество (не {} — это пустой словарь!)
#   s = set([1, 2, 2, 3])   — из списка (дубликаты убираются)
#   s = set('hello')        — из строки → {'h', 'e', 'l', 'o'}
#   s = {x for x in range(5)} — генератор множества (set comprehension)

# TODO: Создайте множество квадратов ЧЁТНЫХ чисел из списка

# number_set = { 1, 1, 1, 1, 1, 2, 3, 3 } # { 1, 2, 3 }

# unique_set = set(number_set) # { 1, 2, 3 }

#
# ДОБАВЛЕНИЕ И УДАЛЕНИЕ:
#   s.add(x)        — добавить элемент x
#   s.remove(x)     — удалить x (KeyError если нет!)
#   s.discard(x)    — удалить x (молча, если нет)
#   s.pop()         — извлечь случайный элемент
#   s.clear()       — очистить множество
#
# ПРОВЕРКИ:
#   x in s          — x есть в множестве? (очень быстро — O(1))
#   x not in s      — x отсутствует?
#   len(s)          — количество элементов
#   a == b          — одинаковые ли множества?
#   a.issubset(b)   — a ⊆ b  (a является подмножеством b)?
#   a <= b          — то же самое через оператор
#   a.issuperset(b) — a ⊇ b  (a содержит всё из b)?
#   a >= b          — то же самое через оператор
#   a.isdisjoint(b) — нет ни одного общего элемента?
#
# ОПЕРАЦИИ НАД МНОЖЕСТВАМИ:
#   a & b           — пересечение: {x: x in a and x in b}
#   a | b           — объединение: {x: x in a or x in b}
#   a - b           — разность: {x: x in a and x not in b}
#   a ^ b           — симметричная разность: {x: только в одном из них}
#
# FROZENSET — неизменяемое множество:
#   fs = frozenset([1, 2, 3])  — нельзя добавить / удалить
#   можно использовать как ключ словаря или элемент другого множества

s1 = { 3, 1, 4, 1, 5, 9, 2, 6, 5 }

print({x for x in range(5)})

fruits = set(['яблоко', 'банан', 'яблоко', 'груша', 'банан'])

print(fruits)

letters = set('mississippi')

