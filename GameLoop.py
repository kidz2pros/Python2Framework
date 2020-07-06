import pygame
from TestActor import TestActor


class GameLoop:

    def __init__(self, worlds):
        self.worlds = worlds
        self.running = True
        self.active_world = worlds[0]

    def set_world(self, world):
        self.active_world = world

    def execute_event_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.active_world.manage_actions()
            self.active_world.actor_bounds()
            self.active_world.draw_screen()
            pygame.display.update()

