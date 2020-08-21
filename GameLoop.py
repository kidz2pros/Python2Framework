import pygame
from World import World
import PlayerInput
import GameUtilities


class GameLoop:

    def __init__(self, worlds):
        self.worlds = worlds
        self.running = True
        GameUtilities.world = worlds[0]
        self.clock = pygame.time.Clock()

    def execute_event_loop(self):
        while self.running:
            time_passed = self.clock.tick(50)
            PlayerInput.reset_key_list()
            for event in pygame.event.get():
                PlayerInput.key_input_listener(event)
                if event.type == pygame.QUIT:
                    running = False
            GameUtilities.world.manage_actions()
            GameUtilities.world.actor_bounds()
            GameUtilities.world.draw_screen()
            pygame.display.update()
            print(GameUtilities.world)

