import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, current_hp, starting_hp = 100):
        self.name = name 
        self.current_hp = current_hp
        self.starting_hp = starting_hp
        self.abilities = list()
        self.armors = list()
    
    def fight(self, opponent):
        fighters = [self.name, opponent]
        winner = random.choice(fighters)
        print(f'{winner} won!')

    def attack(self):
        total_dmg = 0
        for ability in self.abilities:
            total_dmg += ability.attack()
        return total_dmg
    
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)
    
    def take_damage(self, dmg):
        self.current_hp -= dmg - self.defend()
        return self.current_hp

hero = Hero('Ryan', 200)
shield = Armor('shield', 50)
hero.add_armor(shield)
hero.take_damage(60)
print(hero.current_hp)