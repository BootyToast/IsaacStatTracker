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

import pygame
from pygame.locals import *
import time
import glob
import re

itemsToDisplay = []
bossesToDisplay = []
currentBossesToDisplay = []
currentItemsToDisplay = []

pygame.init()
canvas = pygame.display.set_mode((715,500))
pygame.display.set_caption('Isaac Stat Tracker')
	
background = pygame.Surface(canvas.get_size())
background = background.convert()
background.fill((0, 241, 15))

canvas.blit(background, (0, 0))
pygame.display.update()

class NewPicture:
	def __init__( self, x, y, w, h, fileLocation ):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.fileLocation = fileLocation

def collectFiles(player):
	itemFileRegex = r'(ISTData/images/items\\)(\d{1,3})(.+)$'
	for item in player.items:
		for fileName in glob.glob('ISTData/images/items/*'):
			if item == re.match(itemFileRegex, fileName, re.M).group(2):
				foundItem = NewPicture(0, 0, 64, 64, fileName)
				itemsToDisplay.append(foundItem)

	bossFileRegex = r'(ISTData/images/bosses\\)(\d{1,3})(.+)$'
	for boss in player.bosses:
		for fileName in glob.glob('ISTData/images/bosses/*'):
			if boss == re.match(bossFileRegex, fileName, re.M).group(2):
				foundBoss = NewPicture(0, 0, 64, 64, fileName)
				bossesToDisplay.append(foundBoss)

def handleEvents():
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			pass
		elif event.type == MOUSEBUTTONUP:
			pass
		elif event.type == MOUSEBUTTONDOWN:
			pass

def displayGraphics(player):
	global itemsToDisplay
	global bossesToDisplay
	global currentItemsToDisplay
	global currentBossesToDisplay
	global canvas

	itemsToDisplay = []
	bossesToDisplay = []
	collectFiles(player)

	i, j = 0, 0
	if currentItemsToDisplay != itemsToDisplay:
		currentItemsToDisplay = itemsToDisplay
		if itemsToDisplay == []:
			canvas.blit(background, (0, 0))
		for item in itemsToDisplay:
			img = pygame.image.load(item.fileLocation)
			img = pygame.transform.scale(img, (64, 64))
			canvas.blit(img, (item.x + i, item.y + j))
			
			i += 64
			if i > 700:
				i = 0
				j += 64

	i, j = 0, 300
	if currentBossesToDisplay != bossesToDisplay:
		currentBossesToDisplay = bossesToDisplay
		if bossesToDisplay == []:
			canvas.blit(background, (0, 0))
		for boss in bossesToDisplay:
			img = pygame.image.load(boss.fileLocation)
			img = pygame.transform.scale(img, (64, 64))
			canvas.blit(img, (boss.x + i, boss.y + j))
			
			i += 64
			if i > 700:
				i = 0
				j += 64

	#debug
	print "Graphics Portion"
	print "-------------------------"
	pygame.event.pump()
	print "About to Update Display:"
	print "Item Instances:"
	for item in currentItemsToDisplay:
		print item
	print "Boss Instances:"
	for boss in currentBossesToDisplay:
		print boss
	pygame.display.update()
	handleEvents()