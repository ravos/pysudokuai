#!/urs/lib/python
import sys
import pygame



def eliminate(self):
	for grid in self.gridList:
		if grid.tempNum:
			for i in self.row[grid.row]:
				if grid.tempNum in self.gridList[i].candidates:
					self.gridList[i].candidates.remove(grid.tempNum)
			for i in self.col[grid.col]:
				if grid.tempNum in self.gridList[i].candidates:
					self.gridList[i].candidates.remove(grid.tempNum)
			for i in self.box[grid.box]:
				if grid.tempNum in self.gridList[i].candidates:
					self.gridList[i].candidates.remove(grid.tempNum)
	return False
