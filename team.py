import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
        self.living_heroes = list()
        self.living_opponents = list()

    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_heroes(self):
        for i in self.heroes:
            print(i)
    
    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_hp = health

    def attack(self, other_team):

        for hero in self.heroes:
            self.living_heroes.append(hero)

        for hero in other_team.heroes:
            other_team.living_opponents.append(hero)
        
        while len(self.living_heroes) > 0 and len(other_team.living_opponents)> 0:
            randomhero1 = random.choice(self.living_heroes)
            randomhero2 = random.choice(other_team.living_opponents)
            randomhero1.fight(randomhero2)