from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self, team_one, team_two):
        self.team_one = Team(team_one)
        self.team_two = Team(team_two)

    def create_hero(self):
        hero_name = input('Hero name: ')
        hero = Hero(hero_name, current_hp=100)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
                self.create_ability()
           elif add_item == "2":
                self.create_weapon()
           elif add_item == "3":
                self.create_armor()
        return hero

    def create_ability(self):
        name = input('What is the ability name? ')
        max_dmg = input('What is the max damage of the ability? ')
        return Ability(name, max_dmg)

    def create_weapon(self):
        name = input('What is the weapon name? ')
        max_dmg= input('What is the max damage of the weapon? ')
        return Weapon(name, max_dmg)

    def create_armor(self):
        name = input('What is the name of the armor? ')
        max_block = input('What is the max block of the armor? ')   

    def build_team_one(self):
        numOfTeamMembers = int(input('How many members would you like on Team One?\n'))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
    
    def build_team_two(self):
        numOfTeamMembers = int(input('How many members would you like on Team Two?\n'))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
    
    def team_battle(self):
        Team.attack(self.team_one, self.team_two)
    
    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + 'average K/D was: ' + str(team_kills/team_deaths))
        print(self.team_two.name + 'average K/D was: ' + str(team_kills/team_deaths))


        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print('survived from ' + self.team_one.name + ': ' + hero.name)
        
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print('survived from ' + self.team_two.name + ': ' + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena('1', '2')
    print('Welcome to the Superhero Fighter!')
    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()


