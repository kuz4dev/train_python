# Реализуй систему школьного журнала из трёх классов: Student, Subject и Journal.

# Student:
# атрибуты: name, surname
# метод __str__ возвращает "Name Surname"

# Subject:
# атрибуты: title, grades — словарь вида {student: [список оценок]}
# метод add_grade(student, grade) — добавляет оценку студентке (от 2 до 5, иначе сообщение об ошибке и оценка не ставится)
# метод average(student) — средний балл студентки по этому предмету (0, если оценок нет)
# метод top_students() — список студенток со средним баллом ≥ 4.5

# Journal:
# атрибуты: class_name (например, "7А"), subjects — список объектов Subject, students — список студенток
# метод add_student(student)
# метод add_subject(subject)
# метод overall_average(student) — средний балл студентки по всем предметам сразу (среднее по всем оценкам, а не среднее средних)
# метод best_student() — студентка с наибольшим общим средним
# метод report() — печатает таблицу: для каждой студентки её средний по каждому предмету и общий средний

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Subject:
    def __init__(self, title, grades):
        self.grades = grades
        self.title = title

    def add_grade(self, student, new_grade):
        # сделать проверку условием на оценку (больше или равна двум и меньше или равна 5)
        if new_grade < 2 or new_grade > 5:
            print('Ошибка! Оценка не подходит')
            return

        if student not in self.grades:
            self.grades[student] = []
        
        self.grades[student].append(new_grade)

    #средний балл студентки по этому предмету (0, если оценок нет)
    def average(self, student):
        # len(self.grades[student]) = 0
        if student in self.grades and len(self.grades[student]) != 0:
            return sum(self.grades[student]) / len(self.grades[student])
        else:
            return 0

    # список студенток со средним баллом ≥ 4.5  
    def top_students(self):
        top_av_students = []

        for stud in self.grades:             
            if sum(self.grades[stud]) / len(self.grades[stud]) >= 4.5:                 
                top_av_students.append(stud)    

        return top_av_students
    
class Journal:
    def __init__(self, class_name, subjects_list, students):
        self.class_name = class_name
        self.subjects_list = subjects_list
        self.students = students
        
    def add_student(self, person):
        self.students.append(person)

    def add_subject(self, subject):
        self.subjects_list.append(subject)

    # метод overall_average(student) — средний балл студентки по всем предметам сразу (среднее по всем оценкам, а не среднее средних)
    def overall_average(self, student):
        total = 0 # сумма всех оценок
        count = 0 # количество всех оценок

        for subject in self.subjects_list:
            for grade in subject.grades.get(student, []):
                total += grade
                count +=1

        if count == 0:
            return 0

        return total / count
        


# sum(список чисел)
# len(список)
grades = {
    "Ксюша": [5, 5, 5, 5, 5],
    "Соня": [4, 3, 5, 3, 3]
}

grades_rus = {
    "Ксюша": [5, 5, 5, 5, 5],
    "Соня": [5, 5, 5, 5, 5]
}

# students = ["Ксюша", "Соня"]
# subjects_list = []


math = Subject('Математика', grades)
rus = Subject('Русский язык', grades_rus)

math.add_grade('Игорь', 4)
math.add_grade('Игорь', 6)

print(math.average('Игорь'))
print(math.average('Соня'))
print(math.average('Ксюша'))

print(math.top_students())

journal = Journal('11', [], [])
journal.add_student('Игорь')
journal.add_student('Соня')
journal.add_student('Ксюша')
journal.add_subject(math)
journal.add_subject(rus)

print(journal.overall_average('Соня'))



