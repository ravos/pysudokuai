#!/usr/bin/python
import sys
import time
import os
import pygame

from sys 		import stdout
from pygame.locals 	import *
from sudokuGrid 	import sudokuGrid

from hint 		import hint
sys.path.append('./logic')
from eliminate 		import eliminate
from nakedSingle 	import nakedSingle
from hiddenSingle 	import hiddenSingle

class SudokuBoard:
	#initialize the sudokuboard
	def __init__(self,fn_puzzle = None):
		self.gameOn = True
		#initialize the grids
		        
		self.name = ''
		self.gridSize = 60
		self.width = 544
		self.height = 600
		self.focus = -1

		self.row = [[],[],[],[],[],[],[],[],[]]
		self.col = [[],[],[],[],[],[],[],[],[]]
		self.box = [[],[],[],[],[],[],[],[],[]]
		
		for i in range(81):
			self.row[i//9].append(i)
			self.col[i%9].append(i)
			self.box[(i//9)//3*3 + i%9//3].append(i)
		
		self.surface = pygame.display.get_surface()
		self.loadBoard(fn_puzzle)
		self.printBoard('bg.jpg')

		self.hints = []
		
		
	#load board from file: fn_puzzle
	def loadBoard(self, fn_puzzle = None):
		self.board = self.parseBoard(fn_puzzle)
		self.gridList = [sudokuGrid(self.gridSize,i,self.board[i/9][i%9],self.surface) for i in range(81)]
		self.displayBoard()
		

	#parse the board txt file
	def parseBoard(self,fn_puzzle):
		if fn_puzzle is not None:
			board_file = open(fn_puzzle,'r')
			board_content = board_file.readlines();
			#print board_content
			#['0' for elem in [board_line for board_line in board_content] if elem == '.']
			board_content = [board_line[0:9].replace('.','0') for board_line in board_content[0:9]]
			print(board_content)
			temp_board = [[int(num) for num in line] for line in board_content]
		else:
			temp_board = [[0 for i in range(9)] for j in range(9)]
		return temp_board
	
	#print the board at the begining
	def printBoard(self,imgName):
		bgImg = pygame.image.load(imgName)
		bgImg = bgImg.convert()
		self.surface.blit(bgImg,(0,0))
		self.displayBoard()

	#display the board: usually used for refresh
	def displayBoard(self):
		for grid in self.gridList:
			grid.displayGrid()
		pygame.display.flip()		

	#turn all notes on
	def setShowCandidates(self, showCandidates):
		for grid in self.gridList:
			grid.showCandidates = showCandidates
	
	#wait for the event sequence
	def boardEvents(self):
		events = pygame.event.get()
		for event in events:
			#print event
			if event.type == MOUSEBUTTONDOWN:
				grid_pos = event.pos
				if event.button == 3 or grid_pos[1] > 540:
					if self.focus is not -1:
						self.gridList[self.focus].selected = 0
						self.focus = -1
					self.displayBoard()

				elif event.button == 1:
					(g_row,g_col) = (grid_pos[1]/self.gridSize,grid_pos[0]/self.gridSize)
					tempPos = 9*g_row + g_col
					
					if self.focus is not -1:
						self.gridList[self.focus].selected = 0
					self.focus = tempPos
					self.gridList[self.focus].selected = 1
				else:
					print(event)
				self.displayBoard()

			elif event.type == KEYDOWN:
				key = event.key
				#print key
				if key >= 49 and key <= 57:
				#numKey
					setNum = key - 48
					if self.focus is not -1:
						self.gridList[self.focus].setTempNum(setNum)
						self.displayBoard()

				# C = show/hide Candidates
				elif key == 99:
					if self.gridList[0].showCandidates == True:
						print('Hide candidates')
						self.setShowCandidates(False)
						self.displayBoard()
					else:
						print('Show candidates')
						self.setShowCandidates(True)
						self.displayBoard()

				# H = hints
				elif key == 104:
					for hint in self.hints:
						print(hint.name, hint.row, hint.col, hint.num)

				# E = eliminate candidates
				elif key == 101:
					eliminate(self)
					self.displayBoard()

				# U = Naked Single
				elif key == 117:
					nakedSingle(self)
					self.displayBoard()
			
				# V = Hidden Single
				elif key == 118:
					self.hints = []
					hiddenSingle(self)
					self.displayBoard()

				# D or 0 = delete
				elif key == 100 or key == 48:
					if self.focus is not -1 and self.gridList[self.focus].fixed == False:
						self.gridList[self.focus].setTempNum(0)
						self.displayBoard()

				# Ctrl+S = Save Board
				elif key == 115:
					pygame.key.get_mods()

				# Ctrl+L = Load Board
				elif key == 108:
					if pygame.key.get_mods() & KMOD_CTRL:
						self.name = raw_input('The filename of the puzzle: ')
						fn_puzzle = 'puzzle/q' + self.name + '.txt'
						self.loadBoard(fn_puzzle)

				# Ctrl+N = New Board
				elif key == 110:
					if pygame.key.get_mods() & KMOD_CTRL:
						self.loadBoard()

				# ESC/Ctrl+Q = Exit
				elif key == 27 or (key == 113 and (pygame.key.get_mods() & KMOD_CTRL)):
					print('Exiting. Godd bye!')
					self.gameOn = False
					break
				else:
					print(key)
					continue
			
