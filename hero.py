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
        if self.abilities == [] or opponent.abilities == []:
            print("It's a draw!")
        else:
            print('Let the fight begin!')
        while(self.is_alive() == True and opponent.is_alive() == True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if opponent.is_alive() == False:
            print(f"{self.name} wins!")
        else:
            print(f"{villain.name} wins!")

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

    def is_alive(self):
        if self.current_hp <= 0:
            return False
            print("You Died")
        else:
            return True
            print("You're still alive!")

hero = Hero('Ryan', 200)
villain = Hero('Joe', 200)
ability1 = Ability('laser beam', 50)
ability2 = Ability('punch', 100)
hero.add_ability(ability1)
villain.add_ability(ability2)
hero.fight(villain)