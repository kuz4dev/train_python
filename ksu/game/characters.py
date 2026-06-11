# общий класс для наших игроков, на базе которого будут создаваться другие расы и классы
import random

class Character:
    def __init__(self, name, base_hp, base_atk, weapon):
        # имя персонажа
        self.name = name
        # базовое хп
        self.base_hp = base_hp
        # базовая атк
        self.base_atk = base_atk
        # оружие нашего персонажа (есть атака)
        self.weapon = weapon

    # жив ли
    @property
    def is_alive(self):
        return self.base_hp > 0
    
    # # метод attack(target): уменьшает target.hp на self.weapon.damage, выводит name бьёт target.name на damage урона. Если цель умерла, дополнительно: target.name повержен!.
    def attack(self, target):
        damage = self.weapon.w_base_atk + self.base_atk
        target.base_hp -= damage
        print(f'{self.name} атакует {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')


class Warrior(Character):
    def __init__(self, name, base_hp, base_atk, weapon):
        super().__init__(name, base_hp, base_atk, weapon)

    def ability(self, target):
        # двойной урон
        damage = 2 * (self.weapon.w_base_atk + self.base_atk)
        target.base_hp -= damage
        print(f'{self.name} атакует специальной атакой {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')
        # шанс произведения бонус атаки
        if random.random() >= 0.65: 
            # бонус атака
            damage = 0.7 * (self.weapon.w_base_atk + self.base_atk)
            target.base_hp -= damage
            print(f'Бонус атака! {self.name} атакует {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')
    
    def weapon_buff(self):
        attack = self.weapon.buff("воин", self.base_atk)
        self.base_atk = attack

class Mage(Character):
    def __init__(self, name, base_hp, base_atk, weapon, mana):
        super().__init__(name, base_hp, base_atk, weapon)
        #доп характеристика мана
        self.mana = mana 

    def attack(self, target):
        damage = self.weapon.w_base_atk + self.base_atk
        target.base_hp -= damage
        print(f'{self.name} атакует {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')
        #базовая атака просто с получением маны
        self.mana += 5

    def ability(self, target):
        #если маны >=8, то урон удваивается. После атаки 8 маны расходуется
        if self.mana >= 8:
            self.base_atk += 8
            damage = 2 * (self.weapon.w_base_atk + self.base_atk)
            target.base_hp -= damage
            print(f'{self.name} атакует магической специальной атакой {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')
            self.base_atk -= 8
            self.mana -= 8
        else:
            #если маны меньше, обычная атака с множителем 1,5
            damage = 1.5 * (self.weapon.w_base_atk + self.base_atk)
            target.base_hp -= damage
            print(f'{self.name} атакует усиленной атакой {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')

    def weapon_buff(self):
        attack, mana_buffed = self.weapon.buff('маг', self.base_atk, self.mana)
        self.mana = mana_buffed
        self.base_atk = attack


class Bard(Character):
    def __init__(self, name, base_hp, base_atk, weapon, charisma):
        super().__init__(name, base_hp, base_atk, weapon)
        #доп хара - харизма (мб заменить на вдохновение, посмотрим)
        self.charisma = charisma

    def attack(self, target):
        damage = self.weapon.w_base_atk + self.base_atk
        target.base_hp -= damage
        print(f'{self.name} атакует {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')
        #обычная атака с получением харизмы
        self.charisma += 7

    def ability(self, target):
        #если харизмы >= 12, производится атака равная произведению харизмы деленной на 5,7(пересчитать баланс) и базовой атк. потом забираем 10 харизмы
        if self.charisma >= 12:
            damage = self.charisma / 5.7 * (self.weapon.w_base_atk + self.base_atk)
            target.base_hp -= damage
            print(f'{self.name} атакует специальной атакой {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')
            self.charisma -= 10 

    def weapon_buff(self):
        attack, charisma_buffed = self.weapon.buff("бард", self.base_atk, self.charisma)
        self.charisma = charisma_buffed
        self.base_atk = attack

#вор
class Rouge(Character):
    def __init__(self, name, base_hp, base_atk, weapon, agility):
        super().__init__(name, base_hp, base_atk, weapon)
        #доп хара - ловкость
        self.agility = agility

    def attack(self, target):
        target.base_hp -= self.weapon.w_base_atk + self.base_atk
        #базовая атк с получением ловкости
        self.agility += 3

    def ability(self, target):
        #с шансом 50%, если ловкость >=3, вор совершает базовую атк с множителем 1.2 + бонус атаку с множителем 1,8
        if random.random() >= 0.5 and self.agility >= 3:
            damage = 1.2 * (self.weapon.w_base_atk + self.base_atk)
            target.base_hp -= damage
            print(f'{self.name} атакует специальной атакой {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')
            damage = 1.8 * (self.weapon.w_base_atk + self.base_atk) #бонус атака
            target.base_hp -= damage
            print(f'Бонус атака! {self.name} атакует {target.name} из-за спины на {damage}. Оставшееся хп противника - {target.base_hp}')
            self.agility -= 3 #пересчитать
        else:
            #иначе атк с множителем 1,5
            damage = 1.5 * (self.weapon.w_base_atk + self.base_atk)
            target.base_hp -= damage
            print(f'{self.name} атакует усиленной атакой {target.name} на {damage}. Оставшееся хп противника - {target.base_hp}')

    def weapon_buff(self):
        attack, charisma_buffed = self.weapon.buff("вор", self.base_atk, self.agility)
        self.charisma = charisma_buffed
        self.base_atk = attack
       
