import pygame
from Actor import Actor
import PlayerInput

class TestActor(Actor):

    def __init__(self):
        super(TestActor, self).__init__()

    def act(self):
        self.key_commands()

    def key_commands(self):
        if PlayerInput.is_key_down(pygame.K_LEFT):
            self.set_location(self.x - 1, self.y)
        if PlayerInput.is_key_down(pygame.K_RIGHT):
            self.set_location(self.x + 1, self.y)
        if PlayerInput.is_key_down(pygame.K_UP):
            self.set_location(self.x, self.y - 1)
        if PlayerInput.is_key_down(pygame.K_DOWN):
            self.set_location(self.x, self.y + 1)
