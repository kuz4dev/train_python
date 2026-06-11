# Реализуй систему школьного журнала из трёх классов: Student, Subject и Journal.  00

# Student:
# атрибуты: name, surname  00
# метод __str__ возвращает "Name Surname"  00

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
        #имя студента
        self.name = name
        #фамилия студента
        self.surname = surname

    #вывод студента __str__(self)	str(self), print(self)
    def __str__(self):
        return f"{self.name} {self.surname}"


class Subject:
    def __init__(self, title, grades):
        #название предмета
        self.title = title
        #оценки
        self.grades = grades

    def add_grade(self, student, grade):
            if student not in self.grades:
                self.grades[student] = []

            if grade >= 2 and grade <= 5:
                if student in self.grades:
                    self.grades[student].append(grade)
            else:
                print("обшибка")

    #метод average(student) — средний балл студента по этому предмету (0, если оценок нет)
    def average(self, student):
        if student in self.grades:
            if len(self.grades[student]) != 0:
                return sum(self.grades[student]) / len(self.grades[student])
        else:
            return 0
    
    def top_students(self): # метод top_students() — список студентов со средним баллом ≥ 4.5
        top = []
        
        for student in self.grades:
            if self.average(student) >= 4.5:
                top.append(student)

        return top

grades = {
    "Ксюша": [5 ,4, 5, 5, 5],
    "Софа": [3, 5, 3, 3, 5]
}


Sonya = Student(name="Соня", surname="Таз")
Igor = Student(name="Игорь", surname="абоба")
top_students = []

math = Subject('Математика', grades)
math.add_grade('Игорь', 4)
math.add_grade('Игорь', 5)

print(math.average('Игорь'))
print(math.average('Софа'))
print(math.average('Ксюша'))
print(math.top_students())

print(Sonya)
print(Igor)
# print(Subject.top_students())

class Journal:
    def __init__(self, class_name, subjects, student):
        self.class_name = class_name  # class_name - название класса (например, "7А")
        self.subjects = subjects    # subjects — список объектов Subject
        self.students = student   # students — список студентов

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def overall_average(self, student): # — средний балл студентки по всем предметам сразу (среднее по всем оценкам, а не среднее средних)
        #к примеру. [Соня = {математика: среднее мат, русский: среднее рус.}]

        for subject in self.subjects_list:
            for grade in subject.grades.get(student, []):
                total += grade
                count +=1

        if count == 0:
            return 0

        return total / count

    def best_student():   # — студентка с наибольшим общим средним
        pass

    def report():  # — печатает таблицу: для каждой студентки её средний по каждому предмету и общий средний
        pass