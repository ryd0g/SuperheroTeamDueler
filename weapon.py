from ability import Ability
import random

class Weapon(Ability):
    def __init__(self, name, max_dmg):
        self.name = name
        self.max_dmg = max_dmg
    def attack(self):
        weapon_dmg = random.randint(self.max_dmg // 2, self.max_dmg)
        return weapon_dmg