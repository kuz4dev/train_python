import random

class Monster():
    def __init__(self, name, race, rank, hp, clear_damage):
        # имя монст
        self.name = name
        # раса монстра
        self.race = race
        #низший, обычный, редкий, легендарный (босс)
        self.rank = rank
        #низшие = 1-10, обычные = 11-30. редкие = 31-50 (может быть востановление)
        #легендарные = 60-160
        self.hp = hp
        #урон монстра/ не прописано по рангам
        self.clear_damage = clear_damage

    @property
    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        if (self.hp > 0):
            target.hp -= self.clear_damage
            print(f"{self.race} аттакавал(а) на {self.clear_damage} урона {target.name}. Здоровье персонажа {target.hp}")

            chance = random.random()
        
            if chance <= 0.35:
                print("пи-пи-пи, вас отравила крыса при атаке, нанесен двойной урон")
                target.hp -= self.clear_damage
                print(f"{self.race} отравил(а) на {self.clear_damage} урона {target.name}. Здоровье персонажа {target.hp}")
            else:
                print(f"когти и зубы {self.race} при атаке не нанесли яд")

class Rat(Monster):
    def __init__(self, race, rank, hp, clear_damage):
        super().__init__(race, rank, hp, clear_damage)
    
