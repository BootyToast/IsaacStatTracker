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

class Player:
	def __init__(
		self, name, pid, health, healthType, tearFireDelay, tearSpeed, tearRange, 
		luck, movementSpeed, damageModifier, keys, bombs, coins, pillsUsed, 
		roomsEntered, currentLevel, items, bosses
	):

		self.name = name
		self.pid = pid
		self.health = health
		self.healthType = healthType
		self.tearFireDelay = tearFireDelay
		self.tearSpeed = tearSpeed
		self.tearRange = tearRange
		self.luck = luck
		self.movementSpeed = movementSpeed
		self.damageModifier = damageModifier
		self.keys = keys
		self.bombs = bombs
		self.coins = coins
		self.pillsUsed = pillsUsed
		self.roomsEntered = roomsEntered
		self.currentLevel = currentLevel
		self.items = items
		self.bosses = bosses