#    Isaac Stats Tracker - Tracks & Displays Stats
#    Copyright (C) 2015 Andrew Zah
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from ISTPlayer import Player
from ISTGraphics import *
import re
import time
player = Player(
			"", 0, 0, "", 0.00, 0.00, 0.00, 
			0, 0.0, 0.0, 0, 0, 0, 0,
			[], "", [], []
		)
def createPlayer(subtype):
	if subtype == 0:
		player = Player(
			"Isaac", 0, 3, "red", 0.00, 1.00, 23.75,
			0, 1.0, 1.0, 0, 1, 0, 0,
			[], "", [], []
		)
	if subtype == 1:
		player = Player(
			"Magdalene", 1, 4, "red", 0.00, 1.00, 23.75,
			0, 0.85, 1.0, 0, 0, 0, 0,
			[], "", ["45"], []
		)
	if subtype == 2:
		player = Player(
			"Cain", 2, 2, "red", 0.00, 1.00, 17.75,
			0, 1.3, 1.20, 1, 0, 0, 0,
			[], "", ["46"], []
		)
	if subtype == 3:
		player = Player(
			"Judas", 3, 1, "red", 0.00, 1.00, 23.75,
			0, 1.0, 1.35, 1, 0, 3, 0,
			[], "", ["34"], []
		)
	if subtype == 4:
		player = Player(
			"???", 4, 3, "soul", 0.00, 1.00, 23.75,
			0, 1.1, 1.05, 1, 0, 3, 0,
			[], "", ["36"], []
		)
	if subtype == 5:
		player = Player(
			"Eve", 5, 2, "red", 0.00, 1.00, 23.75,
			0, 1.23, 1.0, 1, 0, 3, 0,
			[], "", ["117", "122"], []
		)
	if subtype == 6:
		player = Player(
			"Samson", 6, 3, "red", -0.05, 1.31, 23.75,
			0, 1.23, 1.0, 1, 0, 3, 0,
			[], "", ["117", "122"], []
		)
	if subtype == 7:
		player = Player(
			"Azazel", 7, 3, "red", 0.50, 1.00, 17.75,
			0, 1.25, 1.0, 1, 0, 0, 0,
			[], "", ["118"], []
		)

	if subtype == 8:
		player = Player(
			"Lazarus", 8, 3, "black", 0.00, 1.00, 17.75,
			-1, 1.0, 1.0, 0, 0, 0, 0,
			[], "", [], []
		)
	#eden is all random..
	if subtype == 9:
		player = Player(
			"Eden", 9, 3, "red", 0.70, 1.00, 23.75,
			0, 1.0, 1.0, 0, 0, 0, 0,
			[], "", [], []
		)
	if subtype == 10:
		player = Player(
			"The Lost", 10, 0, "", 0.00, 1.00, 23.75,
			0, 1.0, 1.0, 0, 0, 1, 0,
			[], "", [], []
		)
	return player

while True:
	regexValues = {
		'newGame': r'^RNG Start Seed: (.{9})(.+?)$',
		'newPlayer': r'^(Initialized player with )(.{9})( and )(.+?)$',
		'newItem': r'^(Adding collectible )(.{2,3}) (.+?)$',
		'newBoss': r'^(Boss )(\d{1,2})(.+?)$',
		'newPillAction': r'^(Action PillCard Triggered)$',
		'newLevel': r'^(.{18})(stage \d{1,3}: )(.+?)$',
		'newRoomEntered': r'^(Room )(\S{3,4})' #^(Room )(\d{1,2}.\d{1,2})(.+?)$
	}
	logFile = open('log.txt', 'r')
	seedValues = []

	for line in logFile:
		newGameMatches = re.match(regexValues['newGame'], line, re.M)
		newPlayerMatches = re.match(regexValues['newPlayer'], line, re.M)
		newItemMatches = re.match(regexValues['newItem'], line, re.M)
		newBossMatches = re.match(regexValues['newBoss'], line, re.M)
		newPillActionMatches = re.match(regexValues['newPillAction'], line, re.M)
		newLevelMatches = re.match(regexValues['newLevel'], line, re.M)
		newRoomEnteredMatches = re.match(regexValues['newRoomEntered'], line, re.M)

		if newGameMatches:
			seedValues.append(newGameMatches.group(1))
		if newPlayerMatches:
			subtype = int(newPlayerMatches.group(4)[-1])
			player = createPlayer(subtype)
		if newItemMatches:
			player.items.append(newItemMatches.group(2))
		if newBossMatches:
			player.bosses.append(newBossMatches.group(2))
		if newPillActionMatches:
			player.pillsUsed += 1
		if newLevelMatches:
			player.currentLevel = newLevelMatches.group(2) + newLevelMatches.group(3)
		if newRoomEnteredMatches:
			player.roomsEntered.append(newRoomEnteredMatches.group(2))

	displayGraphics(player)
	pygame.event.pump()
	logFile.close()
	time.sleep(5)

	#debug
	print "----------------------------------------"
	print "Current Seed: " + seedValues[-1]
	print "Current Character: " + player.name
	print "Pills Used: " + str(player.pillsUsed)
	print "Bosses Slain: "
	for boss in player.bosses:
		print boss
	player.items = sorted(set(player.items))
	print "Current Items: "
	for item in player.items:
		print item
	player.roomsEntered = sorted(set(player.roomsEntered))
	print "Rooms Entered: " + str(len(player.roomsEntered))