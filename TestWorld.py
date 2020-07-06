import pygame
from World import World
from TestActor import TestActor
from TestCollision import TestCollision


class TestWorld(World):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.add_actor(TestActor(), 100, 200)
        self.add_actor(TestCollision(), 500, 200)

    def act(self):
        return
