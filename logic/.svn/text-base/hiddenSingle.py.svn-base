#!/urs/lib/python
import sys
import pygame

from eliminate import eliminate
from hint import hint

def hiddenSingle(self, getOne = False):
	ifFound = False
	eliminate(self)
	for unit in self.row:
		tempList = []
		for i in unit:
			tempList = tempList + self.gridList[i].candidates
		for num in range(1,10):
			if tempList.count(num) == 1:
				for i in unit:
					if num in self.gridList[i].candidates:
						self.hints.append(hint('Hidden Single', 1, [self.gridList[i].row, self.gridList[i].col], num))
						ifFound = True
						print 'Found 1 at (',self.gridList[i].row+1,',',self.gridList[i].col+1,')'
						if getOne:
							return ifFound

	for unit in self.col:
		tempList = []
		for i in unit:
			tempList = tempList + self.gridList[i].candidates
		for num in range(1,10):
			if tempList.count(num) == 1:
				for i in unit:
					if num in self.gridList[i].candidates:
						self.hints.append(hint('Hidden Single', 1, [self.gridList[i].row, self.gridList[i].col], num))
						ifFound = True
						print 'Found 1 at (',self.gridList[i].row+1,',',self.gridList[i].col+1,')'
						if getOne:
							return ifFound

	for unit in self.box:
		tempList = []
		for i in unit:
			tempList = tempList + self.gridList[i].candidates
		for num in range(1,10):
			if tempList.count(num) == 1:
				for i in unit:
					if num in self.gridList[i].candidates:
						self.hints.append(hint('Hidden Single', 1, [self.gridList[i].row, self.gridList[i].col], num))
						ifFound = True
						print 'Found 1 at (',self.gridList[i].row+1,',',self.gridList[i].col+1,')'
						if getOne:
							return ifFound

	return ifFound
