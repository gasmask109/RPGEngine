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

class GameCharacter():
    @classmethod
    def __init__(self):
        self.progression = Struct()
        self.level = 1
        
    def move(self, target):
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
        self.progression.strength = 5
        self.progression.dex = 0
        
class Rogue(GameCharacter):
    def __init__(self):
        PlayerCharacter.__init__()
        self.progression.strength = 0
        self.progression.dex = 5
        
class Wizard(GameCharacter):
    def __init__(self):
        PlayerCharacter.__init__()
        self.progression.strength = 0
        self.progression.dex = 0

def combatLoop(party, enemies):
    while partyAlive > 0 and enemiesAlive > 0:
        for character in party:
            character.moveSelect(party, enemies)
        for character in party:
            character.move(character.targets)
        for enemy in enemies:
            enemy.attactPattern(enemies, party)
            enemy.move(enemy.targets)

def engineTest():
    roran = Fighter()
    roran.level += 1
    assert roran.level == 2
    dalia = Rogue()
    assert dalia.level == 2

if __name__ == '__main__':
	engineTest()
