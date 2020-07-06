import pygame
from Actor import Actor


class TestActor(Actor):

    def __init__(self):
        super(TestActor, self).__init__()

    def act(self):
        self.move(2)
