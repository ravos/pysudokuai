#!/urs/lib/python
import sys
import pygame

#define the grid of the board
class sudokuGrid:
	#def initialization
	def __init__(self,size,ind,tempNum,Screen):
		
		self.ind = ind		# ind = 9*row+column
		self.row = ind / 9	# row = row#
		self.col = ind % 9	# col = column#
		self.box = (self.row / 3) * 3 + self.col / 3
		self.posX = self.col * size + (self.col / 3) * 1
		self.posY = self.row * size + (self.row / 3) * 1
 		
		self.fixed = False
		if tempNum:
			self.setTempNum(tempNum)
			self.fixed = True		
		else:
			self.setTempNum(0)
		self.selected = False
		self.showCandidates = False
		self.highlights = []

		# For Display Use
		self.highlight = False
		self.size = size  #size is the length of width and height in pixels
		self.gridSurface = pygame.Surface((size,size))
		self.gridSurface.set_colorkey((0,0,0))
		self.mainScreen = Screen


	#def setTempNum(self)
	def setTempNum(self,num):
		if self.fixed: return False
		else :
			self.tempNum = num
			if num == 0:
				self.candidates = range(1,10)
			else:
				self.candidates = []

	#display the notes in the grid
	def displayNotes(self):
		if self.fixed: return False
		if self.tempNum > 0: return False
		if self.showCandidates is False: return False
		pos = [(10,10),(30,10),(50,10),(10,30),(30,30),(50,30),(10,50),(30,50),(50,50)]
		noteFont = pygame.font.Font('Arial.ttf', 24)
		for num in self.candidates:
			(xpos,ypos) = pos[num - 1]
			#display the number
			noteText = noteFont.render(str(num),True,(0,128,255))
			noteRect = noteText.get_rect()
			noteRect.centerx = xpos
			noteRect.centery = ypos
			self.gridSurface.blit(noteText,noteRect)
				
	#display the tempNum
	def displayNum(self):
		numFont = pygame.font.Font('Arial.ttf', 48)
		if self.fixed:			
			bgNum = numFont.render(str(self.tempNum),True,(10,10,10))
			numRect = bgNum.get_rect()
			numRect.centerx = self.gridSurface.get_rect().centerx
			numRect.centery = self.gridSurface.get_rect().centery
			self.gridSurface.blit(bgNum,numRect)
			#display the current number
		elif self.tempNum > 0:
			bgNum = numFont.render(str(self.tempNum),True,(0,128,255))
			numRect = bgNum.get_rect()
			numRect.centerx = self.gridSurface.get_rect().centerx
			numRect.centery = self.gridSurface.get_rect().centery
			self.gridSurface.blit(bgNum,numRect)
			#display the tempNum
		else:
			a = 'do nothing'
			#display nothing
	

	#display the grid, edge color, elected or not
	def displayGrid(self):
		rect = pygame.Rect(0,0,self.size,self.size)      #be a property?
		# FILL
		if self.selected:
			self.gridSurface.fill((255,128,0))
		else:
			self.gridSurface.fill((255,255,255))
		# EDGE
		pygame.draw.rect(self.gridSurface,(1,1,1),rect,1)
		self.displayNotes()
		self.displayNum()
		self.mainScreen.blit(self.gridSurface,(self.posX, self.posY))
		
	#set the usable nums set
	def setUsableNums(self,numsSet):
		self.usableNums = numsSet
