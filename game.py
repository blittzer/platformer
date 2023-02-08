### Setting file ###
#############################################
import sys
sys.path.insert(0, './classes')

### The Imports ###
#############################################
import pygame
from gameLoop import GameLoop


### The Global Constants ###
#############################################


def main():
	g = GameLoop()
	g.loop()

if __name__ == '__main__':
	main()