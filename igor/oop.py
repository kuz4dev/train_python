# Создадть класс Человек
# Определить его имя, фамилию и возраст
# Создадим метод (функция) класса с приветствием
# Создадим людей Ксюшу, Соню и Игоря и узнаем все их поля и методы


# поле - переменная для класса


class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def say_hello(self):
        print('Привет!')

    def grow_up(self, age):
        self.age = age
        print(f'Я стала/стал старше, теперь мне {self.age}')

    def change_surname(self, new_surname):
        self.surname = new_surname 
        print(f"Новая фамилия - {self.surname}")
        
    def change_name(self, new_name):
        self.name = new_name
        print(f"Новое имя - {self.name}")

class Programmer(Human):
    def __init__(self, language, name, surname, age):
        super().__init__(name, surname, age)
        self.language = language

    def grow_up(self, plus):
        self.age = self.age + plus
        print(f'Я стала/стал старше на {plus} лет, теперь мне {self.age}')

    def who_i_am(self):
        print(f'Я программирую на {self.language}, имя - {self.name}, возраст - {self.age}')


Sophi = Programmer('python', 'Соня', 'Самошкина', 14)
Sophi.who_i_am()
# Sophi.grow_up(2)
# print(Sophi.age)





# Sophi = Human('Соня', 'Самошкина', 14)
# Sophi.say_hello()
# Sophi.say_hello()
# print(Sophi.age, Sophi.name, Sophi.surname)
# Sophi.change_surname("бам")
# Sophi.change_name("бум") 

# Ksu = Human("Ксюша", "Самошкина", 16)
# Ksu.say_hello()
# print(Ksu.surname, Ksu.name, Ksu.age)
# Ksu.change_surname("Чернавина")

# igor = Human("Игорь", "Казьмин", 23)
# igor.say_hello()
# print(igor.surname, igor.name, igor.age)

# igor.change_name('Андрей')
# igor.change_surname('Попов')