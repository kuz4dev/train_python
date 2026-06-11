class Weapon():
    def __init__(self, name, damage, level):
        #имя оружия
        self.name = name 

        # урон оружия
        self.damage = damage

        #уровень оружия
        self.level = level

#класс меч с родителем оружие
class Sword(Weapon):
    def __init__(self, name, damage, level):
        super().__init__(name, damage, level)

#класс лук с родителем оружие
class Bow(Weapon): 
    def __init__(self, name, damage, level, arrows):
        super().__init__(name, damage, level)

        #счетчик стрел
        self.arrows = arrows
