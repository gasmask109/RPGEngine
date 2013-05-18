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

class GameCharacter():
    def move(self, self.target):
        selectedMove = self.selectedMove
        for target in self.targets:
            selectedMove(target)

def combatLoop(party, enemies):
    while partyAlive > 0 and enemiesAlive > 0:
        for character in party:
            character.moveSelect(party, enemies)
        for character in party:
            character.move(character.targets)
        for enemy in enemies:
            enemy.attactPattern(enemies, party)
            enemy.move(enemy.targets)
            
