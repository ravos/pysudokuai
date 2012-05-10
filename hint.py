#!/urs/lib/python
import sys
import pygame

#define the grid of the board
class hint:
	def __init__(self, name, logicID, pos, num, ifRemove = False):
		
		self.name = name
		self.logicID = logicID
		self.row = pos[0]
		self.col = pos[1]
		self.num = num
		self.ifSet = (ifRemove == False)
		self.ifRemove = ifRemove

	
