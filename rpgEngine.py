#  Copyright 2013 Steve Hardy <fatcat32594@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class Struct(): pass

class Party():
    def __init__(self, a):
        self.members = a
        self.aliveMembers()
        
    def aliveMembers(self):
        self.alive = 0
        for each in self.members:
            if each.alive == True:
                self.alive += 1
        return self.alive

class GameCharacter():
    @classmethod
    def __init__(self):
        self.progression = Struct()
        self.level = 1
        self.alive = True
        
    def move(self, target):
        if self.alive == True:
            for target in self.targets:
                self.selectedMove(target)
            
class PlayerCharacter():
    @classmethod
    def __init__(self):
        GameCharacter.__init__()
        
    def moveSelect(party, enemies):
        category = raw_input("Attack or Defend\n")
        if category == "Attack": self.selectedMove = "Attack"
        elif category == "Defend": self.selectedMove = "Defend"
        else:
            print "Please try again\n"
            moveSelect(party, enemies)
        
class Fighter(GameCharacter):
    def __init__(self):
        PlayerCharacter.__init__()
        self.progression.stre = 5
        self.progression.dex = 3
        self.progression.con = 4
        self.progression.intel = 1
        self.progression.wis = 2 
        
class Rogue(GameCharacter):
    def __init__(self):
        PlayerCharacter.__init__()
        self.progression.stre = 3
        self.progression.dex = 5
        self.progression.con = 2
        self.progression.intel = 4
        self.progression.wis = 1
        
class Wizard(GameCharacter):
    def __init__(self):
        PlayerCharacter.__init__()
        self.progression.stre = 1
        self.progression.dex = 3
        self.progression.con = 1
        self.progression.intel = 6
        self.progression.wis = 2
        
class Cleric(GameCharacter):
    def __init__(self):
        PlayerCharacter.__init__()
        self.progression.stre = 1
        self.progression.dex = 1
        self.progression.con = 2
        self.progression.intel = 2
        self.progression.wis = 6

def combatLoop(party, enemies):
    while party.alive > 0 and enemies.alive > 0:
        for character in party:
            character.moveSelect(party, enemies)
        for character in party:
            character.move(character.targets)
        for enemy in enemies:
            enemy.attactPattern(enemies, party)
            enemy.move(enemy.targets)
        party.aliveMembers()
        enemies.aliveMembers()

def engineTest():
    roran = Fighter()
    roran.level += 1
    assert roran.level == 2
    dalia = Rogue()
    assert dalia.level == 1
    playerParty = Party([roran, dalia])
    assert playerParty.aliveMembers() == 2
    roran.alive = False
    assert playerParty.aliveMembers() == 1
    

if __name__ == '__main__':
	engineTest()
