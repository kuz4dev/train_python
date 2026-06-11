# Урок-лекция: Работа с JSON в Python

## 1. Введение

**Что такое JSON?**
*   **JSON** (JavaScript Object Notation) — текстовый формат для хранения и передачи данных.
*   Несмотря на слово «JavaScript» в названии, JSON используется **везде**: Python, Go, Java, мобильные приложения, веб-API.
*   **Зачем?** Когда две программы (или два сервиса) хотят обменяться данными, им нужен общий «язык». JSON — самый популярный такой язык в мире.
*   **Цитата:** «Простота — это высшая утончённость» (Леонардо да Винчи). JSON — живое доказательство.

**JSON vs Python: таблица соответствий**

| JSON | Python | Пример JSON |
|------|--------|-------------|
| object | `dict` | `{"name": "Alice", "age": 25}` |
| array | `list` | `[1, 2, 3]` |
| string | `str` | `"hello"` |
| number (int) | `int` | `42` |
| number (float) | `float` | `3.14` |
| true / false | `True` / `False` | `true` |
| null | `None` | `null` |

> Обратите внимание: в JSON строки — **только в двойных кавычках** `"`. Одинарные `'` — ошибка! Также `True` в Python → `true` в JSON, `None` → `null`.

---

## 2. Модуль `json`

**Импорт**
```python
import json
```

Модуль `json` встроен в Python — ничего устанавливать не нужно.

**Два направления работы:**
1.  **Сериализация - упаковка** (Python → JSON): превращаем объект Python в строку/файл JSON.
2.  **Десериализация - распаковка** (JSON → Python): превращаем строку/файл JSON обратно в объект Python.

**Четыре основные функции:**

| Функция | Что делает | Работает с |
|---------|-----------|-----------|
| `json.dumps()` | Python → строка JSON | строками |
| `json.dump()` | Python → файл JSON | файлами |
| `json.loads()` | строка JSON → Python | строками |
| `json.load()` | файл JSON → Python | файлами |

> Запоминалка: буква **s** на конце = **s**tring (строка). Без **s** = файл.

---

## 3. Сериализация: из Python в JSON

### 3.1. `json.dumps()` — в строку

```python
import json

student = {
    "name": "Анна",
    "age": 20,
    "courses": ["Python", "Математика", "Физика"],
    "graduated": False,
    "thesis": None
}

# Превращаем dict в строку JSON
json_string = json.dumps(student)
print(json_string)
# {"name": "\u0410\u043d\u043d\u0430", "age": 20, ...}  — кириллица закодирована!
```

**Полезные параметры `dumps()`:**

```python
# ensure_ascii=False — чтобы кириллица читалась нормально
# indent=2 — красивый отступ для чтения человеком
json_string = json.dumps(student, ensure_ascii=False, indent=2)
print(json_string)
```

Результат:
```json
{
  "name": "Анна",
  "age": 20,
  "courses": [
    "Python",
    "Математика",
    "Физика"
  ],
  "graduated": false,
  "thesis": null
}
```

> Для русского языка **всегда** используйте `ensure_ascii=False`, иначе получите нечитаемые `\uXXXX` коды.

### 3.2. `json.dump()` — в файл

```python
import json

student = {
    "name": "Анна",
    "age": 20,
    "courses": ["Python", "Математика", "Физика"],
    "graduated": False
}

# Записываем в файл
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent=2)

# Файл student.json создан!
```

> Используем `with` (менеджер контекста) — как вы уже знаете из прошлого занятия. Также указываем `encoding="utf-8"`, чтобы кириллица сохранилась корректно.

---

## 4. Десериализация: из JSON в Python

### 4.1. `json.loads()` — из строки

```python
import json

json_string = '{"name": "Анна", "age": 20, "graduated": false}'

# Превращаем строку JSON обратно в dict
student = json.loads(json_string)

print(student["name"])    # Анна
print(type(student))      # <class 'dict'>
print(student["graduated"])  # False  (уже Python-овский False!)
```

### 4.2. `json.load()` — из файла

```python
import json

with open("student.json", "r", encoding="utf-8") as f:
    student = json.load(f)

print(student["name"])      # Анна
print(student["courses"])   # ['Python', 'Математика', 'Физика']
```

---

## 5. Частые ошибки и подводные камни

### 5.1. `JSONDecodeError` — некорректный JSON

```python
import json

bad_json = "{'name': 'Анна'}"  # Одинарные кавычки — это НЕ JSON!

student = json.loads(bad_json)
# json.decoder.JSONDecodeError!
```

**Как защититься:**
```python
import json

data_string = "какие-то данные..."

try:
    data = json.loads(data_string)
except json.JSONDecodeError as e:
    print(f"Ошибка разбора JSON: {e}")
```

### 5.2. Что нельзя сериализовать

JSON поддерживает не все типы Python. Например, `set`, `datetime`, `tuple` — не сериализуются напрямую.

```python
import json

data = {"tags": {"python", "json", "файлы"}}  # set!
json.dumps(data)
# TypeError: Object of type set is not JSON serializable
```

**Решение:** преобразуйте вручную перед сериализацией.
```python
data = {"tags": list({"python", "json", "файлы"})}  # set → list
json.dumps(data, ensure_ascii=False)
# Работает!
```

> **Важно:** `tuple` при сериализации превращается в `list` (массив JSON `[]`). Обратно `tuple` не восстановится — вернётся `list`.

### 5.3. Кодировка

Если забыть `encoding="utf-8"` при работе с файлами на Windows, кириллица может сломаться. Правило простое: **всегда указывайте `encoding="utf-8"`**.

---

## 6. Практический пример: мини-база данных

Давайте создадим простую «базу данных» студентов в JSON-файле.

```python
import json

# --- Запись ---
students = [
    {"name": "Анна", "age": 20, "grade": 4.5},
    {"name": "Борис", "age": 22, "grade": 3.8},
    {"name": "Вера", "age": 21, "grade": 4.9},
]

with open("students_db.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

print("База сохранена!")

# --- Чтение и поиск ---
with open("students_db.json", "r", encoding="utf-8") as f:
    students = json.load(f)

# Найдем отличников (grade >= 4.5)
excellent = [s for s in students if s["grade"] >= 4.5]
for s in excellent:
    print(f"{s['name']} — оценка {s['grade']}")

# --- Добавление нового студента ---
new_student = {"name": "Галина", "age": 19, "grade": 4.2}
students.append(new_student)

with open("students_db.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

print("Новый студент добавлен!")
```

> Обратите внимание: чтобы **добавить** данные в JSON-файл, нужно сначала **прочитать** весь файл, изменить данные в памяти, а потом **перезаписать** файл целиком. Это отличается от режима `'a'` для обычных текстовых файлов!

---

## 7. JSON и веб-API (бонус)

В реальном мире JSON чаще всего встречается в **веб-API**. Вот простой пример:

```python
import json
import urllib.request

# Получаем данные о пользователе с публичного API
url = "https://jsonplaceholder.typicode.com/users/1"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

print(f"Имя: {data['name']}")
print(f"Email: {data['email']}")
print(f"Город: {data['address']['city']}")
```

> Это упрощённый пример. В реальных проектах обычно используют библиотеку `requests`, но она требует установки. `urllib` — встроенный модуль.

---

## 8. Шпаргалка

```
Python → строка JSON:    json.dumps(obj)
Python → файл JSON:      json.dump(obj, file)
строка JSON → Python:    json.loads(string)
файл JSON → Python:      json.load(file)

Полезные параметры:
  ensure_ascii=False    — для кириллицы
  indent=2              — красивый вывод
  encoding="utf-8"      — в open() для файлов
```

---

## 9. Задания для практики

1.  **Простое:** Создайте словарь со своими данными (имя, возраст, хобби — список). Сохраните в файл `me.json` и прочитайте обратно.

2.  **Среднее:** Напишите программу «Телефонная книга». Она должна:
    *   Загружать контакты из `contacts.json` (создайте файл) при старте (если файл есть).
    *   Позволять добавить новый контакт (имя + телефон).
    *   Сохранять контакты обратно в файл.

3.  **Сложное:** Спроектируйте и добавьте сохранение в файл .json в программе копилки
    *   Добавьте туда все операции с копилкой
    *   Также требуется сохранять и менять баланс в файле

---

**Вопросы?**
