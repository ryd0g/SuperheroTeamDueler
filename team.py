class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        foundHero = False
        for i in self.heroes:
            if i.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_heroes(self):
        for i in self.heroes:
            print(i)

    