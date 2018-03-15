from random import *

class Weapon:
    name = None
    weapdmgmin = None
    weapdmgmax = None
    def weapon_damage(self):
        dmg = randint(self.weapdmgmin, self.weapdmgmax)
        return dmg

class Sword(Weapon):
    name = 'Sword'
    weapdmgmin = 3
    weapdmgmax = 5

class Dagger(Weapon):
    name = 'Dagger'
    weapdmgmin = 1
    weapdmgmax = 2

class shortSword(Weapon):
    name = 'Short Sword'
    weapdmgmin = 2
    weapdmgmax = 4

class longSword(Weapon):
    name = 'Long Sword'
    weapdmgmin = 4
    weapdmgmax = 6

class Excalibur(Weapon):
    name = 'Excalibur'
    weapdmgmin = 6
    weapdmgmax = 8

class Bite(Weapon):
    name = 'Bite'
    weapdmgmin = 3
    weapdmgmax = 4
    
class Armor:
    name = None
    armor = 0
    def defense(self):
        return self.armor

class unArmored(Armor):
    name = 'Unarmored'

class chainMail(Armor):
    name = 'Chainmail'
    armor = 1

class plateMail(Armor):
    name = 'Platemail'
    armor = 2