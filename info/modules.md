# Модули, пакеты и программы

## 1. Отдельные программы

До сих пор мы писали код в интерактивном интерпретаторе. Теперь переходим к **отдельным программам** — файлам `.py`, которые запускаются из терминала.

Создайте файл `test1.py`:

```python
print("Эта программа работает!")
```

Запустите:

```
$ python test1.py
Эта программа работает!
```

---

## 2. Аргументы командной строки

Модуль `sys` даёт доступ к аргументам, переданным при запуске скрипта, через список `sys.argv`.

- `sys.argv[0]` — имя самого скрипта
- `sys.argv[1]`, `sys.argv[2]`, ... — переданные аргументы (всегда строки)

```python
# файл: test2.py
import sys
print('Аргументы программы:', sys.argv)
```

```
$ python test2.py
Аргументы программы: ['test2.py']

$ python test2.py привет мир
Аргументы программы: ['test2.py', 'привет', 'мир']
```

---

## 3. Модули и оператор import

**Модуль** — это файл `.py`, содержащий код Python. Мы ссылаемся на код других модулей с помощью оператора `import`.

### 3.1. Импорт модуля целиком

```python
import report
description = report.get_description()
print("Прогноз погоды:", description)
```

Здесь `report` — это файл `report.py`, лежащий рядом. Все его функции доступны через префикс `report.`.

Файл `report.py`:

```python
from random import choice

def get_description():
    """Возвращает случайный прогноз погоды"""
    weather = ['дождь', 'снег', 'туман', 'солнце', 'кто знает']
    return choice(weather)
```

### 3.2. Импорт с псевдонимом (as)

Если имя модуля длинное или конфликтует с другим — дайте ему псевдоним:

```python
import report as wr
description = wr.get_description()
print("Прогноз погоды:", description)
```

### 3.3. Импорт конкретной функции

Можно импортировать только нужную функцию — тогда префикс модуля не нужен:

```python
from report import get_description
description = get_description()
print("Прогноз погоды:", description)
```

### 3.4. Импорт функции с псевдонимом

```python
from report import get_description as погода
print("Прогноз:", погода())
```

### 3.5. Где размещать import

Два варианта — оба работают:

- **В начале файла** — явно видны все зависимости (рекомендуемый стиль)
- **Внутри функции** — если импорт нужен только этой функции

```python
# Вариант 1: в начале файла
import random

def get_description():
    weather = ['дождь', 'снег', 'солнце']
    return random.choice(weather)

# Вариант 2: внутри функции
def get_description():
    from random import choice
    weather = ['дождь', 'снег', 'солнце']
    return choice(weather)
```

---

## 4. Каталоги поиска модулей

Python ищет модули по списку путей из `sys.path`:

```python
import sys
for path in sys.path:
    print(path)
```

Порядок поиска:
1. Текущий каталог (пустая строка `''` в `sys.path`)
2. Каталоги из переменной окружения `PYTHONPATH`
3. Каталоги стандартной библиотеки
4. Каталоги `site-packages` (pip-пакеты)

**Важно:** первый найденный модуль побеждает. Если вы создадите файл `random.py` в рабочем каталоге, Python найдёт его раньше стандартного `random` — и ваш код сломается.

---

## 5. Пакеты

**Пакет** — это папка с модулями, содержащая файл `__init__.py`.

Структура:

```
sources/                ← папка-пакет
    __init__.py         ← обязательный файл (может быть пустым)
    daily.py            ← модуль
    weekly.py           ← модуль
```

Файл `sources/daily.py`:

```python
def forecast():
    """Фиктивный прогноз на день"""
    return 'как вчера'
```

Файл `sources/weekly.py`:

```python
def forecast():
    """Фиктивный прогноз на неделю"""
    return ['снег', 'ещё снег', 'мокрый снег',
            'ледяной дождь', 'дождь', 'туман', 'град']
```

Основная программа `weather.py`:

```python
from sources import daily, weekly

print("Прогноз на день:", daily.forecast())
print("Прогноз на неделю:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
```

```
$ python weather.py
Прогноз на день: как вчера
Прогноз на неделю:
1 снег
2 ещё снег
3 мокрый снег
4 ледяной дождь
5 дождь
6 туман
7 град
```

Можно импортировать конкретную функцию из модуля внутри пакета:

```python
from sources.daily import forecast
print(forecast())
```

---

## 6. Стандартная библиотека Python

Python поставляется с большой стандартной библиотекой. Перед написанием своего кода всегда стоит проверить, есть ли готовое решение.

### 6.1. collections.Counter — подсчёт элементов

```python
from collections import Counter

breakfast = ['яйца', 'хлеб', 'яйца', 'сыр', 'хлеб', 'яйца']
count = Counter(breakfast)
print(count)            # Counter({'яйца': 3, 'хлеб': 2, 'сыр': 1})
print(count.most_common(1))  # [('яйца', 3)]
```

`Counter` работает с любым итерабельным объектом, включая строки:

```python
print(Counter('абракадабра'))
# Counter({'а': 5, 'б': 2, 'р': 2, 'к': 1, 'д': 1})
```

### 6.2. collections.defaultdict — словарь со значением по умолчанию

Обычный словарь выбрасывает `KeyError` при обращении к несуществующему ключу. `defaultdict` вместо этого создаёт значение по умолчанию.

Аргумент — фабричная функция: `list`, `int`, `str` и т.д.

```python
from collections import defaultdict

# Группировка элементов по категории
food = defaultdict(list)
food['фрукты'].append('яблоко')    # ключ создаётся автоматически
food['фрукты'].append('банан')
food['овощи'].append('морковь')

print(food)
# defaultdict(<class 'list'>, {'фрукты': ['яблоко', 'банан'], 'овощи': ['морковь']})
```

Без `defaultdict` пришлось бы писать так:

```python
food = {}
if 'фрукты' not in food:
    food['фрукты'] = []
food['фрукты'].append('яблоко')
```

### 6.3. collections.OrderedDict — словарь с порядком

Запоминает порядок, в котором были добавлены ключи (в Python 3.7+ обычный `dict` тоже сохраняет порядок, но `OrderedDict` делает это гарантированно и поддерживает методы вроде `move_to_end()`):

```python
from collections import OrderedDict

quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])
for name, quote in quotes.items():
    print(name, quote)
```

### 6.4. collections.deque — двусторонняя очередь

Добавление и удаление с обоих концов за O(1).

```python
from collections import deque

dq = deque('bcd')
dq.appendleft('a')     # добавить слева → deque(['a', 'b', 'c', 'd'])
dq.append('e')          # добавить справа → deque(['a', 'b', 'c', 'd', 'e'])
print(dq.popleft())     # удалить слева → 'a'
print(dq.pop())         # удалить справа → 'e'
```

Пример — проверка палиндрома через `deque`:

```python
def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('radar'))    # True
print(palindrome('halibut'))  # False
```

Проще можно: `word == word[::-1]`, но задача — показать работу `deque`.

### 6.5. itertools — функции для итераций

**chain** — объединяет несколько последовательностей в одну:

```python
import itertools

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
# 1, 2, a, b
```

**cycle** — бесконечный цикл по элементам:

```python
# Осторожно: бесконечный цикл!
for item in itertools.cycle([1, 2]):
    print(item)
# 1, 2, 1, 2, 1, 2, ...
```

**accumulate** — накопленные значения (по умолчанию — сумма):

```python
print(list(itertools.accumulate([1, 2, 3, 4])))
# [1, 3, 6, 10]
```

С пользовательской функцией (произведение):

```python
def multiply(a, b):
    return a * b

print(list(itertools.accumulate([1, 2, 3, 4], multiply)))
# [1, 2, 6, 24]
```

### 6.6. pprint — красивый вывод

```python
from pprint import pprint

data = {'Moe': 'A wise guy, huh?', 'Larry': 'Ow!', 'Curly': 'Nyuk nyuk!'}

print(data)     # всё в одну строку, трудно читать
pprint(data)    # каждый элемент на отдельной строке
```

---

## 7. Установка сторонних пакетов (pip)

Стандартной библиотеки иногда недостаточно. Сторонние пакеты устанавливаются через `pip`:

```
$ pip install flask              # последняя версия
$ pip install flask==0.9.0       # конкретная версия
$ pip install 'flask>=0.9.0'     # минимальная версия
$ pip install -r requirements.txt  # из файла требований
```

Где искать пакеты:
- [PyPI](https://pypi.org/) — главный репозиторий пакетов Python
- [GitHub](https://github.com/) — исходный код проектов

---

## Практика

### Задание 1

Создайте файл `zoo.py` с функцией `hours()`, которая выводит строку `'Открыто 9-17 ежедневно'`. Импортируйте модуль и вызовите функцию четырьмя способами:

```python
# Способ 1: import целиком
import zoo
zoo.hours()

# Способ 2: import с псевдонимом
import zoo as menagerie
menagerie.hours()

# Способ 3: выборочный import
from zoo import hours
hours()

# Способ 4: выборочный import с псевдонимом
from zoo import hours as info
info()
```

### Задание 2

Создайте словарь `plain` с парами `'a': 1`, `'b': 2`, `'c': 3` и выведите его. Затем создайте `OrderedDict` с теми же парами.

```python
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)
```

### Задание 3

Создайте `defaultdict(list)` с именем `dict_of_lists`. Добавьте к ключу `'a'` значение `'something for a'` за одну операцию и выведите `dict_of_lists['a']`.

```python
from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
# ['something for a']
```

### Задание 4

Дан список покупок — кортежи `(категория, товар, цена)`. Сгруппируйте товары по категориям и посчитайте сумму в каждой.

```python
from collections import defaultdict

purchases = [
    ('еда', 'хлеб', 50),
    ('еда', 'молоко', 80),
    ('техника', 'наушники', 2500),
    ('еда', 'сыр', 350),
    ('техника', 'мышь', 1200),
    ('одежда', 'футболка', 900),
]

grouped = defaultdict(list)
for category, item, price in purchases:
    grouped[category].append((item, price))

for cat, items in grouped.items():
    total = sum(price for _, price in items)
    names = ', '.join(item for item, _ in items)
    print(f"{cat}: {total} руб. ({names})")
```

```
еда: 480 руб. (хлеб, молоко, сыр)
техника: 3700 руб. (наушники, мышь)
одежда: 900 руб. (футболка)
```

### Задание 5

Подсчитайте буквы в слове `'абракадабра'` с помощью `Counter` и выведите 3 самые частые.

```python
from collections import Counter

letters = Counter('абракадабра')
print(letters.most_common(3))
# [('а', 5), ('б', 2), ('р', 2)]
```

### Задание 6

Напишите функцию проверки палиндрома через `deque`. Проверьте слова: `'радар'`, `'шалаш'`, `'питон'`.

```python
from collections import deque

def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

for word in ['радар', 'шалаш', 'питон']:
    print(f"'{word}' — палиндром: {palindrome(word)}")
```

```
'радар' — палиндром: True
'шалаш' — палиндром: True
'питон' — палиндром: False
```

### Задание 7

С помощью `itertools.chain` объедините три списка `[1, 2]`, `[3, 4]`, `[5, 6]`. С помощью `itertools.accumulate` посчитайте накопленную сумму `[10, 20, 30, 40]`.

```python
import itertools

print(list(itertools.chain([1, 2], [3, 4], [5, 6])))
# [1, 2, 3, 4, 5, 6]

print(list(itertools.accumulate([10, 20, 30, 40])))
# [10, 30, 60, 100]
```
