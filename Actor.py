import pygame
import abc
import math


class Actor:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.image = pygame.image.load('default.png')
        self.display = pygame.transform.rotate(self.image, 0)
        self.world = None

    @abc.abstractmethod
    def act(self):

        return

    def set_location(self, x, y):
        self.x = x
        self.y = y

    def turn(self, increment):
        self.rotation += increment
        self.rotation %= 360
        self.rotate_image()

    def set_rotation(self, rotation):
        if rotation != self.rotation:
            self.rotation = rotation
            self.rotate_image()

    def set_image(self, image):
        self.image = image
        self.display = pygame.transform.rotate(self.image, self.rotation)

    def rotate_image(self):
        self.display = pygame.transform.rotate(self.image, self.rotation % 360)

    def draw_self(self, screen):
        screen.blit(self.display, (self.x,self.y))

    def added_to_world(self, world):
        return

    def move(self, distance):
        radians = math.radians(self.rotation)
        dx = math.cos(radians) * distance
        dy = math.sin(radians) * distance
        self.set_location(self.x + dx, self.y + dy)

    def intersects(self, actor):
        rect = self.display.get_bounding_rect()
        test_rect = rect.move(self.x, self.y)
        other_rect = actor.display.get_bounding_rect()
        test_other_rect = other_rect.move(actor.x, actor.y)
        return test_rect.colliderect(test_other_rect)

    def get_all_intersectors(self, type):
        intersectors = []
        actors = self.world.get_actors_of_type(type)
        if self in actors:
            actors.remove(self)
        for actor in actors:
            if self.intersects(actor):
                intersectors.append(actor)
        return intersectors

    def get_one_intersector(self, type):
        intersectors = self.get_all_intersectors(type)
        if intersectors:
            return intersectors[0]
        return




