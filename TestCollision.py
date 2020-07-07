from Actor import Actor
from TestActor import TestActor


class TestCollision(Actor):

    def __init__(self):
        super(TestCollision, self).__init__()

    def act(self):
        actors = self.world.get_actors_of_type(TestActor)
        if actors:
            self.turn_towards(actors[0].x, actors[0].y)
        self.collide()
        self.move(1)

    def collide(self):
        intersector = self.get_one_intersector(TestActor)
        if intersector is not None:
            self.world.remove_actor(intersector)
