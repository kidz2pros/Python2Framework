import pygame
from World import World

world = World(0, 0)
change_world = True
ended = False


def set_world(new_world):
    global world
    world = new_world



