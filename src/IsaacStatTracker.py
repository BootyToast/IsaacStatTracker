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

def createPlayer(subtype):
	if subtype == 0:
		player = Player( "Isaac", 0, 0, [], "", [], [], [] )
	elif subtype == 1:
		player = Player( "Magdalene", 0, 0, [], "", [], [], [] )
	elif subtype == 2:
		player = Player( "Cain", 0, 0, [], "", [], [], [] )
	elif subtype == 3:
		player = Player( "Judas", 0, 0, [], "", [], [], [] )
	elif subtype == 4:
		player = Player( "???", 0, 0, [], "", [], [], [] )
	elif subtype == 5:
		player = Player( "Eve", 0, 0, [], "", [], [], [] )
	elif subtype == 6:
		player = Player( "Samson", 0, 0, [], "", [], [], [] )
	elif subtype == 7:
		player = Player( "Azazel", 0, 0, [], "118", [], [], [] )
	elif subtype == 8:
		player = Player( "Lazarus", 0, 0, [], "", [], [], [] )
	elif subtype == 9:
		player = Player( "Eden", 0, 0, [], "", [], [], [] )
	elif subtype == 10:
		player = Player( "The Lost", 0, 0, [], "", [], [], [] )
	else:
		player = Player( "Unknown", 0, 0, [], "", [], [], [] )
	return player

def debugLog(seedValues, player):
	print "----------------------------------------"
	if seedValues:
		print "Current Seed: " + seedValues[-1]
	print "Current Character: " + player.name
	print "Pills Used: " + str(player.pillsUsed)
	print "Bosses Slain: "
	for boss in player.bosses:
		print boss
	print "MiniBosses: "
	for miniBoss in player.miniBosses:
		print miniBoss
	player.items = sorted(set(player.items))
	print "Current Items: "
	for item in player.items:
		print item
	player.roomsEntered = sorted(set(player.roomsEntered))
	print "Rooms Entered: " + str(len(player.roomsEntered))

while True:

	regexValues = {
		'newGame': r'^RNG Start Seed: (.{9})(.+?)$',
		'newPlayer': r'^(Initialized player with )(.{9})( and )(.+?)$',
		'newItem': r'^(Adding collectible )(.{1,3}) (.+?)$',
		'newBoss': r'^(Boss )(\d{1,2})(.+?)$',
		'newMiniBoss': r'(MiniBoss )(\d{1,2})(.+?)$',
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
		newMiniBossMatches = re.match(regexValues['newMiniBoss'], line, re.M)
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
		if newMiniBossMatches:
			player.miniBosses.append(newMiniBossMatches.group(2))	
		if newPillActionMatches:
			player.pillsUsed += 1
		if newLevelMatches:
			player.currentLevel = newLevelMatches.group(2) + newLevelMatches.group(3)
		if newRoomEnteredMatches:
			player.roomsEntered.append(newRoomEnteredMatches.group(2))

	player.items = sorted(set(player.items))
	displayGraphics(player)
	pygame.event.pump()
	logFile.close()
	debugLog(seedValues, player)
	time.sleep(5)