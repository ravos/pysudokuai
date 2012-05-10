#!/urs/lib/python
import sys
import pygame

from eliminate import eliminate

def nakedSingle(self):
	eliminate(self)
	for grid in self.gridList:
		if grid.tempNum == 0 and len(grid.candidates) == 1:
			grid.setTempNum(grid.candidates[0])
			print grid.ind
			print 'Found 1 at (',grid.row+1,',',grid.col+1,')'
			return True
	print 'Found none...'
	return False
