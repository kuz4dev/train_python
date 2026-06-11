from characters import Character
from weapons import Sword, Bow
from monsters import Monster

import random

#оружия что используются
Cool_Bow = Bow("крутое", 14, 14, 16)
Normal_Sword = Sword("нормальное", 12, 14)

#персонажи name, race, rank, hp, weapon, clear_damage
Sonya = Character('Соня', 'Эльф', 10, 100, Cool_Bow, 6)
Igor = Character('Игорь', 'Дварф', 10, 100, Normal_Sword, 7)
# name, race, rank, hp, clear_damage
agressiv_rat = Monster('Агрессивная крыса', "крыса", "обычный",  random.randint(5, 13), random.randint(5, 7))


def Attack_Rat(): #драка с крысой
    while Sonya.hp >= 0 or agressiv_rat.hp >= 0:
        Sonya.attack(agressiv_rat)
        agressiv_rat.attack(Sonya)

        if Cool_Bow.arrows == 0:
            print(f"{Sonya.name} не может больше сражатся")
            while Sonya.hp != 0:
                agressiv_rat.attack(Sonya)

        is_over = win_loger(agressiv_rat, Sonya)

        if is_over: 
            break


def Attack_Igor():   #драка с игорем
    while Sonya.hp >= 0 or Igor.hp >= 0:
        Sonya.attack(Igor)
        Igor.attack(Sonya)

        if Cool_Bow.arrows == 0:
            print(f"{Sonya.name} не может больше сражатся")
            while Sonya.hp != 0:
                Igor.attack(Sonya)
        
    
        is_over = win_loger(Igor, Sonya)

        if is_over: 
            break


def win_loger(opponent_first, opponent_second):
    if opponent_first.hp <= 0:
        print(F"{opponent_first.name} мертв(а), {opponent_second.name} победил(a)")
        return True
    elif opponent_second.hp <= 0:
        print(F"{opponent_second.name} мертв(а), {opponent_first.name} победил(a)")
        return True

    return False
    


do = int(input(f"Время для сражений! Нужно выбрать врага! 1 - Игорь (тестово), 2 - агресивная крыса "))


if do == 1:
    Attack_Igor()
    
elif do == 2:
    Attack_Rat()


elif do != 1 or do != 2:
    print("Враг не найден >_<. Попробуйте еще раз.")


if Igor.hp <= 0 or agressiv_rat.hp <= 0:
    Sonya.hp += 20
    print(F"Первый враг повержен, остался еще один. Из врага выпало зелье здоровья, выпив ваше здоровье стало: {Sonya.hp}")

    print("пойдем на следующего врага.")

    if do == 1: #если в начале мы шли на игоря, сейчас на крысу
        Attack_Rat()
    if do == 2: #если в начале мы шли на крысу, сейчас на Игоря
        Attack_Igor()


#TODO: 
# 1. в коде повторяется строчка о стрелах, но не выводится кол-во стрел. 
# 2. почистить файлы.