from characters import Character, Warrior, Mage, Bard, Rouge
from weapons import Claymore, Wand
from enemy import Opponent
import random

Classes = {
    "Воин": Warrior,
    "Маг": Mage,
    "Бард": Bard,
    "Вор": Rouge
}

hero_name = input("Введите имя героя")
Hero_class_name = input("Выберите класс героя. Воин/Маг/Бард/Вор")

Hero_class = Classes[Hero_class_name]

stick = Wand(10)
Hero = Hero_class(hero_name, 20, 12, stick, 5)

sword = Claymore(9)
enemy = Opponent("наемник", 520, 9, sword)

print("Однажды вы решили вступить в гильдию. А вот вы уже здесь, ждете своего первого заказа - сопровождение груза. " \
"Ваша первая задача - доставить груз в целости и сохранности. Пока вы его не выполните, на следующий ранг не перейдете. " \
"Все же будет спокойно? Да ведь? Да?... Скажите, почему именно на вашем первом задании появился наемник?")

print("Бой начался.")

while True:
    action = input("Ваш ход. Выберите действие. e - атака, q - способность")
    if action == "e":
        Hero.attack(enemy)
    if action == "q":
        Hero.ability(enemy)
    
    print("Ход противника")
    if random.random() > 0.5:
        enemy.attack(Hero)
    else:
        enemy.ability(Hero)

    if (not enemy.is_alive):
        print("Противник побежден!")
        take = input("оружие противника - двурук. Забираем? 1 - да, 2 - нет")
        if take == "1":
            Hero = Hero_class(hero_name, 1140, 14, sword, 5)
            print("Оружие получено")
        else:
            print("Вы отказались от оружия")
        
        break


    if (not Hero.is_alive):
        print("Вас победили. Вы убегаете и слышите: «Сегодня мы ужинаем!!!» Возможно, первые задания тоже бывают комом, попробуйте еще раз.")
        Hero = Hero_class(hero_name, 20, 12, stick, 5)
        print("Бой начался.")
        


        

  













