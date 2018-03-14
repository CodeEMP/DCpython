from random import *
import equipment
    
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.maxhp = hp
    weapon = equipment.Weapon()
    armor = equipment.unArmored()
    def alive(self):
        if self.hp < 1:
            return False
        else:
            return True
    def check_status(self):
        print('{} has {} health left.'.format(self.name, self.hp))
    def attack(self, target):
        dmg = self.weapon.weapon_damage()
        dmg -= target.armor.defense()
        if dmg < 1:
            dmg = 1
        else:
            pass
        print('{} attacks with it\'s {}, dealing {} damage.'.format(self.name, self.weapon.name, dmg))
        return dmg
        
class Hero(Character):
    potions = 3
    weapon = equipment.Sword()
    zenny = 1
    starting_power = 0
    power = starting_power
    armor = equipment.chainMail()
    def attack(self, target):
        dmg = self.weapon.weapon_damage()
        crit = randint(1, 20)
        if crit == 20:
            dmg += self.power
            dmg *= 2
            dmg -= target.armor.defense()
            if dmg < 1:
                dmg = 1
            else:
                pass
            print('You attack with your {}, it crits for {} damage!'.format(self.weapon.name, dmg))
        else:
            dmg += self.power
            dmg -= target.armor.defense()
            if dmg < 1:
                dmg = 1
            else:
                pass
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
    
    def full_heal(self):
        self.hp = self.maxhp
        self.check_status()

class Enemy(Character):
    hurt = ''
    unhurt = ''
    
    def check_status(self):
        if self.hp/self.maxhp * 100 <= 50:
            print(self.hurt)
        else:
            print(self.unhurt)
            
class Goblin(Enemy):
    hurt = 'The goblin is looking injured.'
    unhurt = 'The goblin seems to be in good health.'
    weapon = equipment.Dagger()
    bounty = 2

class Zombie(Enemy):
    hurt = 'The zombie is looking more corpsey.'
    unhurt = 'The zombie shambles energetically.'
    weapon = equipment.Dagger()
    bounty = 1

class Bandit(Enemy):
    hurt = 'The bandit is questioning his life choices.'
    unhurt = 'The bandit seems eager to loot you.'
    weapon = equipment.shortSword()
    bounty = 4
    
class Mimic(Enemy):
    unhurt = 'The mimic is still terrifying.'
    hurt = 'The mimic looks pretty broken, but is still terrifying.'
    weapon = equipment.shortSword()
    bounty = 5
    
class Hobgoblin(Enemy):
    hurt = 'The Hobgoblin is looking a little more worried.'
    unhurt = 'The Hobgoblin smirks.'
    weapon = equipment.Sword() 
    bounty = 10
    armor = equipment.chainMail()
