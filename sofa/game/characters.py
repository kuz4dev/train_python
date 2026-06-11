class Character():
    def __init__(self, name, race, rank, hp, weapon, clear_damage):
        #имя персонажа
        self.name = name
        #раса персонажа
        self.race = race
        # ранг/уровень персонажа
        self.rank = rank 
        # здоровье персонажа
        self.hp = hp
        # оружие персонажа
        self.weapon = weapon
        #чистый урон персонажа. при атаке урон оружия + урон персонажа
        self.clear_damage = clear_damage
        
    #жив ли персонаж? проверка здоровья. if 0 = false. if 1 = true.
    @property
    def is_alive(self):
        return self.hp > 0
    
    #функция атаки
    def attack(self, target):
        if (self.hp > 0):
            #убавляем у здоровя цели, урон оружия и чистый урон
            target.hp -= self.weapon.damage + self.clear_damage
            print(f"{self.name} аттакавал(а) на {self.weapon.damage + self.clear_damage} урона {target.name}. Здоровье врага {target.hp}")
        