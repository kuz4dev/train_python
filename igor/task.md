# Задачи на закрепление

Темы: структуры данных, файлы, функции, ООП.

---

## Задача 1. Словарь учениц и средний балл

В файле `grades.txt` каждая строка устроена так:

```
Анна: 5 4 5 3 4
Мария: 3 3 4 5 4
Полина: 5 5 5 5 5
Дарья: 2 3 3 4 3
```

Напишите программу, которая читает файл и выводит для каждой ученицы её средний балл, округлённый до двух знаков после запятой. В конце выведите имя ученицы с самым высоким средним.

Пример вывода:

```
Анна: 4.20
Мария: 3.80
Полина: 5.00
Дарья: 3.00
Лучший результат: Полина
```

### Решение

```python
results = {}  # имя -> средний балл

with open("grades.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        name, grades_part = line.split(":")
        grades_strings = grades_part.split()

        total = 0
        count = 0
        for grade in grades_strings:
            total = total + int(grade)
            count = count + 1

        average = total / count
        results[name] = average

# выводим всех
for name in results:
    print(f"{name}: {results[name]:.2f}")

# ищем лучший результат через явный цикл
best_name = ""
best_score = -1
for name in results:
    if results[name] > best_score:
        best_score = results[name]
        best_name = name

print(f"Лучший результат: {best_name}")
```

---

## Задача 2. Функция-фильтр уникальных слов

Напишите функцию `unique_words(text)`, которая принимает строку и возвращает список уникальных слов в том порядке, в котором они впервые встретились. Регистр игнорируется (слова `Привет` и `привет` считаются одинаковыми), знаки препинания нужно отбросить.

Пример:

```python
text = "Кошка спит. Кошка ест. Собака спит!"
print(unique_words(text))
# ['кошка', 'спит', 'ест', 'собака']
```

### Решение

```python
def unique_words(text):
    # убираем знаки препинания, заменяя их на пробелы
    punctuation = ".,!?;:()-"
    cleaned = ""
    for char in text:
        if char in punctuation:
            cleaned = cleaned + " "
        else:
            cleaned = cleaned + char

    # приводим к нижнему регистру и режем на слова
    words = cleaned.lower().split()

    result = []
    for word in words:
        if word not in result:
            result.append(word)

    return result


text = "Кошка спит. Кошка ест. Собака спит!"
print(unique_words(text))
```

---

## Задача 3. Библиотека (ООП)

Опишите три класса: `Book`, `Reader` и `Library`.

**Book** хранит название, автора и признак того, выдана ли книга сейчас на руки (изначально — нет).

**Reader** хранит имя и список книг, которые он сейчас читает (изначально пустой).

**Library** хранит список всех книг и список всех читателей. У библиотеки есть методы:
- `add_book(book)` — добавить книгу
- `register_reader(reader)` — записать читателя
- `give_book(reader_name, book_title)` — выдать книгу читателю. Если книга уже на руках или её нет в библиотеке — вывести сообщение и ничего не делать
- `return_book(reader_name, book_title)` — принять книгу обратно
- `show_status()` — вывести список всех книг и для каждой указать, свободна она или у кого находится

Пример использования:

```python
lib = Library()
lib.add_book(Book("Гарри Поттер", "Дж. Роулинг"))
lib.add_book(Book("Война и мир", "Лев Толстой"))

lib.register_reader(Reader("Анна"))
lib.register_reader(Reader("Мария"))

lib.give_book("Анна", "Гарри Поттер")
lib.give_book("Мария", "Гарри Поттер")  # уже на руках
lib.show_status()

lib.return_book("Анна", "Гарри Поттер")
lib.show_status()
```

### Решение

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_taken = False


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def register_reader(self, reader):
        self.readers.append(reader)

    def give_book(self, reader_name, book_title):
        # находим читателя
        target_reader = None
        for reader in self.readers:
            if reader.name == reader_name:
                target_reader = reader

        # находим книгу
        target_book = None
        for book in self.books:
            if book.title == book_title:
                target_book = book

        if target_book is None:
            print(f"Книги '{book_title}' нет в библиотеке")
            return

        if target_book.is_taken:
            print(f"Книга '{book_title}' уже на руках")
            return

        target_book.is_taken = True
        target_reader.books.append(target_book)
        print(f"Книга '{book_title}' выдана читателю {reader_name}")

    def return_book(self, reader_name, book_title):
        for reader in self.readers:
            if reader.name == reader_name:
                for book in reader.books:
                    if book.title == book_title:
                        book.is_taken = False
                        reader.books.remove(book)
                        print(f"Книга '{book_title}' возвращена")
                        return

    def show_status(self):
        print("--- Состояние библиотеки ---")
        for book in self.books:
            if book.is_taken:
                # ищем, у кого она
                holder_name = ""
                for reader in self.readers:
                    for reader_book in reader.books:
                        if reader_book.title == book.title:
                            holder_name = reader.name
                print(f"{book.title} — у читателя {holder_name}")
            else:
                print(f"{book.title} — свободна")
```

---

## Задача 4. Наследование: фигуры

Опишите базовый класс `Shape` с методом `area()`, который возвращает 0. От него унаследуйте классы `Rectangle` (хранит ширину и высоту), `Circle` (хранит радиус) и `Triangle` (хранит основание и высоту). Каждый дочерний класс должен переопределить метод `area()` и считать свою площадь.

Напишите функцию `total_area(shapes)`, которая принимает список фигур и возвращает сумму их площадей.

Пример:

```python
shapes = [
    Rectangle(3, 4),
    Circle(5),
    Triangle(6, 4),
]
print(total_area(shapes))
```

### Решение

```python
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


def total_area(shapes):
    total = 0
    for shape in shapes:
        total = total + shape.area()
    return total


shapes = [
    Rectangle(3, 4),
    Circle(5),
    Triangle(6, 4),
]
print(total_area(shapes))
```
