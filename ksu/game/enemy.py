from characters import Character
import random

class Opponent(Character):
    def __init__(self, name, base_hp, base_atk, weapon):
        super().__init__(name, base_hp, base_atk, weapon)

    def ability(self, target):
        damage = self.weapon.w_base_atk + self.base_atk
        target.base_hp -= 1.5 * damage
        print(f'{self.name} атакует вас специальной атакой {target.name} на {damage}. Оставшееся хп - {target.base_hp}')
        
        if random.random() >= 0.5: 
            # бонус атака
            damage =  self.weapon.w_base_atk + self.base_atk
            target.base_hp -= 0.46 * damage
            print(f'Бонус атака! {self.name} атакует вас на {damage}. Оставшееся хп - {target.base_hp}')