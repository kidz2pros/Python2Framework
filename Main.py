import pygame
from GameLoop import GameLoop
from TestWorld import TestWorld

pygame.init()

width = 800
height = 600


game = GameLoop([TestWorld(width, height)])

game.execute_event_loop()
