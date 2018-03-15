from random import *
import characters
import equipment

class Location:
    def __init__(self, name):
        self.name = name
    places = []
    def options(self):
        while True:
            try:
                print('\n' + '*' * 75)
                print('{} : Go where?\n'.format(self.name))
                for num, locale in enumerate(self.places):
                    print('| {}.  {}'.format(num + 1, locale))
                print('\n> ', end =' ')
                choice = int(input())
                if choice in range(1, len(self.places) + 1):
                    return choice
            except IndexError:
                print('Invalid input.')
                
           
class Town(Location):
    def __init__(self, name, places, itemlist, special):
        super().__init__(name)
        self.places = places
        self.itemlist = itemlist
        self.special = special
    
    def go_to(self, locale):
        while True:
            if self.places[locale - 1] == 'Leave':
                break
            elif self.places[locale - 1] == 'Shop':
                print('\n' + '*' * 75)
                print('Welcome to the {} Item shop! What would you like to buy?'.format(self.name))
                print('\nZenny: {}'.format(hero.zenny))
                print('Potions: {}\n'.format(hero.potions))
                shop = Shop(self.itemlist)
                shop.selection()
                locale = self.options()
            elif self.places[locale - 1] == 'Training Ground':
                print('Welcome to the {} Training Ground! Here are our courses.'.format(self.name))
                print('\nZenny: {}'.format(hero.zenny))
                print('Potions: {}\n'.format(hero.potions))
                shop = Shop(self.special)
                shop.selection()
                locale = self.options()
        
    
class Shop:
    def __init__(self, itemlist):
        self.itemlist = itemlist
    def selection(self):
        while True:
            try:
                for num, item in enumerate(self.itemlist):
                    print('{}. {}'.format(num + 1, item), end ='\t')
                print('\n> ')
                choice = int(input())
                if self.itemlist[choice - 1] == 'Leave':
                    print('Thanks for coming by.')
                    break
                else:
                    self.buy(self.itemlist[choice - 1])
            except IndexError:
                print('Invalid input.')
   
    def buy(self, item):
        if item == 'Potion':
            if hero.zenny < 5:
                print('Not enough zenny. Cost 5\n')
            else:
                hero.zenny -= 5
                hero.potions =+ 1
                print('Thanks!\nYou got a Potion!\n')
        elif item == 'Chainmail':
            if hero.zenny < 30:
                print('Not enough zenny. Cost 30\n')
            elif hero.armor.name == 'Chainmail':
                print('You already have that!\n')
            elif hero.armor.armor > 1:
                print('The armor you have is better.\n')
            else:
                hero.zenny -= 30
                hero.armor = equipment.chainMail()
                print('Thanks\nYou got Chainmail!\n')
                
        elif item == 'Longsword':
            if hero.zenny < 25:
                print('Not enough zenny. Cost 25')
            elif hero.armor.name == 'Longsword':
                print('You already have that!\n')
            elif hero.weapon.weapdmgmax > 6:
                print('The armor you have is better.\n')
            else:
                hero.zenny -= 25
                hero.weapon = equipment.longSword()
                print('Thanks!\nYou got a Longsword!\n')
                
        elif item == 'Strength training':
            if hero.power >= hero.starting_power + 2:
                print('You\'ve trained your strength to the max.\n')
            elif hero.zenny < 25:
                print('Not enough zenny. Cost 25')
            else:
                hero.zenny -= 25
                print('You feel stronger! Gained 1 power!')
                hero.power += 1
        
        elif item == 'Evasion':
            if hero.power >= hero.starting_power + 4:
                print('You\'ve trained your Evasion to the max.\n')
            elif hero.zenny < 35:
                print('Not enough zenny. Cost 35')
            else:
                hero.zenny -= 35
                print('You feel more agile!')
                hero.evasion += 1
     
    
def combat(player, enemy):
    player = player
    enemy = enemy
    while player.alive() is True and enemy.alive() is True:
        print()
        player.check_status()
        enemy.check_status()
        print()
        print("-" * 54)
        print("| 1.Fight {} \t\t\t2.Do nothing |".format(enemy.name))
        print("| 3.Use potion     \t\t\t4.Flee       |")
        print("-" * 54)
        print("> ", end=' ')
        raw_input = input()
        print('*'* 75)
        if raw_input == "1":
            dmg = player.attack(enemy)
            print()
            enemy.hp -= dmg
        elif raw_input == "2":
            print('You stand there like a jackass.')
            print()
        elif raw_input == "3":
            player.use_potion()
        elif raw_input == "4":
            print('You run from the {}. You  are forever branded a coward'.format(enemy.name))
            print()
            retire(True)
        else:
            print('Invalid input')
            continue

        if enemy.hp > 0:
            # Enemy attack
            dmg = enemy.attack(player)
            player.hp -= dmg
            if player.hp <= 0:
                print("You are dead.")
                exit()
        else:
            print('You defeated the {}!'.format(enemy.name))
            hero.zenny += enemy.bounty

def main():
    innsmouth = Town('Innsmouth', ['Shop', 'Training Ground', 'Leave'], 
    ['Leave', 'Potion', 'Chainmail', 'Longsword'], ['Leave', 'Strength training', 'Evasion'])
    while True:
        print('*'* 75)
        print('Zenny: {}'.format(hero.zenny))
        print('Potions: {}'.format(hero.potions))
        print("-" * 56)
        print("| 1.Venture \t\t\t\t2.Go to town   |")
        print("| 3.Use potion     \t\t\t4.Retire       |")
        print("-" * 56)
        print("> ", end=' ')
        raw_input = input()
        if raw_input == '1':
            venture()
        elif raw_input == '2':
            place = innsmouth.options()
            innsmouth.go_to(place)
        elif raw_input == '3':
            hero.use_potion()
            hero.check_status()
        elif raw_input == '4':
            retire(False)
        else:
            print('Invalid input')

def common_encouter():
    roll = randint(1, 100)
    if roll in range(1, 51):
        foe = characters.Goblin('Goblin', 7)
        print('It\'s another goblin! Defend yourself!')
        combat(hero, foe)
        slain['Goblin'] += 1
    elif roll in range(51, 101):
        foe = characters.Zombie('Zombie', 10)
        print('A shambling corpse approaches! You\'ve seen this movie.')
        combat(hero, foe)
        slain['Zombie'] += 1

def uncommon_encounter():
    roll = randint(1, 100)
    if roll in range(1, 51):
        foe = characters.Goblin('Goblin', 10)
        print('A big looking goblin approaches! Attack!')
        combat(hero, foe)
        slain['Goblin'] += 1
        
    elif roll in range(51, 101):
        foe = characters.Bandit('Bandit', 10)
        print('A bandit jumps out from the shadows! Stay away from my loot!')
        combat(hero, foe)
        slain['Bandit'] += 1
        
def rare_encounter():
    print('Uh oh. A menacing looking hobgoblin is coming.')
    foe = characters.Hobgoblin('Hobgoblin', 15)
    combat(hero, foe)
    slain['Hobgoblin'] += 1

def special_encounter():
    pass

def loot_roll():
    input('A treasure chest! As you go to open it...')
    loot = randint(1,20)
    if loot in range(1, 11):
            print('You found a potion. That\'ll come in handy.')
            hero.potions += 1
    elif loot in range(11, 16):
            print('There\'s 2 potions! Lucky!')
            hero.potions += 2
    elif loot in range(16, 20):
            print('The chest has teeth and it attacks! What sick bastard thought of this!?')
            mim = characters.Mimic('Mimic', 10)
            combat(hero, mim)
            slain['Mimic'] += 1
    else:
        if hero.weapon.name != 'Excalibur':
            print('A gleaming golden sword is in the chest. It looks far better than yours.')
            print('Good thing anything left in chests is free for the taking! /Get!')
            hero.weapon = equipment.Excalibur()
            print('You got Excalibur!')
        else:
            print('3 potions! Who is leaving these here?')
            hero.potions += 3

def venture():
    print()
    quest = randint(1,100)
    if quest in range(1, 51):
        common_encouter()
        
    elif quest in range(51, 71):
        uncommon_encounter()
        
    elif quest in range(71, 91):
        loot_roll()
        
    elif quest in range(91, 98):
        rare_encounter()
        
    elif quest in range(98, 101):
        pass
    
def retire(flee):
    print('\nFinal Tally:\n')
    for key, value in slain.items():
        print(key + ': '+ str(value))
    print('\n{} potions left'.format(hero.potions))
    score = 0
    score += slain['Goblin'] * 50
    score += slain['Zombie'] * 60
    score += slain['Mimic'] * 70
    score += slain['Hobgoblin'] * 150
    score += slain['Bandit'] * 80
    score += hero.potions * 30
    print()
    if flee == True:
        print('-10% for cowardice')
        score -= score * .1
    else:
        pass
    out = 'TOTAL SCORE: {}'.format(score)
    print('*' * (len(out) + 4))
    print('* ' + out + ' *')
    print('*' * (len(out) + 4))
    exit()
    
hero = characters.Hero('Hero', 12)
# keep track of all slain enemies
slain = dict(Goblin = 0, Mimic = 0, Zombie = 0, Bandit = 0, Hobgoblin = 0)
main()
