#!/usr/bin/python
import sys
import pygame
from sudoku import SudokuBoard

width = 542
height = 600
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((width,height))

myboard = SudokuBoard()
while myboard.gameOn:
	myboard.boardEvents()


