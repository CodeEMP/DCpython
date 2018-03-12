from random import *
class Weapon:
    def __init__(self, name, weapdmgmin, weapdmgmax):
        self.name = name
        self.weapdmgmin = weapdmgmin
        self.weapdmgmax = weapdmgmax
    def damage(self):
        pass
        
class Character:
    def __init__(self, name, hp,):
        self.name = name
        self.hp = hp
        self.maxhp = hp
    def alive(self):
        if self.hp < 1:
            return False
        else:
            return True
    def check_status(self):
        print('{} has {} health left.'.format(self.name, self.hp))

class Hero(Character):
    potions = 3
    weapon = Weapon('Sword', 3, 5)
    def attack(self):
        dmg = randint(self.weapon.weapdmgmin, self.weapon.weapdmgmax)
        print('You attack with your {}, dealing {} damage.'.format(self.weapon.name, dmg))
        return dmg
    def use_potion(self):
        if self.potions < 1:
            print('You out of potions! Oh no!')
        else:
            print('You chug a potion in the midst of combat! Ballsy.')
            heal = randint(5, 8)
            self.hp += heal
            self.potions -= 1
            print('It heals you for {}.'.format(heal))
            print('You have {} potions left'.format(self.potions))
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            else:
                pass

class Goblin(Character):
    def check_status(self):
        if self.hp/self.maxhp * 100 <= 50:
            print('The goblin is looking injured.')
        else:
            print('The goblin seems to be in good health.')
    weapon = Weapon('Dagger', 1, 2)
    def attack(self):
        dmg = randint(self.weapon.weapdmgmin, self.weapon.weapdmgmax)
        print('The Goblin attacks with his {}, dealing {} damage.'.format(self.weapon.name, dmg))
        return dmg

class Zombie(Character):
    def check_status(self):
        if self.hp/self.maxhp * 100 <= 50:
            print('The zombie is looking more corpsey.')
        else:
            print('The zombie shambles energetically.')
    weapon = Weapon('gross hands', 1, 1)
    def attack(self):
        dmg = randint(self.weapon.weapdmgmin, self.weapon.weapdmgmax)
        print('The Zombie attacks with his {}, dealing {} damage.'.format(self.weapon.name, dmg))
        return dmg

class Mimic(Character):
    def check_status(self):
        if self.hp/self.maxhp * 100 <= 50:
            print('The mimic is still terrifying.')
        else:
            print('The mimic looks pretty broken, but is still terrifying.')
    weapon = Weapon('Bite', 3, 4)
    def attack(self):
        dmg = randint(self.weapon.weapdmgmin, self.weapon.weapdmgmax)
        print('The Mimic attacks with his {}, dealing {} damage.'.format(self.weapon.name, dmg))
        return dmg
        
class Hobgoblin(Character):
    def check_status(self):
        if self.hp/self.maxhp * 100 <= 50:
            print('The Hobgoblin smirks.')
        else:
            print('The Hobgoblin is looking a little more worried.')
    weapon = Weapon('Sword', 3, 5)
    def attack(self):
        dmg = randint(self.weapon.weapdmgmin, self.weapon.weapdmgmax)
        print('The Hobgoblin attacks with his {}, dealing {} damage.'.format(self.weapon.name, dmg))
        return dmg
        
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
            dmg = player.attack()
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
            exit()
        else:
            print('Invalid input')
            continue

        if enemy.hp > 0:
            # Enemy attack
            dmg = enemy.attack()
            player.hp -= dmg
            if player.hp <= 0:
                print("You are dead.")
                exit()
        else:
            print('You defeated the {}!'.format(enemy.name))
                
def main():
    # keep track of all slain enemies
    slain = dict(Goblin = 0, Mimic = 0, Zombie = 0, Hobgoblin = 0)
    print('A goblin attacks. Defend yourself!')
    gob1 = Goblin('Goblin', 6)
    combat(hero, gob1)
    slain['Goblin'] += 1
    while True:
        print('*'* 75)
        contin = input('Venture forth? (Y/N)').lower()
        if contin == 'y':
            slain = venture(slain)
        elif contin == 'n':
            retire(slain)
        else:
            print('Invalid entry')
 
def venture(slain):
    print()
    slain = slain
    quest = randint(1,100)
    if quest >= 1 and quest <= 33:
        print("It's another goblin! Defend yourself!")
        gob = Goblin('Goblin', 8)
        combat(hero, gob)
        slain['Goblin'] += 1
    elif quest >= 34 and quest <= 60:
        print("A shambling corpse approaches!")
        zom = Zombie('Zombie', 12)
        combat(hero, zom)
        slain['Zombie'] += 1
    elif quest >= 61 and quest <= 70:
        print("A big looking goblin attacks! Defeat him!")
        gob = Goblin('Goblin', 10)
        combat(hero, gob)
        slain['Goblin'] += 1
    elif quest >= 71 and quest <= 95:
        input('A treasure chest! As you go to open it...')
        loot = randint(1,20)
        if loot >=1 and loot <= 10:
            print('You found a potion. That\'ll come in handy.')
            hero.potions += 1
        elif loot >= 11 and loot <= 15:
            print('There\'s 2 potions! Lucky!')
            hero.potions += 2
        elif loot >= 16 and loot <= 19:
            print('The chest has teeth and it attacks! What sick bastard thought of this!?')
            mim = Mimic('Mimic', 10)
            combat(hero, mim)
            slain['Mimic'] += 1
        else:
            if hero.weapon.name == 'Sword':
                print('A gleaming golden sword is in the chest. It looks far better than yours.')
                print('Good thing anything left in chests is free for the taking! /Get!')
                hero.weapon = Weapon('Excalibur', 6, 8)
                print('You got Excalibur!')
            else:
                print('3 potions! Who is leaving these here?')
                hero.potions += 3
            
    elif quest >= 96 and quest <= 100:
        print("A menacing looking Hobgoblin attacks! Fight for you life!")
        hob = Hobgoblin('Hobgoblin', 15)
        combat(hero, hob)
        slain['Hobgoblin'] += 1
    return slain
    
def retire(slain):
    slain = slain
    print('\nFinal Tally:\n')
    for key, value in slain.items():
        print(key + ': '+ str(value))
    print('\n{} potions left'.format(hero.potions))
    score = 0
    score += slain['Goblin'] * 50
    score += slain['Zombie'] * 40
    score += slain['Mimic'] * 70
    score += slain['Hobgoblin'] * 100
    score += hero.potions * 30
    print()
    out = 'TOTAL SCORE: {}'.format(score)
    print('*' * (len(out) + 4))
    print('* ' + out + ' *')
    print('*' * (len(out) + 4))
    exit()

hero = Hero('Hero', 12)

main()
