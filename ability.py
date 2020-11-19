import random

class Ability:
    def __init__(self, name, max_dmg):
        self.name = name
        self.max_dmg = max_dmg
    
    def attack(self):
        atk = random.randint(0, self.max_dmg)
        return atk