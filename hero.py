import random

class Hero:
    def __init__(self, name, current_hp, starting_hp = 100):
        self.name = name 
        self.current_hp = current_hp
        self.starting_hp = starting_hp
    
    def fight(self, opponent):
        fighters = [self.name, opponent]
        winner = random.choice(fighters)
        print(f'{winner} won!')


hero1 = Hero('superman', 200)
hero2 = Hero('batman', 200)
hero1.fight(hero2.name)